'''
Used to actually start the bot with the solanaClient
'''

import asyncio
from solana_client import SolanaAsyncClient
from solana_ws_client import SolanaWSClient

async def main():
    #Create a Solana client instance
    #Info: RPC Client can still be used if needed (thats why its intialized)
    sol_client = SolanaAsyncClient()
    #Fetch a recent blockhash
    blockhash = await sol_client.get_latest_blockhash()
    print(f"Recent Blockhash: {blockhash}")
    
    #Initialization of WS Client
    ws_client = SolanaWSClient()
    await ws_client.connect()
    await ws_client.subscribe_to_token_program_logs()

    # This will forever 
    '''
    TODO: in a real bot this should be ran in a task or some form
    '''
    await ws_client.listen_for_new_mints()
   
    #Close the client
    #await sol_client.close()

if __name__ == "__main__":
    asyncio.run(main())