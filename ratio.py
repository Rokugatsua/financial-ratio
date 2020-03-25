class Ratio:
    pass


class Liquid(Ratio):
    def current(self, current_assets:int , current_liabilities:int) ->float:
        return current_assets / current_liabilities

    def quick(self, current_assets:int, current_liabilities:int , inventory:int) ->float:
        return (current_assets - inventory) / current_liabilities

class Activity(Ratio):
    def receivable_turnover(self, sales: int, account_receivale:int) ->float:
        return sales / account_receivale

    def average_collection_period(self, receivable_turnover) ->int:
        return 360 / receivable_turnover

    def total_asset_turnover(self, sales:int, total_asset:int) ->int:
        return sales / total_asset

class Solvency(Ratio):
    def debt_to_assets(self, total_liabiliites:int, total_asset:int) ->int:
        return total_liabiliites / total_asset
        
    def time_interest_earn(self, EBIT:int, interest_expense: int) ->int:
        return EBIT / interest_expense

class Profitability(Ratio):
    def gross_profit_margin(self, gross_profit:int, sales:int ) ->float:
        return gross_profit / sales

    def operation_profit_margin(self, EBIT:int, sales:int) -> float:
        return EBIT / sales

    def net_profit_margin(self, EAT:int, sales:int) -> float:
        return EAT / sales

    def return_on_assets(self, EAT:int, total_asset:int) -> float:
        return EAT / total_asset

    def return_on_equity(self, EAT:int, equity:int) -> float:
        return EAT / equity




class Evaluate:
    def __init__(self, Ratios: list):
        self.Ratios = Ratios

    def progres(self):
        pass

    def show(self):
        pass


    