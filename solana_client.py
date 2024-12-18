'''
Everything related to the client
This will later be called from the main.py (emotionless.py)
'''
import asyncio
from solana.rpc.async_api import AsyncClient
from config import RPC_URL, COMMITMENT

class SolanaAsyncClient:
    def __init__(self):
        '''
        Initialize the Solana async RPC client with the given RPC URL and commitment.
        '''
        self.client = AsyncClient(endpoint=RPC_URL, commitment=COMMITMENT)

    async def get_latest_blockhash(self):
        '''
        Async fetch the recent blockhash from the Solana cluster.
        This helps verify that the RPC connection is working            
        '''
        response = await self.client.get_latest_blockhash()
        return response.value.blockhash
    
    async def fetch_new_token_accounts(self):
        '''
        Placeholder for an async method to detect the newly created token accounts (basically the memecoins)
        Will be refined in future updates
        '''
        # TODO : Implement logic to find newly created token accounts.
        return []
    

    async def close(self):
        '''
        Close the underlying AsyncClient session.
        -> This also closes the RPC Connection
        '''
        await self.client.close()