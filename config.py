'''
Contains all the important URLs and other Configurations
'''
#For later if testing is over then use this: "https://api.mainnet-beta.solana.com"
RPC_URL = "https://api.devnet.solana.com"
WS_URL = "wss://api.devnet.solana.com" # Can later be change to mainnet URL: "wss://api.mainnet-beta.solana.com"

#Transaction commitment level: can be "processed", "confirmed", "finalized"
COMMITMENT = "processed" # TODO: this should later be put to confirmed

#Minimum liquidity or supply filters (just placeholders for now)
MINIMUM_LIQUIDITY = 1000 #placeholder: tokens must have at least 1000 in supply
MAX_LISTEN_DURATION = 60 #Seconds to listen for new token creation events

#You might add a logging level here for convenience
LOG_LEVEL = 'INFO'

#All SPL tokes are associated with the SPL Token Program
TOKEN_PROGRAMM_ID = 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'