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

class SolanaWSClient:
    def __init__(self):
        self.ws = None
        self.subscription_id = None

    async def connect(self):
        self.ws = await connect(WS_URL)

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
        For now its just detecting the instructions as proof of concept
        '''
        async for msg_list in self.ws:
            print(f"Received message list: {msg_list}")
            for msg in msg_list:
                print(f"Received message: {msg}")
                
                if isinstance(msg, SubscriptionResult):
                    # This is the response to our subscription request
                    self.subscription_id = msg.result
                    print(f"Subscribed with subscription id: {self.subscription_id}")
                
                elif isinstance(msg, LogsNotification):
                    # This is a logs notification 
                    logs = msg.result.value.logs #earlier: msg.params.result.value.logs
                    for line in logs:  
                        if 'InitializeMint' in line:
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n+++ Detected InitializeMint Instruction +++\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            print(f"New Mint detected: {line}")
                        '''
                        TODO: Extract the mint address from the transaction context
                        '''

    async def close(self):
        '''
        Closes the websocket client & connection
        '''
        if self.subscription_id is not None:
            await self.ws.logs_unsubscribe(self.subscription_id)
        await self.ws.close()