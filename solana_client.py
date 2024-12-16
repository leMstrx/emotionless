import asyncio
from httpx import AsyncClient
from config import RPC_URL

class SolanaClient:
    def __init__(self, endpoint: str = RPC_URL):
        self.endpoint = endpoint
        
    async def get_account_info(self, pubkey: str) -> dict:
        '''
        Fetch Account Info from Solana Blockchain given public key
        '''
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [pubkey, {"encoding": "jsonParsed"}]
        } 

        async with AsyncClient() as client:
            response = await client.post(self.endpoint, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get("result",{})
        
#Quick test
async def test():
    client = SolanaClient()
    info = await client.get_account_info("So11111111111111111111111111111111111111112")
    print(info)

asyncio.run(test())

if __name__ == "__main__":
    async def test():
        client = SolanaClient()
        info = await client.get_account_info("So11111111111111111111111111111111111111112")
        print(info)

    asyncio.run(test())
