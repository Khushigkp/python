# Create a class BankAccount with:
#   - Private attribute: __balance
#   - Methods:
#      - deposit(amount) to add money
#      - withdraw(amount) to subtract money
#      - get_balance() to view current balance
#   Let the user deposit ₹1000 and withdraw ₹500.
# Print the final balance.
class BankAccount:
    def __init__(self,balance=0):
       self.__balance= balance
    def deposit( self,amount):
      self.__balance += amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -= amount
        else :
          print("insufficient amount")
    def get_balance(self):
       return self.__balance
b=BankAccount()
(b.deposit(1000))
(b.withdraw(500))
print(b.get_balance())
