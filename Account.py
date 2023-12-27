# Defined a class
class Account():
    def __init__(self, number, owner, pay, openingDate):
        self._number = number
        self._owner = owner        
        self._pay = pay
        self._openingDate = openingDate 
    
    # Method that display the information of the customer
    def __str__(self):
        return "The number of account : "+str(self._number) +"\nThe owner is (Mr/Ms) : "+ self._owner + "\nYour pay :" +str(self._pay) +"DH" + "\nOpening date of your account :" + str(self._openingDate) 

