import asyncio
from typing import Dict, Any

async def general_safety_check(rpc_client, mint_info: dict) -> bool: 
    '''
    Perform general safety checks on a newly minted token. 
    '''
    issues = []

    #Check Freeze Authority
    # -> If the freeze authority is not set, the token can be frozen by the owner and the holders can't sell
    if mint_info['freeze_authority'] is not None:
        issues.append("Freeze authority set. The token can be frozen by the owner.")

    #Check Mint Authority
    # -> If the mint authority is not set, the token supply can't be increased by the owner
    if mint_info['creator'] is None:
        issues.append("No mint authority set. The token supply can't be increased by the owner.")
    '''
    # Check Top Holder % 
    # -> If the top holder holds a suspicious amount of supply, it's a potential rug pull
    top_holder_data = await get_top_holder_info(rpc_client, mint_info['mint_address'])
    if top_holder_data:
        if top_holder_data['']
    '''

    #Check Dev Wallet History
    # TODO

    #Check for Honeypot 
    # TODO

    # Check for Liquidity 
    # TODO

    #Summarize issues
    if issues:
        print(f"Potential risks found for mint {mint_info['mint_address']}:")
        for issue in issues: 
            print(f" - {issue}")
        return False # Token fails the checks
    else: 
        print(f"Mint {mint_info['mint_address']} passed all safety checks.")
        return True # Token passes the checks
    

async def get_top_holder_info(rpc_client, mint_address: str) -> Dict[str, Any]:
    '''
    Get information about the top holders of the token and distribution.
    :param mint_address: The mint address of the token
    :param rpc_client: The RPC client to use for fetching the data
    :return: A dictionary containing the top holders and their balances
    '''
    response = await rpc_client.get_token_accounts_by_owner(mint_address)
    return None


    accounts = await rpc_client.get_token_accounts_by_owner(mint_address)
    top_holders = sorted(accounts, key=lambda x: x['amount'], reverse=True)[:5]
    return top_holders