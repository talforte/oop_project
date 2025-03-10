from controller import controller
# להוסיף צבעים ולסדר את הקוד
class view:
    def __init__(self):
        self.controller = controller()

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
        # Ask the user for their risk level
        risk_level = input("Enter the risk level for your portfolio (low-medium-high): ")
        print(f"You have chosen a {risk_level} risk level for your portfolio.")

        # Display the menu
        choice = self.menu()
        while choice != "5":  # exit if the user chooses 5

            if choice == "1":  # buy database
                print("\033[1;32mYou chose to buy\033[0m")

            elif choice == "2":  # sell database
                print("\033[1;31mYou chose to sell\033[0m")

            elif choice == "3":  # advice from ollama
                print("\033[1;33mYou chose to get advice\033[0m")
                print(self.controller.ask_question(input("Enter your question: ")))

            elif choice == "4":  # show graph/table
                print("\033[1;36mYou chose to show portfolio\033[0m")
                user_choice = input("Do you want to see it as a graph or a table? (graph/table): ").strip().lower()
                if user_choice == "graph":
                    self.controller.show_portfolio_graph()
                elif user_choice == "table":
                    print(self.controller.show_portfolio_table())
                else:
                    print("\033[1;31mInvalid choice\033[0m")

            else:
                print("\033[1;31mInvalid choice\033[0m")

            choice = self.menu()
        print("\033[1;35mExiting the menu. Goodbye!\033[0m")
view().show_menu()