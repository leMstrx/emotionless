'''
Used to actually start the bot with the solanaClient
'''

import asyncio
from solana_client import SolanaAsyncClient

async def main():
    #Create a Solana client instance
    sol_client = SolanaAsyncClient()
    #Fetch a recent blockhash
    blockhash = await sol_client.get_latest_blockhash()
    print(f"Recent Blockhash: {blockhash}")
    #Close the client
    await sol_client.close()

if __name__ == "__main__":
    asyncio.run(main())