'''
Contains all the important URLs and other Configurations
'''
#For later if testing is over then use this: "https://api.mainnet-beta.solana.com"
RPC_URL = "https://api.devnet.solana.com"

#Transaction commitment level: can be "processed", "confirmed", "finalized"
COMMITMENT = "processed"

#Minimum liquidity or supply filters (just placeholders for now)
MINIMUM_LIQUIDITY = 1000 #placeholder: tokens must have at least 1000 in supply
MAX_LISTEN_DURATION = 60 #Seconds to listen for new token creation events

#You might add a logging level here for convenience
LOG_LEVEL = 'INFO'