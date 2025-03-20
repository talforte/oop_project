from ollamamodel import ollamamodel
from security import *
from dbmodel import dbmodel
from securitylist import SecurityList
from riskmodel import riskModel


class controller:
    def __init__(self,risk_level:str):
        self.ollama = ollamamodel()
        self.db = dbmodel()
        self.sl = SecurityList()
        self.cr = riskModel()
        self.risk_level = risk_level

    def ask_question(self, question):
        return self.ollama.ask_ollama(question)
    
    def buy_stocks(self,name:str,shares_to_buy:float):
        stock = self.sl.find_security(name)
        risk = self.cr.calculate_risk(stock.sector, stock.changes, stock.type) 
        if self.cr.matching_risk_level(self.risk_level,risk):
            return self.db.buy_stock(stock,shares_to_buy)
        else:
            print("The risk of this stock is not suitable for your risk level. Abort.")
            return False
        
    def sell_stocks(self,name:str,shares_to_sell:float):
        stock = self.sl.find_security(name)
        return self.db.sell_stock(stock,shares_to_sell)
    
    def buy_bonds(self,name:str,shares_to_buy:float):
        bond = self.sl.find_security(name)
        risk = self.cr.calculate_risk(bond.sector, bond.changes, bond.type)
        if self.cr.matching_risk_level(self.risk_level,risk):
            return self.db.buy_bond(bond,shares_to_buy)
        else:
            print("The risk of this stock is not suitable for your risk level. Abort.")
            return False

    
    def sell_bonds(self,name:str,shares_to_sell:float):
        bond = self.sl.find_security(name)
        self.db.sell_bond(bond,shares_to_sell)

        
    def get_portfolio_data(self):
        return self.db.get_portfolio_data()
    

