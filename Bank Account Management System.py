#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint

class Account:
    def __init__(self, account_no, account_holder_name, balance=0):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = balance

    def show_info(self):
        print(f"Account number: {self.account_no}")
        print(f"Customer Name: {self.account_holder_name}")
        print(f"Balance: {self.balance}")

    def show_balance(self):
        print(f"Current balance is: {self.balance}")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

class SavingsAccount(Account):
    def __init__(self, account_no, account_holder_name, balance=0, interest_rate=0.5):
        super().__init__(account_no, account_holder_name, balance)
        self.interest_rate = interest_rate
        

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Amount {amount} deposited successfully.")
        self.show_balance()

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
            self.show_balance()

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest calculated: {interest}")
        self.balance += interest
        self.show_balance()

class CurrentAccount(Account):
    def __init__(self, account_no, account_holder_name, balance=0, overdraft_limit=1000):
        super().__init__(account_no, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
            self.show_balance()
        else:
            print("Insufficient funds.")


# In[3]:


# Interaction code
list_of_accounts = []

def check_account_exists(acc_no):
    for customer in list_of_accounts:
        if customer.account_no == acc_no:
            return customer
    return None

while True:
    print("1. Create account")
    print("2. Show bank details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Personal details")
    print("7. calculate interest")
    print("8. Exit")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        account_type = input("Enter account type (Savings/Current): ").capitalize()
        if account_type == "Savings":
            account = SavingsAccount(randint(100000, 999999), input("Enter your Name: "))
        elif account_type == "Current":
            account = CurrentAccount(randint(100000, 999999), input("Enter your Name: "))
        else:
            print("Invalid account type.")
            continue
        list_of_accounts.append(account)
        print("Account created successfully.")

    elif user_choice == 2:
        if not list_of_accounts:
            print("No accounts found.")
        else:
            for account in list_of_accounts:
                account.show_info()

    elif user_choice == 3:
        acc_no = int(input("Enter your account number: "))
        customer = check_account_exists(acc_no)
        if customer:
            customer.deposit()
        else:
            print("Account does not exist.")

    elif user_choice == 4:
        acc_no = int(input("Enter your account number: "))
        customer = check_account_exists(acc_no)
        if customer:
            customer.withdraw()
        else:
            print("Account does not exist.")

    elif user_choice == 5:
        from_acc_no = int(input("Enter account number from which you want to transfer: "))
        to_acc_no = int(input("Enter account number to which you want to transfer: "))
        from_acc_cus = check_account_exists(from_acc_no)
        to_acc_cus = check_account_exists(to_acc_no)
        if from_acc_cus and to_acc_cus:
            transfer_amount = int(input("Enter transfer amount: "))
            if from_acc_cus.balance < transfer_amount:
                print("Insufficient balance.")
            else:
                from_acc_cus.balance -= transfer_amount
                to_acc_cus.balance += transfer_amount
                print("Transfer successful.")
        else:
            print("One or both accounts do not exist.")

    elif user_choice == 6:
        acc_no = int(input("Enter your account number: "))
        customer = check_account_exists(acc_no)
        if customer:
            customer.show_info()
        else:
            print("Account does not exist.")
            
    elif user_choice == 7:
        acc_no = int(input("Enter your account number : "))
        customer = check_account_exists(acc_no)
        if customer:
            customer.calculate_interest()
        else:
            print("Account does not exist.")

    elif user_choice == 8:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")


# In[ ]:




