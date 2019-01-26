class Account:

    def __init__(self,filepath):
        self.file_path = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amt_to_remove):
        self.balance = self.balance - amt_to_remove

    def deposit(self,amt_to_add):
        self.balance = self.balance + amt_to_add

    def commit(self):
        with open(self.file_path,'w') as file:
            file.write(str(self.balance))

# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# account.deposit(200)
# print(account.balance)
# account.commit()

class Checking(Account):

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt",10)
checking.transfer(100)
checking.commit()
print(checking.balance)
