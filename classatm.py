# Atm class for set or get balance, account number and then pin
class Atm:
    __balance = 0
    __accountNumber = 0
    __pin = 0

    def set__accountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
    def get__accountNumber(self):
        return self.__accountNumber
    
    
    def set__pin(self,pin):
        self.__pin = pin 
    def get__pin(self):
        return self.__pin


    def set__balance(self,amount):
        self.__balance = amount
    def get__balance(self):
        return self.__balance