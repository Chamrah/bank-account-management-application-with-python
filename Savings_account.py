# Importation the class Account from file Account.py to Fetch information
from Account import Account
# Defined a class
class SavingsAccount(Account):
    def __init__(self, number, owner, pay, openingDate, interest):
        super().__init__(number, owner, pay, openingDate)
        self.__interest = interest
 
    # Method that display the information of the customer
    def __str__(self):
        return super().__str__() + "\nYour interest :" + str(self.__interest)+"DH"
    