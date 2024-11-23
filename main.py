import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator  # Example for technical analysis
import backtrader as bt
from config import *

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

#Fetch account details

try:
    account = api.get_account()
    print('Account ID', account.id)
    print('Account Status', account.status)
    print('Cash Balance', account.cash)
    print('Equity', account.equity)
except Exception as e:
    print('Error fetching account details', str(e)) 






