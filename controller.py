from ollamamodel import ollamamodel
from security import *
from dbmodel import dbmodel
import pandas as pd
import matplotlib.pyplot as plt

class controller:
    def __init__(self):
        self.ollama = ollamamodel()
    def ask_question(self, question):
        return self.ollama.ask_ollama(question)
    def buy_stocks(self,stock:Stock,shares_to_buy:float):
        pass
    def show_portfolio_graph(self):
        db = dbmodel()
        data = db.get_portfolio_data()
        
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

    def show_portfolio_table(self):
        db = dbmodel()
        data = db.get_portfolio_data()
        # Code to display table using data
        # For example, using pandas

        df = pd.DataFrame(data)
        return df
