from classatm import Atm
from classcreateaccount import Name, Address, OtherDetail
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime
atm = Atm()
def forShow():
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

    # Check account number or pin correct or not
    while True:
        accountNumber =input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter your account number                                                
    |                                                                            
    ------------------------------------------------------------------------------
    """)
        
        if(accountNumber.isdigit()):        
            cursor.execute(f"""SELECT count(*) FROM bank WHERE account_number = {accountNumber}
        """)
            get_account_detail = cursor.fetchone()
            dict_get_account_detail = dict(get_account_detail)
            # check account numer is in database or not if its answer is yes then go in if condition
            if(dict_get_account_detail['count'] > 0): 
                cursor.execute(f"""SELECT * FROM bank WHERE account_number = {accountNumber}
        """)
                get_account_detail_table = cursor.fetchone()
                dict_get_account_detail_table = dict(get_account_detail)
                # if account number is correct then set balance pin or account number for other use
                atm.set__accountNumber(int(accountNumber))
                atm.set__pin(int(get_account_detail_table['pin']))
                atm.set__balance(int(get_account_detail_table['balance']))
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
        
        else:
            print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Plzz enter valid account number                                          
    |                                                                            
    ------------------------------------------------------------------------------
    """)
    
    # Input pin for endtered account number and check it
    while True:
        pin = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter your pin                                                           
    |                                                                             
    ------------------------------------------------------------------------------
    """)
        
        if(pin.isdigit()):
        # check pin correct or not
            if(int(pin) == atm.get__pin()): 
                print("Your pin is successfully match")
                print("This is your account detail")
                break
            else:
                print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Plzz enter valid pin                                          
    |                                                                             
    ------------------------------------------------------------------------------
    """)

        else:
                print("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Plzz enter valid pin                                          
    |                                                                             
    ------------------------------------------------------------------------------
    """)
                
                
    # Get table and show detail about customer
    cursor.execute(f"""SELECT * FROM bank WHERE account_number = {accountNumber}
    """)
    get_account_detail_table = cursor.fetchone() 
                
    for i in get_account_detail_table:
        if(i!='pin'):
             print(f"{(str(i)).capitalize()} : {get_account_detail_table[i]}") 
        
          