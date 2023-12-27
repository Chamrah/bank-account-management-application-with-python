from Account import Account
from Current_account import CurrentAccount
from Savings_account import SavingsAccount

# Customer 1 of the Account
A1 = Account(1234,"rayane omro",3000,"18-03-2012")
print(A1.__str__())
print("*"*50)

# Customer 1 of the current Account
CA1 = CurrentAccount(7687,"simo damir",2000,"29-12-2022",1000)
print(CA1.__str__())
print("*"*50)

# Customer 1 of the savings Account
SA1 = SavingsAccount(8947,"Kawtar chakou",2100,"07-10-2023",500)
print(SA1.__str__())

