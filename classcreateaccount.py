
class Name:
        
    __prefix = ""
    __firstName = ""
    __middleName = ""
    __lastName = ""

    def get__prefix(self):
        return self.__prefix
    
    def set__prefix(self,prefix):
        self.__prefix = prefix

    def get__firstName(self):
        return self.__firstName
    
    def set__firstName(self,firstName):
        self.__firstName = firstName

    def get__middleName(self):
        return self.__middleName
    
    def set__middleName(self,middleName):
        self.__middleName = middleName

    def get__lastName(self):
        return self.__lastName
    
    def set__lastName(self,lastName):
        self.__lastName = lastName
    


class Address:

    __area = ""
    __city = ""
    __state = ""
    __country = ""
    __zipCode = 0

    def get__area(self):
        return self.__area
    
    def set__area(self,area):
        self.__area = area

    def get__city(self):
        return self.__city
    
    def set__city(self,  city):
        self.__city = city

    def get__state(self):
        return self.__state
    
    def set__state(self,state):
        self.__state = state

    def get__country(self):
        return self.__country
    
    def set__country(self,  country):
        self.__country = country

    def get__zipCode(self):
        return self.__zipCode
    
    def set__zipCode(self, zipCode):
        self.__zipCode = zipCode



class OtherDetail(Name, Address):
    __phoneNo = 0
    __DOB = "1/1/2000"
    __maritualStatus = ""
    __occupation = ""
    __adharCardNo = 0
    __mail = ""
    __gender = ""
    __accountType = 1

    def set__phoneNo(self, phoneNo):
        self.__phoneNo = phoneNo
    def get__phoneNo(self):
        return self.__phoneNo
    
    def set__DOB(self, DOB):
        self.__DOB = DOB
    def get__DOB(self):
        return self.__DOB
    
    def set__maritualStatus(self, maritualStatus):
        self.__maritualStatus = maritualStatus
    def get__maritualStatus(self):
        if (self.__maritualStatus == "Yes"): return True
        return False
    
    def set__maritualStatus(self, maritualStatus):
        self.__maritualStatus = maritualStatus
    def get__maritualStatus(self):
        return self.__maritualStatus

    def set__occupation(self, occupation):
        self.__occupation = occupation
    def get__occupation(self):
        return self.__occupation
    
    def set__adharCardNo(self, adharCardNo):
        self.__adharCardNo = adharCardNo
    def get__adharCardNo(self):
        return self.__adharCardNo
    
    def set__mail(self, mail):
        self.__mail = mail
    def get__mail(self):
        return self.__mail
    
    def set__gender(self, gender):
        self.__gender = gender
    def get__gender(self):
        return self.__gender
    
    def set__accountType(self, accountType):
        self.__accountType = accountType
    def get__accountType(self):
        return self.__accountType
