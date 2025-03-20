from security import RegularStock, PreferredStock, GovernmentBond, CorporateBond

class SecurityList: #רשימה המכילה 10 אג"ח ו10 מניות כלליות
    def __init__(self):
        self.securities = {
            "stocks": [
            RegularStock(name="Apple", value=50.0, sector="technology", changes="big changes", type="regular stock", ticker="AAPL", dividend_yield=5),
            PreferredStock(name="Microsoft", value=45.0, sector="technology", changes="low changes", type="preferred stock", ticker="MSFT", fixed_dividend=4),
            RegularStock(name="Amazon", value=60.0, sector="consumption", changes="big changes", type="regular stock", ticker="AMZN", dividend_yield=3),
            PreferredStock(name="Google", value=55.0, sector="technology", changes="low changes", type="preferred stock", ticker="GOOGL", fixed_dividend=2),
            RegularStock(name="Facebook", value=40.0, sector="technology", changes="low changes", type="regular stock", ticker="FB", dividend_yield=1),
            RegularStock(name="Berkshire Hathaway", value=70.0, sector="finance", changes="big changes", type="regular stock", ticker="BRK.A", dividend_yield=0),
            PreferredStock(name="Alibaba", value=35.0, sector="consumption", changes="low changes", type="preferred stock", ticker="BABA", fixed_dividend=2),
            RegularStock(name="Tencent", value=30.0, sector="technology", changes="low changes", type="regular stock", ticker="TCEHY", dividend_yield=1),
            PreferredStock(name="Tesla", value=80.0, sector="consumption", changes="big changes", type="preferred stock", ticker="TSLA", fixed_dividend=0),
            RegularStock(name="Visa", value=65.0, sector="finance", changes="big changes", type="regular stock", ticker="V", dividend_yield=3)
            ],
            "bonds": [
            GovernmentBond(name="US Treasury Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=1.5, maturity_date="2030-01-01", country="USA"),
            GovernmentBond(name="German Bund", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=0.5, maturity_date="2030-01-01", country="Germany"),
            GovernmentBond(name="UK Gilt", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=1.0, maturity_date="2030-01-01", country="UK"),
            GovernmentBond(name="Japanese Government Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=0.1, maturity_date="2030-01-01", country="Japan"),
            GovernmentBond(name="French OAT", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=0.8, maturity_date="2030-01-01", country="France"),
            GovernmentBond(name="Italian BTP", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=1.2, maturity_date="2030-01-01", country="Italy"),
            GovernmentBond(name="Canadian Government Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=1.3, maturity_date="2030-01-01", country="Canada"),
            GovernmentBond(name="Australian Government Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=1.4, maturity_date="2030-01-01", country="Australia"),
            GovernmentBond(name="Swiss Government Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=0.2, maturity_date="2030-01-01", country="Switzerland"),
            GovernmentBond(name="Chinese Government Bond", value=100.0, sector="government", changes="low changes", type="government bond", interest_rate=2.0, maturity_date="2030-01-01", country="China")
            ]
        }

    def get_security_by_name(self, name): #המשתמש מזין שם של מניה או אג"ח והפונקציה מחזירה את המניה או האג"ח
        name = name.lower()
        for security_type in self.securities.values():
            for security in security_type:
                if security.name.lower() == name:
                    return security
        return False
    def get_all_securities(self): #להחזיר את כל האג"חים ומניות ביחד
        return self.securities["stocks"] + self.securities["bonds"]
    
    def find_security(self, name: str):
        stock_or_bond = self.get_security_by_name(name)
        while stock_or_bond is False:
            print(f"No security found with name: {name}")
            name = input("Please enter a valid security name: ")
            stock_or_bond = self.get_security_by_name(name)
        return stock_or_bond
