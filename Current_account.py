# Importation the class Account from file Account.py to Fetch information
from Account import Account
# Defined a class
class CurrentAccount(Account):
# AOA => Authorized overdraft amount
    def __init__(self, number, owner, pay, openingDate, AOA):
        super().__init__(number, owner, pay, openingDate)
        self.__AOA = AOA

    # Method that display the information of the customer
    def __str__(self):
        return super().__str__() + "\nYour Authorized overdraft amount :" + str(self.__AOA)+"DH"
    