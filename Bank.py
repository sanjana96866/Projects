class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} dollars. New balance: {self.balance} dollars.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} dollars. New balance: {self.balance} dollars.")

    def check_balance(self):
        print(f"Current balance: {self.balance} dollars.")
      
def main():
    accounts = {}
    while True:
        print("\nWelcome to the Python Bank")
        print("1. Create Account")
        print("2. Log in")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = BankAccount(name)
                print("Account created successfully.")
        
        elif choice == "2":
            name = input("Enter your name: ")
            if name in accounts:
                account = accounts[name]
                print(f"Welcome back, {name}!")
                
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    
                    option = input("Enter your option: ")
                    
                    if option == "1":
                        account.check_balance()
                    elif option == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == "3":
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == "4":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Account not found. Please create an account first.")
        
        elif choice == "3":
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the banking application
if __name__== "__main__":
    main()
