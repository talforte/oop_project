from ollamamodel import ollamamodel
from security import *
from dbmodel import dbmodel
from securitylist import SecurityList
from riskmodel import riskModel
import pandas as pd
import matplotlib.pyplot as plt

class controller:
    def __init__(self,risk_level:str):
        self.ollama = ollamamodel()
        self.db = dbmodel()
        self.sl = SecurityList()
        self.cr = riskModel()
        self.risk_level = risk_level
    def ask_question(self, question):
        return self.ollama.ask_ollama(question)
    
    def find_security(self, name: str):
        stock_or_bond = self.sl.get_security_by_name(name)
        while stock_or_bond is None:
            print(f"No security found with name: {name}")
            name = input("Please enter a valid security name: ")
            stock_or_bond = self.sl.get_security_by_name(name)
        return stock_or_bond
    def matching_risk(self, risk_level:str,risk:float):

        if risk_level == "low" and 0.1 <= risk <= 2.5:
            return True
        elif risk_level == "medium" and 2.51 <= risk <= 4.5:
            return True
        elif risk_level == "high" and risk >= 4.51:
            return True
        else:
            return False
    
    def buy_stocks(self,name:str,shares_to_buy:float):
        stock = self.find_security(name)
        risk = self.cr.calculate_risk(stock.sector, stock.changes, stock.type) # 3
        if self.matching_risk(self.risk_level,risk):
            return self.db.buy_stock(stock,shares_to_buy)
        else:
            print("The risk of this stock is not suitable for your risk level. Abort.")
            return False
        
    def sell_stocks(self,name:str,shares_to_sell:float):
        stock = self.find_security(name)
        return self.db.sell_stock(stock,shares_to_sell)
    
    def buy_bonds(self,name:str,shares_to_buy:float):
        bond = self.find_security(name)
        risk = self.cr.calculate_risk(bond.sector, bond.changes, bond.type)
        if self.matching_risk(self.risk_level,risk):
            return self.db.buy_bond(bond,shares_to_buy)
        else:
            print("The risk of this stock is not suitable for your risk level. Abort.")
            return False

    
    def sell_bonds(self,name:str,shares_to_sell:float):
        bond = self.find_security(name)
        return self.db.sell_bond(bond,shares_to_sell)
    
    def show_portfolio_graph(self): # להזיז ל-VIEW
        data = self.db.get_portfolio_data()
        
        if not data:
            print("No data available to display the graph.")
            return

        try:
            df = pd.DataFrame(data)
        except (TypeError, KeyError) as e:
            print(f"Error processing data: {e}")
            return

        # Combine stocks and bonds into one pie chart
        plt.figure(figsize=(10, 5))
        df.groupby('name')['value'].sum().plot(kind='pie', autopct='%1.1f%%')
        plt.ylabel('')
        plt.title('Portfolio Distribution by Asset')
        plt.show()

    def show_portfolio_table(self): #להזיז ל-VIEW
        data = self.db.get_portfolio_data()
        # Code to display table using data
        # For example, using pandas

        df = pd.DataFrame(data)
        return df
    

