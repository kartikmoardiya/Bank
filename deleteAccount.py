from classatm import Atm
from classcreateaccount import Name, Address, OtherDetail
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime

def forDelete():
    atm = Atm()

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
            
    # For Check Account 
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
            if(dict_get_account_detail['count'] > 0): 

                cursor.execute(f"""SELECT * FROM bank WHERE account_number = {accountNumber}
                """)
                get_account_detail_table = cursor.fetchone()
                dict_get_account_detail_table = dict(get_account_detail_table)
                atm.set__accountNumber(int(accountNumber))
                atm.set__pin(int(get_account_detail_table['pin']))
                atm.set__balance(int(get_account_detail_table['balance']))
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
            
    
    while True:
        pin = input("""
    ------------------------------------------------------------------------------
    |                                                                            
    |   Enter your pin                                                           
    |                                                                             
    ------------------------------------------------------------------------------
    """)
        if(pin.isdigit()):
            if(int(pin) == atm.get__pin()): 
                print("Your pin is successfully match")
                print("Your Account number is Successfully Delete")
                cursor.execute(f"""DELETE FROM bank WHERE account_number = {accountNumber}
    """)
                conn.commit()
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
    