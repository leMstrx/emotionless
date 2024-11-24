#General Imports 
import pandas as pd
from datetime import dateime, time, timezone
from typing import List, Dict, Union

#Alpaca API Imports
from alpaca.trading.client import TradingClient


class EmotionlessRobot():

    def __init__(self, api_key: str, secret_key: str, trading_account: str = None) -> None:
        """
        Initialize the EmotionlessRobot with the given parameters.

        :param api_key: Api key for the robot.
        :param secret_key: Secret Key for the robot.
        :param trading_account: The trading account ID.
        """
        self.trading_account: str = trading_account
        self.session: TradingClient = self._create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame = None

    def _create_session(self) -> TradingClient:
        """
        Create a session with the Alpaca API.

        :return: A session with the Alpaca API.
        """
        client = TradingClient(
            api_key=self.api_key,
            secret_key=self.secret_key,
            paper=True
        )
        return client
    
    @property
    def pre_market_open(self) -> bool:
        """
        Check if the pre-market is open.

        :return: True if pre-market is open, False otherwise.
        """
        pre_market_start_time = dateime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        market_start_time = dateime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        right_now = dateime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else: 
            return False

    @property
    def post_market_open(self) -> bool:
        """
        Check if the post-market is open.

        :return: True if post-market is open, False otherwise.
        """
        post_market_end_time = dateime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = dateime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = dateime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        else: 
            return False

    @property
    def regular_market_open(self) -> bool:

        market_start_time = dateime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        market_end_time = dateime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        right_now = dateime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        else: 
            return False
        
    def create_portfolio(self):
        pass

    def create_trade(self): 
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[Dict]:
        pass

        