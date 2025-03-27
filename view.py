from controller import controller
import pandas as pd
import matplotlib.pyplot as plt


class view:
    def __init__(self):
        self.controller = controller(input("Enter your risk level (low/medium/high): "))

    def menu(self):
        print("\033[1;34m========== MENU ==========\033[0m")
        print("\033[1;32m1. Buy\033[0m")
        print("\033[1;31m2. Sell\033[0m")
        print("\033[1;33m3. Get Advice\033[0m")
        print("\033[1;36m4. Show Portfolio\033[0m")
        print("\033[1;35m5. Exit\033[0m")
        print("\033[1;34m==========================\033[0m")
        choice = input("Enter your choice: ")
        return choice
    
    
    
    def show_menu(self):
        

        choice = self.menu()
        while choice != "5":  # exit the menu if the user types 5

            if choice == "1":  # buy (database)
                print("\033[1;32mWould you like to buy stocks or bonds?\033[0m")
                buy_choice = input("Enter your choice (stocks/bonds): ").strip().lower()
                if buy_choice == "stocks":
                    self.controller.buy_stocks(input("Enter the stock name: "), float(input("Enter the number of shares to buy: "))
                    )
                elif buy_choice == "bonds":
                    self.controller.buy_bonds(input("Enter the bond name: "), float(input("Enter the number of shares to buy: "))
                    )
                else:
                    print("\033[1;31mInvalid choice\033[0m")

            elif choice == "2":  # sell (database)
                print("\033[1;31mWould you like to sell stocks or bonds?\033[0m")
                sell_choice = input("Enter your choice (stocks/bonds): ").strip().lower()
                if sell_choice == "stocks":
                    self.controller.sell_stocks(input("Enter the stock name: "), float(input("Enter the number of shares to sell: ")))
                elif sell_choice == "bonds":
                    self.controller.sell_bonds(input("Enter the bond name: "), float(input("Enter the number of shares to sell: ")))
                else:
                    print("\033[1;31mInvalid choice\033[0m")
                
            elif choice == "3":  # advice from ollama
                print("\033[1;33mYou chose to get advice\033[0m")
                print(self.controller.ask_question(input("Enter your question: ")))

            elif choice == "4":  # show graph/table
                print("\033[1;36mYou chose to show portfolio\033[0m")
                user_choice = input("Do you want to see it as a graph or a table? (graph/table): ").strip().lower()
                if user_choice == "graph":
                    data = self.controller.get_portfolio_data()
                    if not data:
                        print("No data available to display the graph.")
                    else:
                        try:
                            df = pd.DataFrame(data)
                            # Combine stocks and bonds into one pie chart
                            plt.figure(figsize=(10, 5))
                            df.groupby('name')['value'].sum().plot(kind='pie', autopct='%1.1f%%')
                            plt.ylabel('')
                            plt.title('Portfolio Distribution by Asset')
                            plt.show()
                        except (TypeError, KeyError) as e:
                            print(f"Error processing data: {e}")

                elif user_choice == "table":
                    data = self.controller.get_portfolio_data()
                    df = pd.DataFrame(data)
                    print(df)
                else:
                    print("\033[1;31mInvalid choice\033[0m")

            else:
                print("\033[1;31mInvalid choice\033[0m")

            choice = self.menu()
        print("\033[1;35mExiting the menu. Goodbye!\033[0m")
