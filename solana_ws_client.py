'''
Everything related to the websocket client
'''
###

import asyncio
from solana.rpc.websocket_api import connect
from solders.pubkey import Pubkey # type: ignore
from solders.rpc.config import RpcTransactionLogsFilterMentions # type: ignore
from solders.rpc.responses import LogsNotification, SubscriptionResult # type: ignore
from config import WS_URL, TOKEN_PROGRAMM_ID
from solana_client import SolanaAsyncClient
from safety_checks import general_safety_check #Relevant Safety Checks
from websockets.exceptions import ConnectionClosedError
from solana.exceptions import SolanaRpcException

class SolanaWSClient:
    def __init__(self):
        self.ws = None
        self.subscription_id = None
        self.rpc_client = SolanaAsyncClient() #Integrate the RPC client directly in here to streamline
        self.seen_signatures = set() #Keep track of seen signatures to avoid duplicates

    async def connect(self):
        print("Conntecting to WS endpoint...")
        self.ws = await connect(
            WS_URL,
            ping_interval=60, #send a ping every 30s 
            ping_timeout=2000 #if no ping within 30s then timeout (clsoe the connection)
        )

    async def subscribe_to_token_program_logs(self):
        #Subscribe to logs mentioning the token program
        program_pubkey = Pubkey.from_string(TOKEN_PROGRAMM_ID)
        filter_ = RpcTransactionLogsFilterMentions(program_pubkey)
        
        #Subscribe to logs using the filter
        self.subscription_id = await self.ws.logs_subscribe(filter_)
        print(f"Subscribed to logs from Token Program: {TOKEN_PROGRAMM_ID} with subscription id {self.subscription_id}") 

    async def listen_for_new_mints(self):
        print("\n+++ Now listening for new mints +++\n\n\n")
        #This will run indefinetly and yield whenever a log event occurs
        '''
        Info:
        logs is list of strings logged by the program during transaction execuction
        TODO: - Look for something that indication InitializeMint Instruction
              - Figure out which account the mint is 
              - Now also checks for seen duplicates
        For now its just detecting the instructions as proof of concept
        '''
        async for msg_list in self.ws:
            try: 
                #print(f"Received message list: {msg_list}")
                for msg in msg_list:
                    
                    if isinstance(msg, SubscriptionResult):
                        # This is the response to our subscription request
                        self.subscription_id = msg.result
                        #print(f"Subscribed with subscription id: {self.subscription_id}")
                    
                    elif isinstance(msg, LogsNotification):
                        # This is a logs notification 
                        logs = msg.result.value.logs #earlier: msg.params.result.value.logs
                        signature = msg.result.value.signature
                        if signature in self.seen_signatures:
                            continue
                        self.seen_signatures.add(signature)
                        
                        
                        # Filter for InitializeMint and InitializeMint2 instructions
                        if any(instr in " ".join(logs) for instr in ["InitializeMint", "InitializeMint2"]):
                            print("\n\n\n\n\n\n\n\n\n\n+++ Detected InitializeMint Instruction +++\n")
                            #print(f"Received message: {msg}")
                            asyncio.create_task(self.handle_mint_event(signature))

                            #Add a small delay to avoid spamming the RPC endpoint
                            await asyncio.sleep(2) #Maybe adjust timing to improve performance
            except Exception as e:
                print(f"Error while processing logs: {e}")
        
    async def handle_mint_event(self, signature: str):
        #print(f"Processing transaction: {signature}")
        mint_info = await self.rpc_client.get_transaction_details(signature)
        if mint_info: 
            print(f"Mint Adress: {mint_info['mint_address']}")
            print(f"Creator: {mint_info['creator']}")
            print(f"Freeze Authority: {mint_info['freeze_authority']}")
            print(f"Decimals: {mint_info['decimals']}")

            #Perform the general safety checks 
            is_safe = await general_safety_check(self.rpc_client, mint_info)
            if is_safe: 
                print(f"Mint {mint_info['mint_address']} passed all safety checks. Proceeding further")
            else: 
                print(f"Mint {mint_info['mint_address']} failed safety checks. Ignoring this token.")
            
    async def listen_for_new_mints_forever(self):
        '''
        Continuously listens for new mints also if the Websockets closes
        '''
        while True:
            try:
                await self.connect()
                await self.subscribe_to_token_program_logs()
                await self.listen_for_new_mints()
            except ConnectionClosedError as cce:
                print(f"Connection closed unexpectedly: {cce}")
                print("Reconnecting...")
            except (OSError, SolanaRpcException) as e:
                print(f"Network or RPC error occurred: {e}")
                print("Reconnecting...")
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
                print("Reconnecting...")
            finally:
                await self.close()
            print(f"Reconnecting in 5 seconds...")
            await asyncio.sleep(5)

    async def close(self):
        '''
        Closes the websocket client & connection
        '''
        try: 
            if self.subscription_id is not None:
                await self.ws.logs_unsubscribe(self.subscription_id)
            await self.ws.close()
        except Exception as e: 
            print(f"Error while closing WS connection: {e}")
        finally: 
            await self.rpc_client.close() #Also close the RPC Client
        