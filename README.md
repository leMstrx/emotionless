# Emotionless Sniping Bot

-> Python based Sniping Bot build to snipe newly & freshly created tokens on the solana blockchain while incorportaing some essential safety checks

### Basic info of the bot
- Python based
- Solana Blockchain
- Mainly based on solders and solana-py (all other requirements in requirements.txt)


### What is left to do?
- Creating own wallet
- Create Fetch_new_token_accounts method with logic to find newly created token accounts -> Difficult with rate limiting
- COMMITMENT to "confirmed" DONE
- Connecting new Keypairs
- Connection to Solana Blockchain
- Safety Checks 
- Switch from devnet to beta-mainnet
- Run Bot in a task

### ROADMAP -> "Leitfaden"
1. Enhance Log Parsing
    - InitializeMint can be used to obtain information of mint adress and **creator**
2. Filter by Token Metadata
    - Liquidity Requirements: Query the newly created token's metadata and ensure it meets minimum liquidity or supply thresholds before interacting with it.
    - Blacklists/Whitelists: Maintain a Lists of Known Scams that are incorporated at all times
3. Automate Buying Newly Minted Tokens
    - Integrate with the Solana RPC API to interact with the mint
    - Automate **Purchase** process for promising tokens:
        1. Fetch the token's associated account details
        2. Confirm liquidity checks and check if tradings pairs exists on DEX like Orca Radyium (maybe Pump.fun because the rest would already be too late)
        3. Place a buy order **ONLY IF ALL CRITERIAS ARE MET**
4. Integrate Trading Strategies
    - Initial Buy: Automatically buy a small amount of the new token as soon as it's detected (if it checks all safety procedures)
    - Risk Management: Implement Stop Loss (maybe trailing) and take profit rules to manage risk
    - Timing and Volume: Avoid buying large volumes that might affect liquidity or prices adversely
5. Performance Optimization
    - Run the bot asynchronously to handle multiple events and tokens simultaneously
    - Use a high performance Solana RPC node or service to ensure low-latency responses
6. Logging and Monitoring
    - Implement a proper logging to debug and monitor the bot's activity (maybe streamlit or excel)
    - Set up alerts for detected mints und trades
7. Security and Safety Measures
    - Use a secure wallet for interactions 
    - Implement safeguards to avoid buying scam tokens or tokens with liquidity traps

#### Daily Updates: 
[18.12.2024]
- Decision Bot will be async built from the start
- Switched to Websocket built

[20.12.2024]
- Implemented Basic Safety Checks
- Now problem with RPC Rate Limiting -> Needs to be solved
- Switched to Mainnet

[23.12.2024]
- Serious problems with rate limitting 