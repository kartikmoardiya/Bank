from database import engine, SessionLocal, get_db,Base
import models

models.Base.metadata.create_all(bind = engine) # For Connect DataBase With Python

# Take Input As Per User Requirment
while True:
    choice = input("""
    ------------------------------------------------------------------------------
    |                                                                            |
    |   1. CREATE ACCOUNT                                                        |
    |   2. ATM                                                                   |
    |   3. SHOW ACCOUNT DETAIL                                                   |
    |   4. DELETE ACCOUNT                                                        |
    |   5. HELP                                                                  |
    |   6. EXIT                                                                  |
    |                                                                            | 
    ------------------------------------------------------------------------------
    """)
    
    # Impoer Some Libraries For Performing Some Operation As Per User Requirment
    from createaccount import forCreatingAccount
    from deleteAccount import forDelete
    from showAccount import forShow
    from help import forHelp
    from atm import forAtm
    
    
    if(choice == '1'):
        # If User Want To Create New Account Then This Function Will Execute From "createaccount" Library
        forCreatingAccount()
        
    elif(choice == '2'):
        # If User Want Do Some Opertaion In ATM Then This Function Will Execute From "atm" Library
        forAtm()
        
    elif(choice == '3'):
        # For Show Account Details
        forShow()
        
    elif(choice == '4'):
        # Account Delete From Bank
        forDelete()
        
    elif(choice == '5'):
        # For Help
        forHelp()
        
    elif (choice == '6'):
        # For Execute From Banking System
        print("You Are Exit From Bank")
        break
    else:
        print("Enter the valid number")



























