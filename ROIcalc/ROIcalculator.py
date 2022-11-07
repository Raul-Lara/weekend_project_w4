class my_calculator():
    def __init__(self):

        self.cash_ = 0
        self.expenses_ = []
        self.gain = []
        self.income_ = {}
        self.expensesdict = {}
            
    def income(self):
        print(f"Current income(s) : {self.gain}")
        icome_key = input("Enter income name : ")
        income_value = float(input(f"What is the value of {icome_key}?"))
        self.income_[icome_key] = income_value 
        self.cash_ += income_value
        self.gain.append(icome_key)  
        print(self.gain)
        print(f"Cashflow: {self.cash_}")
        m_income = input("Would you like to add another source of income? (y/n) : ")
        if m_income.lower() == "y":
            self.income() 
        elif m_income.lower() == "n":
            pass
        else:
            print("Invalid input, please try again")

    def expenses(self):
        print("- - - - - Current Expenses - - - - - ")
        print(self.expenses_)
        expence_input = input("Enter the expense as a string : ")
        self.expenses_.append(expence_input)
        expense_num = float(input(f"What is the cost of {expence_input}?"))
        self.expensesdict[expence_input] = expense_num 
        self.cash_ -= expense_num
        print(self.expensesdict)
        print(f"Cashflow: {self.cash_}")
        m_expen = input("Would you like to add another expense? (y/n) : ")
        if m_expen.lower() == "y":
            self.expenses() 
        elif m_expen.lower() == "n":
            pass
        else:
            print("Invalid input, please try again!")


    def cashFlow(self):
        print(f"Your incomes are: {self.income_}.") 
        print(f"Your expenses are: {self.expensesdict}.")
        print(f"Your cash flow is {self.cash_}.")

    def roi(self):
        investment = float(input("Please enter your initial investment : "))
        user_result = float(float(self.cash_) / investment)
        user_result * 100.0
        print(f"Your return on investment is {user_result}%.")
    

    def roi(self):
        investment = float(input("Please enter your initial annual investment : "))
        user_result = float(float((self.cash_)*12) / investment)
        user_result * 100.0
        print(f"Your ROI is {user_result}%.")

class Main():
    def Directions():
        print("""
Welcome to Raul's calculator
Options:
(1) Insert income source
(2) Insert Expenses
(3) Show Cash Flow
(4) Calculate ROI
(5) Quit

        """)
    def run():
        Main.Directions()
        self = my_calculator()
        while True:
            choice = input("Please select one of the items above:\n")
            if choice == "1":
                self.income()
            elif choice == "2":
                self.expenses()    
            elif choice == "3":
                self.cashFlow()
            elif choice == "4":
                self.roi()
            elif choice == "5":
                print("Thanks for using this calculator! have an awsome day!")
                break
            

Main.run()


