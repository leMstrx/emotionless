#General imports
import numpy as np
import pandas as pd
from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby
from datetime import datetime, time, timezone
from typing import List, Dict, Tuple, Union

class StockFrame():

    def __init__(self, data: List[dict]) -> None:
        self._data = data
        self._frame = pd.DataFrame = self.create_frame()
        self._symbol_groups: DataFrameGroupBy = None
        self._symbol_rolling_groups: RollingGroupby = None

    @property
    def frame(self) -> pd.DataFrame:
        return self._frame
    
    @property
    def symbol_groups(self) -> DataFrameGroupBy:
        """
        Create a group for each symbol in the data.
        """
        self._symbol_groups = self._frame.groupby(
            by='symbol', # This is the column that we want to group by
            as_index=False, # This is to make sure that the symbol is not the index of the group
            sort=True # This is to sort the groups by the symbol
        )

        return self._symbol_groups
    
    def symbol_rolling_groups(self, size: int) -> RollingGroupby:
        """
        Create a rolling window for the symbol groups.
        """
        if not self._symbol_groups:
            self.symbol_groups

        self._symbol_rolling_groups = self._symbol_groups.rolling(size)

        return self._symbol_rolling_groups
    
    def create_frame(self) -> pd.DataFrame:
        """
        Create a dataframe from the data.
        """
        # Create the dataframe
        price_df = pd.DataFrame(data=self._data)
        price_df = self._parse_datetime_colum(price_df=price_df)
        price_df = self._set_multi_index(price_df=price_df)

        return price_df
    
    def  _parse_datetime_colum(self, price_df: pd.DataFrame) -> pd.DataFrane:
        """
        Parse the datetime column.
        """
        price_df['datetime'] = pd.to_datetime(price_df['datetime'], unit='ms', origin='unix')

        return price_df
    
    def _set_multi_index(self, price_df: pd.DataFrame) -> pd.DataFrame:
        """
        Set the multi-index for the dataframe.
        """
        price_df = price_df.set_index(keys=['symbol', 'datetime'])

        return price_df
    
    def add_rows(self, data: dict) -> None:
        column_names = ['open', 'close', 'high', 'low', 'volume']

        for symbol in data:
            #Parse this timestamp
            time_stamp = pd.to_datetime(data[symbol]['quoteTimeinLong'], unit='ms', origin='unix')

            # Define our index
            row_id = (symbol, time_stamp)

            #Define our Values
            row_values = [
                data[symbol]['openPrice'],
                data[symbol]['closePrice'],
                data[symbol]['highPrice'],
                data[symbol]['lowPrice'],
                data[symbol]['askSize'] + data[symbol]['bidSize']
            ]

            # Create a new row in the dataframe
            new_row = pd.Series(data=row_values, index=column_names)

            # Add the row to the dataframe
            self.frame.loc[row_id, column_names] = new_row.values
            self.frame.sort_index(inplace=True)

    def do_indicators_exist(self, column_names: List[str]) -> bool:
        """
        Check if the indicators exist in the dataframe.
        """
        # Check if the columns exist in the dataframe
        pass

    def _check_signals(self, indicators: Dict) -> Union[pd.Series, None]:
        """
        Check if the indicators exist in the dataframe.
        """
        # Check if the indicators exist in the dataframe
        pass
