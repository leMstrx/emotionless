'''
Used to actually start the bot with the solanaClient
'''

import asyncio
from solana_client import SolanaAsyncClient
from solana_ws_client import SolanaWSClient

async def main():
    #Initialization of WS Client
    ws_client = SolanaWSClient()
    try:
        await ws_client.listen_for_new_mints_forever()
    except KeyboardInterrupt:  
        print("Shutting down...")
    finally:
        #Close the WS client
        await ws_client.close()

if __name__ == "__main__":
    asyncio.run(main())