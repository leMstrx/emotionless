'''
Everything related to the client
This will later be called from the main.py (emotionless.py)
'''
import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey # type: ignore
from solders.transaction_status import EncodedConfirmedTransactionWithStatusMeta # type: ignore
from config import RPC_URL, COMMITMENT, TOKEN_PROGRAMM_ID
import base64

class SolanaAsyncClient:
    def __init__(self):
        '''
        Initialize the Solana async RPC client with the given RPC URL and commitment.
        '''
        self.client = AsyncClient(endpoint=RPC_URL, commitment=COMMITMENT)
        self.token_program_pubkey = Pubkey.from_string(TOKEN_PROGRAMM_ID)

    async def get_latest_blockhash(self):
        '''
        Async fetch the recent blockhash from the Solana cluster.
        This helps verify that the RPC connection is working            
        '''
        response = await self.client.get_latest_blockhash()
        return response.value.blockhash
    

    
    async def get_transaction_details(self, signature: str):
        """
        Fetch and parse transaction details from the RPC endpoint.
        """
        response = await self.client.get_transaction(
            tx_sig=signature,
            max_supported_transaction_version=0,
            encoding="jsonParsed"  # Ensure we get parsed data
        )
        
        if response.value is None:
            print("No transaction details found.")
            return None

        # Access the parsed transaction details
        try:

            instructions = response.value.transaction.transaction.message.instructions 
                
            for i in instructions:
                if str(i.program_id) == TOKEN_PROGRAMM_ID and i.parsed['type'] in ('initializeMint', 'initializeMint2'):
                    print(f"++++ Found new potential MemeCoin mint transaction ++++")
                    print(f"\nPrint Instruction:{i}")
                    # Check if this instruction is of type `initializeMint`
                    parsed_data = i.parsed
                    print(f"Print Parsed Data:{parsed_data}")
                    print(f"Type: {parsed_data['type']}")
                    if parsed_data['type'] in ('initializeMint', 'initializeMint2'):
                        info = parsed_data["info"]
                        mint_info = {
                            "mint_address": info["mint"],
                            "creator": info["mintAuthority"],
                            "freeze_authority": info.get("freezeAuthority"),
                            "decimals": info["decimals"],
                        }
                        print(mint_info)
                        return mint_info
        except KeyError as e:
            print(f"KeyError while parsing transaction: {e}")
        except Exception as e:
            print(f"Error while processing transaction: {e}")

        return None  # If no `initializeMint` instruction was found
    
    # async def get_token_holders
    # TODO

    # get wallet transactions
    # TODO 

    # Simulate Sell
    # TODO

    # Get Liquidity
    # TODO

    async def close(self):
        '''
        Close the underlying AsyncClient session.
        -> This also closes the RPC Connection
        '''
        await self.client.close()