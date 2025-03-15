import sqlite3
from security import *


class dbmodel:
    def __init__(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect('investment.db')
        self.c = self.conn.cursor()

        # Create the stocks table
        self.c.execute('''CREATE TABLE IF NOT EXISTS stocks
                    (name TEXT, ticker TEXT, price REAL, share REAL, dividend_yield REAL, fixed_dividend REAL)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS bonds
                    (name TEXT, price REAL, share REAL, interest_rate REAL, maturity_date TEXT, country TEXT, credit_rating TEXT)''')

    # Function to buy stocks
    def buy_stock(self, stock:Stock, shares_to_buy:float):
        # Fetch the current shares of the stock
        self.c.execute("SELECT share FROM stocks WHERE name=?", (stock.name,))
        current_share = self.c.fetchone()
        
        if current_share:
            new_share = current_share[0] + shares_to_buy
            # Update the stock with the new share value
            self.c.execute("UPDATE stocks SET share=? WHERE name=?", (new_share, stock.name))
        else:
            # Insert the stock if it doesn't exist
            self.c.execute("INSERT INTO stocks (name, ticker, price, share) VALUES (?, ?, ?, ?)",
                    (stock.name, stock.ticker, stock.value, shares_to_buy))
        self.conn.commit()

    # Function to buy bonds
    def buy_bond(self, bond:Bond, shares_to_buy:float):
        # Fetch the current shares of the bond
        self.c.execute("SELECT share FROM bonds WHERE name=?", (bond.name,))
        current_share = self.c.fetchone()
        
        if current_share:
            new_share = current_share[0] + shares_to_buy
            # Update the bond with the new share value
            self.c.execute("UPDATE bonds SET share=? WHERE name=?", (new_share, bond.name))
        else:
            # Insert the bond if it doesn't exist
            self.c.execute("INSERT INTO bonds (name, price, share, interest_rate, maturity_date, country, credit_rating) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (bond.name, bond.value, shares_to_buy, bond.interest_rate, bond.maturity_date, bond.country, bond.credit_rating))
        self.conn.commit()
    # Function to sell stocks
    def sell_stock(self, stock: Stock, shares_to_sell: float):
        # Fetch the current shares of the stock
        self.c.execute("SELECT share FROM stocks WHERE name=?", (stock.name,))
        current_share = self.c.fetchone()
        
        if current_share and current_share[0] >= shares_to_sell:
            new_share = current_share[0] - shares_to_sell
            if new_share > 0:
                # Update the stock with the new share value
                self.c.execute("UPDATE stocks SET share=? WHERE name=?", (new_share, stock.name))
            else:
                # Delete the stock if no shares are left
                self.c.execute("DELETE FROM stocks WHERE name=?", (stock.name,))
            self.conn.commit()
        else:
            print(f"You have {current_share[0]} shares and you want to sell {shares_to_sell} shares. There is not enough shares to sell. Abort.")

    # Function to sell bonds
    def sell_bond(self, bond: Bond, shares_to_sell: float):
        # Fetch the current shares of the bond
        self.c.execute("SELECT share FROM bonds WHERE name=?", (bond.name,))
        current_share = self.c.fetchone()
        
        if current_share and current_share[0] >= shares_to_sell:
            new_share = current_share[0] - shares_to_sell
            if new_share > 0:
                # Update the bond with the new share value
                self.c.execute("UPDATE bonds SET share=? WHERE name=?", (new_share, bond.name))
            else:
                # Delete the bond if no shares are left
                self.c.execute("DELETE FROM bonds WHERE name=?", (bond.name,))
            self.conn.commit()
        else:
            print(f"You have {current_share[0]} shares and you want to sell {shares_to_sell} shares. There is not enough shares to sell. Abort.")

    # Close the connection
    def close_connection(self):
        self.conn.close()
        
    def get_portfolio_data(self):
        # Fetch all the stocks
        self.c.execute("SELECT * FROM stocks")
        stocks = self.c.fetchall()
        # Fetch all the bonds
        self.c.execute("SELECT * FROM bonds")
        bonds = self.c.fetchall()
        # Combine the stocks and bonds data
        data = []
        for stock in stocks:
            data.append({
                'type': 'stock',
                'name': stock[0],
                'value': stock[2] * stock[3]
            })
        for bond in bonds:
            data.append({
                'type': 'bond',
                'name': bond[0],
                'value': bond[1] * bond[2]
            })
        return data
