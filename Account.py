class Account:
    __name = ""
    __balance = 0
    

    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance

    def printBankDetials(self):
        print("Name: ",self.__name)
        print("Balance: ",self.__balance)    
         