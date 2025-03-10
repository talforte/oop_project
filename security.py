
class Security:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Stock(Security):
    def __init__(self, name, value, ticker):
        super().__init__(name, value)
        self.ticker = ticker

class RegularStock(Stock):
    def __init__(self, name, value, ticker, dividend_yield):
        super().__init__(name, value, ticker)
        self.dividend_yield = dividend_yield

class PreferredStock(Stock):
    def __init__(self, name, value, ticker, fixed_dividend):
        super().__init__(name, value, ticker)
        self.fixed_dividend = fixed_dividend

class Bond(Security):
    def __init__(self, name, value, interest_rate, maturity_date):
        super().__init__(name, value)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date

class GovernmentBond(Bond):
    def __init__(self, name, value, interest_rate, maturity_date, country):
        super().__init__(name, value, interest_rate, maturity_date)
        self.country = country

class CorporateBond(Bond):
    def __init__(self, name, value, interest_rate, maturity_date, credit_rating):
        super().__init__(name, value, interest_rate, maturity_date)
        self.credit_rating = credit_rating
