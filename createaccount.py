from classcreateaccount import Name, Address, OtherDetail
from classatm import Atm
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime


while True:
    try:
        conn = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = 'Kartik123',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        # If Database Connect Successfully Then It Will Execute
        # print("Database connect sucessfully connected")
        break

    except Exception as error:
        print("Connection to database failed")
        # Database Not Connected
        # print("Error : ",error)
        time.sleep(2)
        
ca = OtherDetail()

def forCreatingAccount():
    # Check Leap Year Or not
    def checkLeapYear(n):
        year = int(n)
        
        if (year%400 == 0):
            return True
        elif (year%100 == 0):
            return False
        elif (year%4 == 0):
            return True
        else:
            return False
        

    # input of prefix
    def inputPrefix():
        while True:

            prefix = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter the prefix                                                         
        |   For Male --> "Mr"                                                        
        |   For Female --> "Mrs"                                                      
        |                                                                            
        ------------------------------------------------------------------------------
        """)
            
            # Prefix is right or wrong 
            if prefix.capitalize() == 'Mr' or prefix.capitalize() == 'Mrs':
                ca.set__prefix(prefix.capitalize())
                print("You Enter This Prefix : ",prefix.capitalize())
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Input As Per Example                               
        |                                                                           
        -----------------------------------------------------------------------------
        """)


    # inpunt Name --> lastname, middlename, firstname
    def inputName():
        # make list for optimaation and input
        nameList = ["firstName","middleName","lastName"]
        
        # itreate list
        for i in nameList:
            # copy element for get actual value
            copyName = i
            
            # This Loop is for get valid input
            while True:
                i = input(f"""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter your {copyName}                                                           
        |                                                                            
        ------------------------------------------------------------------------------
        """)
                # check Input in number or not if input is in number format. it will go in if condtion
                if i.isdigit():
                    print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Input                                              
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                else:
                    break
            
            # set name on class 
            if(copyName=="firstName"):
                ca.set__firstName(i.capitalize())
                print("Your First Name is : ",ca.get__firstName( ))
            elif(copyName=="middleName"):
                ca.set__middleName(i.capitalize())
                print("Your Middle Name is : ",ca.get__middleName( ))
            elif(copyName=="lastName"):
                ca.set__lastName(i.capitalize())
                print("Your Last Name is : ",ca.get__lastName( ))
        
        
    # Input Adress --> area, city, state, country, zipcode
    def inputAddress():

        addressList = ["area", "city", "state", "country","zipcode"]
        
        # we want to zipcode in number so "ct" is used to get index of zipcode
        ct = -1
            
        # itreate list
        for i in addressList:
            # copy element for get actual value
            copyName = i
            
            # update index using ct   
            ct = ct + 1
            
            # This Loop is for get valid input
            while True:
                
                i = input(f"""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter your {copyName}                                                           
        |                                                                            
        ------------------------------------------------------------------------------
        """)
                
                # id ct == 4 means zipcode is allow then check len of zipcode and it is  digit or not
                if len(i) == 6 and ct == 4 and i.isdigit() :
                    print(f"your {copyName} is {i}")
                    ca.set__zipCode(int(i))
                    break
                
                # if ct ==4 but user entered invalid input
                elif(ct==4):
                    print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Input                                         
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                # input some other detail acception zipcode then check it is digit or not beacuse other detail are not allow in number formT
                elif ct < 4 and i.isdigit():
                    print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Input                                       
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                else:
                    print(f"your {copyName} is {i.capitalize()}")
                    # set name on class 
                    if(copyName=="area"):
                        ca.set__area(i.capitalize())
                    elif(copyName=="city"):
                        ca.set__city(i.capitalize())
                    elif(copyName=="state"):
                        ca.set__state(i.capitalize())
                    elif(copyName=="country"):
                        ca.set__country(i.capitalize())
                    break
                    
                
                    
                
    
    
    # Input Phone Number     
    def inputPhoneNumber():
        while True:
            phoneNo = input("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Enter Your phone number                                                 
        |                                                                           
        -----------------------------------------------------------------------------
        """)
            # For check Length of phone number and check it is digit or not
            if(len(phoneNo)==10 and phoneNo.isdigit()):
                ca.set__phoneNo(int(phoneNo))
                print("Your Phone Number is : ",ca.get__phoneNo())
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Phone Number                                              
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                

    # Input date pf birth
    def inputDateOfBirth():
        while True:
            dob = input("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Enter Your Date Of Birth                                                
        |   In Form Of DD/MM/YYYY                                                   
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                
            day = dob[0:2]
            month = dob[3:5]
            year = dob[6:10]
            
            # check form of input correct or not like DD/MM/YYYY
            if(len(day) == 2) and (len(month)==2) and (len(year)==4) and (dob[2] == '/') and (dob[5]=='/') and (day.isdigit()) and (month.isdigit()) and (year.isdigit()):
                # 31 days in month
                if (month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12') and (day>='0' and day <= '31'):
                    ca.set__DOB(dob)
                    print("Your Date Of Birth is : ",ca.get__DOB())
                    break
                # 30 days in month
                elif (month == '04' or month == '06' or month == '09' or month == '11') and (day>='0' and day <= '30'):
                    ca.set__DOB(dob)
                    print("Your Date Of Birth is : ",ca.get__DOB())
                    break
                # if month is fabruary then check leap year or not if yes then execute this elif condition otherwise execute bellow condition
                elif(checkLeapYear(year) and month == '02' and day >= '01' and day <= '29'):
                    ca.set__DOB(dob)
                    print("Your Date Of Birth is : ",ca.get__DOB())
                    break
                elif(checkLeapYear(year) == False and month == '02' and day >= '01' and day < '29'):
                    ca.set__DOB(dob)
                    print("Your Date Of Birth is : ",ca.get__DOB())
                    break
                else:
                    print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Date Of Birth                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                        
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Date Of Birth                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """) 
        
        
    # input the adharCard Number            
    def inputAadharCardNumber():
        
        while True:
            adharCardNo = input("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Enter your Aadhar Card No                                               
        |                                                                           
        -----------------------------------------------------------------------------
        """)
            # check length of adhar card number
            if(len(adharCardNo)==12) and (adharCardNo.isdigit()):
                ca.set__adharCardNo(int(adharCardNo))
                print("Your Adhdhar Number is : ", ca.get__adharCardNo())
                break
            else:
                    print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Adharcard Number                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """) 
        
        
    # Check Maritual Status           
    def inputMaritualStatus():
        while True:

            maritualStatus = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter the your Maritual Status                                           
        |   For Example : "Yes"                                                      
        |               : "No"                                                       
        |                                                                            
        ------------------------------------------------------------------------------   
        """)
            if maritualStatus.capitalize() == 'Yes' or maritualStatus.capitalize() == 'No' and type(maritualStatus)==str:
                ca.set__maritualStatus(maritualStatus.capitalize())
                print("Your Maritual Status is : ",ca.get__maritualStatus( ))
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Answer                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """)
    
    
    # Input Occupation            
    def inputOccupation():
        
        while True:
            occupation = input("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Enter your occupation                                                   
        |                                                                           
        -----------------------------------------------------------------------------
        """)
            # Check input is integer or not
            if(occupation.isdigit()):
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Answer                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """)
            
            else:
                ca.set__occupation(occupation)
                print("Your Occupation is : ", ca.get__occupation())
                break
            

    # Input Gender
    def inputGender():
        while True:

            gender = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter your Gender                                                        
        |   For Example : "Male"                                                     
        |               : "Female"                                                   
        |               : "Other"                                                    
        |                                                                            
        ------------------------------------------------------------------------------    
        """)
            if gender.capitalize() == 'Male' or gender.capitalize() == 'Female' or gender.capitalize() == 'Other':
                ca.set__gender(gender.capitalize())
                print("Your Gender is : ",ca.get__gender( ))
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Gender                                             
        |                                                                           
        -----------------------------------------------------------------------------
        """)


    # input Account Type
    def inputAccountType():
        while True:

            accountType = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Choose the your Account Type                                             
        |   For : 1. Savings Account                                                 
        |       : 2. Current Account                                                 
        |                                                                            
        ------------------------------------------------------------------------------
        """)
            #Check input valid or not
            if accountType == '2' or accountType == '1':
                if(accountType=='1'):
                    ca.set__accountType("Savings Account")
                    print("Your Account Choice is : Savings Account")
                else:
                    ca.set__accountType("Current Account")
                    print("Your Account Choice is : Current Account")
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Number As Per Example                              
        |                                                                           
        -----------------------------------------------------------------------------
        """) 


    # Input Emial
    def inputEmail():
        while True:

            mail = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter the your Email Address                                             
        |   For Example : xxxxx@gmail.com                                            
        |                                                                            
        ------------------------------------------------------------------------------ 
        """)
            # Check Input is correct or not
            if type(mail) == str and mail[-10:len(mail)]=='@gmail.com':
                ca.set__mail(mail.lower())
                print("Your email address is : ",ca.get__mail( ))
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Email Address                                      
        |                                                                           
        -----------------------------------------------------------------------------
        """)  
    
    # Create atm Object for ATM class            
    atm = Atm()


    # Input pin from user
    def inputPin():
        while True:
            pin = input("""
        ------------------------------------------------------------------------------
        |                                                                            
        |   Enter 4 Digit Account Pin                                              
        |                                                                            
        ----------------------------------------------------------------------------- 
        """)
            # Check pin is correct or not
            if(len(pin)==4) and(pin.isdigit()):
                print("Your pin is successfully created")
                atm.set__pin(int(pin))
                break
            else:
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Plzz Enter The Valid Email Address                                      
        |                                                                           
        -----------------------------------------------------------------------------
        """)
                
        
    # Creat Account Number
    def randomAccountNumber():
        
        # While loop is usage for check created new aacount number has been in database or not
        while True:
            acno = randint(100000,999999)
            cursor.execute(f"""SELECT count(*) FROM bank WHERE account_number = {acno}
        """)
            get_account_detail = cursor.fetchone()
            dict_get_account_detail = dict(get_account_detail)
            
            # if kartik1['count'] is less than 0 means no similar account number in database 
            if(dict_get_account_detail['count']) <= 0:    
                atm.set__accountNumber(acno)
                print("""
        -----------------------------------------------------------------------------
        |                                                                           
        |   Congratulations                                                         
        |   Your Account Is Sccessfully Created                                     
        |   Your Account Number is %s                                               
        |                                                                           
        -----------------------------------------------------------------------------
        """%(acno))
                break
        

    def dataBase():
        while True:
            try:
                conn = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = 'Kartik123',cursor_factory=RealDictCursor)
                cursor = conn.cursor()
                # print("Database connect sucessfully connected")
                break

            except Exception as error:
                print("Connection to database failed")
                # print("Error : ",error)
                time.sleep(2)
            
        cursor.execute(f""" INSERT INTO bank (account_number,pin,balance,prefix,first_name,middle_name,last_name,area,city,state,country,zipcode,phone_number,date_of_birth,maritual_status,occuoation,aadhar_card_number,email,gender,account_type,create_at) 
        VALUES {str(atm.get__accountNumber()),str(atm.get__pin()),str(atm.get__balance()),ca.get__prefix(),ca.get__firstName(),ca.get__middleName(),ca.get__lastName(),ca.get__area(),ca.get__city(),ca.get__state(),ca.get__country(),str(ca.get__zipCode()),str(ca.get__phoneNo()),ca.get__DOB(),ca.get__maritualStatus(),ca.get__occupation(),str(ca.get__adharCardNo()),ca.get__mail(),ca.get__gender(),ca.get__accountType(),str(datetime.now())}""")
        conn.commit()
            

    # List of all input Fucntions for calling their function 
    dict_get_account_detail = [inputPrefix(),inputName(),inputGender(),inputMaritualStatus(),inputAddress(),inputDateOfBirth(),inputPhoneNumber(),inputEmail(),inputAadharCardNumber(),inputOccupation(),inputAccountType(),randomAccountNumber(),inputPin(),dataBase()]

    # # call all the function through list
    # def forCreatingAccount():
    #     # for i in dict_get_account_detail:
    #     #     i
    #     inputPrefix()
    #     inputName()
    #     inputGender()
    #     inputMaritualStatus()
    #     inputAddress()
    #     inputDateOfBirth()
    #     inputPhoneNumber()
    #     inputEmail()
    #     inputAadharCardNumber()
    #     inputOccupation()
    #     inputAccountType()
    #     randomAccountNumber()
    #     inputPin()
    #     dataBase()
        
            
            