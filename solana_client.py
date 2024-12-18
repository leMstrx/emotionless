'''
Everything related to the client
This will later be called from the main.py (emotionless.py)
'''
import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey # type: ignore
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
    
    async def fetch_token_mint_accounts(self):
        '''
        Fetch all accounts owned by the token program and return those that are like mint accounts. 
        For now, it will do the follwing:
        - Fetch program accounts of the token programs
        - Filter them by the exepected data size of a mint account (82 bytes)
        - Return their public keys
        Later this will be refined to look for newly created tokens and incorporate safety procedures
        '''
        resp = await self.client.get_program_accounts(
            self.token_program_pubkey, 
            encoding='base64',
            filters=[82])

        mint_accounts = []
        if resp.value:
            for acc_info in resp.value:
                # acc_info looks like:
                # {
                #   "pubkey": "...",
                #   "account": {
                #       "data": ["base64_encoded_data", "base64"],
                #       "executable": false,
                #       "lamports": ...,
                #       "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                #       "rentEpoch": ...
                #   }
                # } 
                data_b64 = acc_info.account.data[0] #base 64 encoded data
                #Decode the base64 data
                data = base64.b64decode(data_b64)

                #Mint accounts for SPL tokens that are 82 bytes long
                # If it's exactly 82 bytes, let's assume it's a mint account
                if len(data) == 82:
                    mint_accounts.append(acc_info.pubkey)

        return mint_accounts
    

    async def close(self):
        '''
        Close the underlying AsyncClient session.
        -> This also closes the RPC Connection
        '''
        await self.client.close()