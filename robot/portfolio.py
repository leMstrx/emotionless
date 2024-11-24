#General Imports
from typing import List, Dict, Union, Tuple

class Portfolio():

    def __init__(self, account_number: str = None):
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        self.account_number = account_number

    def add_position(self, symbol: str, asset_type: str, quantity: int = 0, purchase_price: float = 0.0, purchase_date: str = None) -> dict:
        """
        Add a position to the portfolio.
        """
        self.positions[symbol] = {}

        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type
        
        return self.positions

    def add_positions(self, positions: List[dict]) -> dict:
        """
        Add multiple positions to the portfolio.
        """
        if isinstance(positions, List):
            for position in positions:
                self.add_position(
                    symbol=position['symbol'],
                    asset_type=position['asset_type'],
                    quantity=position.get('quantity', 0),
                    purchase_price=position.get('purchase_price', 0.0),
                    purchase_date=position.get('purchase_date', None)
                )
            return self.positions
        else:
            raise TypeError("Positions must be a list of dictionaries")
        
    def remove_position(self, symbol: str) -> Tuple[bool, str]:
        if symbol in self.positions:
            del self.positions[symbol]
            return True, f"{symbol} was successfully removed."
        else:
            return False, f"{symbol} was not found in the portfolio."
        

    def in_portfolio(self, symbol: str) -> bool:
        """
        Check if a symbol is in the portfolio.
        """
        if symbol in self.positions:
            return True
        else:
            return False
        
    def is_profitable(self, symbol: str, current_price: float) -> bool:
        """
        Check if a position is profitable.
        """
        purchase_price = self.positions[symbol]['purchase_price']

        if purchase_price <= current_price:
            return True
        elif purchase_price > current_price:
            return False
            
    def total_allocation(self):
        pass

    def risk_exposure(self):
        pass
    
    def total_market_value(self):
        pass
