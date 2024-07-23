from classatm import Atm
from classcreateaccount import Name, Address, OtherDetail
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime

def forAtm():
    atm = Atm()

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
            

        
    # For Check Account Number Correct Or Not 
    while True:
        accountNumber =input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter your account number                                                
    |                                                                            
    ------------------------------------------------------------------------------
    """)
        
        # Check Account Number In Database
        cursor.execute(f"""SELECT count(*) FROM bank WHERE account_number = {accountNumber}
        """)
        # Store Data Of Acoount Number in "get_account_detail"
        get_account_detail = cursor.fetchone()
        # Convert into dictnory for itreate
        dict_get_account_detail = dict(get_account_detail)
        
        # If "get_account_detail['count'] > 0" means that account is available in bank 
        if(get_account_detail['count'] > 0): 

            cursor.execute(f"""SELECT * FROM bank WHERE account_number = {accountNumber}
            """)
            # Store Data Of Acoount Number in "get_access" for access balance pin or account number
            get_access = cursor.fetchone()
            # Convert into dictnory for itreate for access balance pin or account number
            dict_get_access = dict(get_access)
            
            # Set pin balance for perticular user
            atm.set__accountNumber(int(accountNumber))
            atm.set__pin(int(dict_get_access['pin']))
            atm.set__balance(int(dict_get_access['balance']))
            
            print("Your Account number is Successfully Match")
            break
        else:
            print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Plzz enter valid account number                                          
    |                                                                            
    ------------------------------------------------------------------------------
    """)
            
            
            
    # For Check Pin
    while True:
            pin = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter your pin                                                           
    |                                                                             
    ------------------------------------------------------------------------------
    """)
            # Check Pin number correct or not
            if(int(pin) == atm.get__pin()): 
                print("Your pin is successfully match")
                break
            else:
                print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Plzz enter valid pin                                          
    |                                                                             
    ------------------------------------------------------------------------------
    """)



    # After Correction of Account number and pin open atm and do some operation
    choice = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   1. Deposite                                                              
    |   2. Pin Change                                                            
    |   3. Withdrawal                                                             
    |   4. Balance Check                                                         
    |                                                                            
    ------------------------------------------------------------------------------
    """)

    # Deposite
    if(choice == '1'):
        amount = input("""
    ------------------------------------------------------------------------------
    |                                                                           
    |   Enter Amount for credite                                                 
    |                                                                            
    ------------------------------------------------------------------------------
    """)
        # add amount in his actual
        atm.set__balance(int(dict_get_access['balance'])+int(amount))
        
        #update in database
        cursor.execute(f"""UPDATE bank SET balance = {atm.get__balance()} WHERE account_number = {accountNumber}
        """)
        conn.commit()
        
        print("Credites Successfully")
       
    
    # Pin change 
    elif(choice == '2'):
        pin = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter new pin                                                            
    |                                                                            
    ------------------------------------------------------------------------------
    """)
        atm.set__pin(pin)
        
        # updated pin set in database 
        cursor.execute(f"""UPDATE bank SET pin = {atm.get__pin()} WHERE account_number = {accountNumber}
        """)
        conn.commit()
        
        print("Completely change pin")
        
    # withdrawal money
    elif(choice == '3'):
        while True:
            amount = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter Amount for debited                                                
    |                                                                           
    ------------------------------------------------------------------------------
    """)
            # Check Debited Amount is Less than actual balance or note
            if(int(amount) <= dict_get_access['balance']):
                atm.set__balance(dict_get_access['balance']-int(amount))
                
                # update balance after debited
                cursor.execute(f"""UPDATE bank SET balance = {atm.get__balance()} WHERE account_number = {accountNumber}
        """)
                conn.commit()
                
                print("Debited Sucessfully")
                break
            else:
                print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Your Balance is Less Then Your Required Amount
    |                                                                             
    ------------------------------------------------------------------------------
    """)
                
    # Check His Balance          
    elif(choice == '4'): 
        print("""Your Balance is : """, int(dict_get_access['balance']))
        
    # user enter wrong number for in atm
    else:
        print("Enter the valid number")
        
        
    
