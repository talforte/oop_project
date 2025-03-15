
class Security:
    def __init__(self, name, value, sector, changes, type): # אתחול: שם,ערך,סקטור,שינויים,סוג
        self.name = name
        self.value = value
        self.sector = sector
        self.changes = changes
        self.type = type

class Stock(Security):
    def __init__(self, name, value, sector, changes,type, ticker):
        super().__init__(name, value, sector, changes,type) 
        self.ticker = ticker

class RegularStock(Stock):
    def __init__(self, name, value, sector, changes,type, ticker, dividend_yield):
        super().__init__(name, value, sector, changes,type, ticker)
        self.type = "Regular Stock"
        self.dividend_yield = dividend_yield

class PreferredStock(Stock):
    def __init__(self, name, value, sector, changes, ticker,type, fixed_dividend):
        super().__init__(name, value, sector, changes,type, ticker)
        self.type = "Preferred Stock"
        self.fixed_dividend = fixed_dividend

class Bond(Security):
    def __init__(self, name, value, sector, changes,type, interest_rate, maturity_date):
        super().__init__(name, value, sector, changes,type)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date

class GovernmentBond(Bond):
    def __init__(self, name, value, sector, changes,type, interest_rate, maturity_date, country):
        super().__init__(name, value, sector, changes,type, interest_rate, maturity_date)
        self.type = "Government Bond"
        self.country = country

class CorporateBond(Bond):
    def __init__(self, name, value, sector, changes,type, interest_rate, maturity_date, credit_rating):
        super().__init__(name, value, sector, changes,type, interest_rate, maturity_date)
        self.type = "Corporate Bond"
        self.credit_rating = credit_rating
