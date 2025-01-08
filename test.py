import asyncio
from solana.rpc.websocket_api import connect
from solders.pubkey import Pubkey # type: ignore
from solders.rpc.config import RpcTransactionLogsFilterMentions # type: ignore

TOKEN_PROGRAMM_ID = 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'

async def test_ws():
    ws = await connect(
        "wss://api.mainnet-beta.solana.com",
        ping_interval=60,
        ping_timeout=120,
    )
    token_pubkey = Pubkey.from_string(TOKEN_PROGRAMM_ID)
    filter_ = RpcTransactionLogsFilterMentions(token_pubkey)
    sub_id = await ws.logs_subscribe(filter_)
    print(f"Subscribed with ID {sub_id}")

    async for msg_list in ws:
        print(msg_list)

if __name__ == "__main__":
    asyncio.run(test_ws())
