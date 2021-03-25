#defining the bank account

class Bank:
    balance = 0

    def __init__(self):
        print("Account has been created!")


    def deposit(self):
        amount = float(input("Please an enter amount to deposit: "))
        self.balance = self.balance + amount
        print("You have deposited a specific amount. Your balance is now: %f" % self.balance)



    def withdraw(self):
        amount = float(input("Please enter amount to withdraw:"))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("You have withdrawn a specific amount. Your balance is now: %f " % self.balance)
        else:
            print("You cannot withdraw any money right now.")



    def inquiry(self):
        print("Your current balance is: %f" % self.balance)


acc = Bank()
acc.deposit()
acc.withdraw()