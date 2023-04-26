#!/usr/bin/env python
# coding: utf-8

# ## Import module

# In[2]:


#for dataset
from dataset_module import FileOperator
data = FileOperator().read_transactions()

#for distance
from distance_module import DistanceModule

#for statistics

from statistic_module import TransactionStatistics
from statistic_module import Frequency
from statistic_module import Percentile


# In[3]:


TransactionStatistics(data, 21).getAvg()


# In[4]:


data[21][500000]


# ## function for Statistics Menu

# In[ ]:


# function for Statistics

def menuStatistic():
    
    print("---------------------------------Statistics------------------------------------")
    print()
          
    print("\n Please select a statistical operation to perform by number :\n")

    print("1 : Average transactions of any user   ")
    print("2 : Average transactions of all user   ")
    print("3 : Mode of transactions of any user   ")
    print("4 : Mode of transactions of all user   ")
    print("5 : Median of all transactions of any user   ")
    print("6 : Median of all transactions of all user   ")
    print("7 : Interquartile range of any user’s transactions   ")
    print("8 : Interquartile range of all user’s transactions   ")
    print("9 : location centroid of any user, based on their transaction locations  ")
    print("10 : Standard deviation of any specific user’s transactions   ")
    print("11 : Determines whether a transaction is fraudulent or not. It should provide details of such transactions  ")
    print("12 : Abnormal transaction for any given user   ")
    print("13 : Z score of any user’s transactions   ")
    print("14 : Z score for all user’s transactions   ")
    print("15 : Z score for any particular user’s transaction   ")
    print("16 : Frequencies of transactions at any given location   ")
    print("17 : nth percentiles of transactions of any user   ")
    print("18 : nth percentiles of transactions of all users   ")
    print("19 : outlier of any location and of any user")
    print("20 : outlier of all user's transaction")

    try:
        option = int(input ("\n      >> ")) 
    except ValueError:
        print("\nInvalid option. Please enter a number.")
        
#Average transactions of any user 
    if option == 1:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getAvg()
            
            print(f"Average transactions for user {userId} : {result}" )
            
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#Average transactions of all user            
    elif option == 2:
        result = TransactionStatistics(data).getAvg()
        print(f"Average transactions for all user: {result}" )

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#Mode of transactions of any user            
    elif option == 3:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getMode()
            print(f"Mode of transactions for user {userId} : {result}" )
            
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Mode of transactions of all user            
    elif option == 4:
        result = TransactionStatistics(data).getMode()
        print(f"Mode of transactions for all user : {result}" )

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
            
#Median of all transactions of any user
    elif option == 5:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getMedian()
            print(f"Median of transactions for user {userId} : {result}" )            
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)    
        
#Median of all transactions of all user   ")            
    elif option == 6:
        result = TransactionStatistics(data).getMedian()
        print(f"Median of transactions for all user : {result}" )

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#Interquartile range of any user’s transactions         
    elif option == 7:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getInterquartile()
            print(f"Interquartile of transactions for user {userId} :" )
            print(result)
                       
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Interquartile range of all user’s transactions             
    elif option == 8:
        result = TransactionStatistics(data).getInterquartile()
        print("Interquartile of transactions for all user :" )
        print(result)

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#location centroid of any user, based on their transaction locations 
    elif option == 9:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getCentroid()
            print(f"Location centroid of user {userId} : {result}" )
            
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Standard deviation of any specific user’s transactions    
    elif option == 10:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getStd()
            print(f"Standard deviation of user {userId} : {result}" )            
        except ValueError:
            print("\n Please enter a number.")
            
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#transaction is fraudulent or not.
    elif option == 11:
        try:
            userId = int(input("Enter User ID: >> "))
            transactionId = int(input("Enter Transaction ID: >> "))
            result = TransactionStatistics(data, userId, transactionId).isFraud()
            
            print("\n ------ Transaction Detail ------")
            print(f"User ID: {userId}")
            print(f"Transaction ID: {transactionId}")
            print(f"Description: {result['description']}")
            print(f"Amount: {result['amount']}")
            print(f"X cordinate: {result['xCoordinate']}")
            print(f"Y cordinate: {result['yCoordinate']}")
            
        except ValueError:
            print("\n Please enter a number.")
            
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Abnormal transaction for any given user
    elif option == 12:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getAbnormal()
            print(f"Abnormal Transaction of user {userId} :" )
            print(*result, sep=", ")
            
            # call function for further menu options. parse current menu and previous menu
            LastMenu(menuStatistic, main)
           
        except ValueError:
            print("\n Please enter a number.")            

#Z score of any user’s transactions   
    elif option == 13:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data, userId).getZscore()
            print(f"Z Score of user {userId} :" )  
            print(*result, sep=", ")
            
        except ValueError:
            print("\n Please enter a number.") 
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Z score for all user’s transactions 
    elif option == 14:
        result = TransactionStatistics(data).getZscore()
        print(f"Z Score of transaction for all user :{result} " )
        print(*result, sep=", ")

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#Z score for any particular user’s transaction
    elif option == 15:
        try:
            userId = int(input("Enter User ID: >> "))
            transactionId = int(input("Enter Transaction ID: >> "))
            result = TransactionStatistics(data, userId, transactionId).getZscore()
            
            print(f"Z Score of transaction {transactionId} for user {userId}: {result}" )
            
            
        except ValueError:
            print("\n Please enter a number.") 
            
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#Frequencies of transactions at any given location
    elif option == 16:
        try:
            xCord = int(input("Enter x Coordinate: >> "))
            yCord = int(input("Enter y Coordinate: >> "))
            result = Frequency(data, xCord, yCord).getFreq()
            print(f"Frequencies of transactions in location ({xCord},{yCord}) : {result}" )           
        except ValueError:
            print("\n Please enter a number.") 
            
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#nth percentiles of transactions of any user 
    elif option == 17:
        try:
            userId = int(input("Enter User ID: >> "))
            n = int(input("Enter User nth Percentile of a particular amount to retrieve: >> "))
            result = Percentile(n, data,userId).getPercentile()
            
            print(f"{n}th Percentile of user {userId} transaction is : {result}" )
           
        except ValueError:
            print("\n Please enter a number.") 

        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
# nth percentiles of transactions of all users 
    elif option == 18:
        try:
            n = int(input("Enter User nth Percentile of a particular amount to retrieve: >> "))
            result = Percentile(n, data).getPercentile()
            
            print(f"{n}th Percentile of all user transaction is : {result}" )           
        except ValueError:
            print("\n Please enter a number.") 
            
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
        
#outlier of any location and of any user
    elif option == 19:
        try:
            userId = int(input("Enter User ID: >> "))
            result = TransactionStatistics(data,userId).getOutlier() 
            print(f"Outlier of location for user {userId} :" )
            print(*result, sep=", ")
            
        except ValueError:
            print("\n Please enter a number.")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)

#outlier of any user
    elif option == 20:
        result = result = TransactionStatistics(data).getOutlier() 
        print(f"Outlier of location for all user : " )
        print(*result, sep=", ")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuStatistic, main)
    
    else: 
        print("\nYou entered an invalid option, Try Again")
        LastMenu(menuStatistic, main)
        
        # call function for further menu options. parse current menu and previous menu
        


# ## function for Distance Menu

# In[ ]:


# function for Distance between Transactions

def menuDistance():

    print("---------------------------------Distance between Transactions----------------------------------------------------")
    print()
    
    print("Enter 1 for Distance between Transaction of the same user ")
    print("Enter 2 for Distance between Transaction of Two user ")
    
    try:
        option = int(input ("      >> "))        
    except ValueError:
        print("Enter a integer numerical value")
        
    # code segment for Transaction between the same users
    if option == 1:
        
        userId = int(input("Enter User ID:          >> "))
        
        # checks if user exist
        if userId in data:
            transactionId_1 = int(input("Enter first Transaction ID: >> "))
            transactionId_2 = int(input("Enter second Transaction ID: >> "))
                        
            distance1 = DistanceModule(data).getDistance(userId,transactionId_1, transactionId_2)
            print(f"\nThe distance between transaction {transactionId_1} and transaction {transactionId_2} of user ID {userId}")
            print(f"\n: {distance1}")
            # call function for further menu options. parse current menu and previous menu
            LastMenu(menuDistance, main)
            
        else: print(f"\nuser ID {userId} does not exist ")
        # call function for further menu options. parse current menu and previous menu
        LastMenu(menuDistance, main)

            
    elif option == 2:
        
            userId_1 = int(input("Enter User ID for User 1 : >> "))
            userId_2 = int(input("Enter User ID for User 2: >> "))
            
            if userId_1 in data and userId_2 in data :
                
                transactionId_1 = int(input("Enter Transaction ID for user 1 : >> "))     
                transactionId_2 = int(input("Enter Transaction ID for user 2 : >> ")) 
              
            #compute the distance between 2 different users            
                distance2= DistanceModule(data).getDistance_TwoUser(userId_1, userId_2, transactionId_1, transactionId_2 )
                
                print(f"\nThe distance between transaction {transactionId_1} of user ID {userId_1} and transaction {transactionId_2} of user ID {userId_2} ")
                print(f"\n: {distance2}")
                
                # call function for further menu options. parse current menu and previous menu
                LastMenu(menuDistance, main)
                
            else:
                print("\n One or both of the user IDs does not exist")
                # call function for further menu options. parse current menu and previous menu
                LastMenu(menuDistance, main)
            
    else: 
        print("\nYou entered an invalid option, Try Again")
        LastMenu(menuDistance, main)

        # call function for further menu options. parse current menu and previous menu
            

    


# ## function for Transaction Menu

# In[ ]:


# function for menuTransaction = Transaction detail check

def menuTransaction():
    
    print("---------------------------------Transaction detail check--------------------------------------------------------")
    print() 
    try:  
        userId = int(input("Enter User ID:          >> "))
        # checks if userId exist 
        if userId in data:
            transactionId = int(input("Enter Transaction ID:   >> "))
            # checks if transaction ID exist in User Transaction
            if transactionId in data[userId]:
                
                transaction = data[userId][transactionId]
                print("\n ------ Transaction Detail ------")
                print(f"\nUser ID: {userId}")
                print(f"Transaction ID: {transactionId}")
                print(f"Description: {transaction['description']}")
                print(f"Amount: {transaction['amount']}")
                print(f"X cordinate: {transaction['xCoordinate']}")
                print(f"Y cordinate: {transaction['yCoordinate']}")
                print(f"Fraudulent: {transaction['fraud']}")
                
                # call function for further menu options. parse current menu and previous menu
                LastMenu(menuTransaction, main)

            else: 
                print(f"\nTransaction ID {transactionId} does not exist for user ID {userId} ")
                LastMenu(menuTransaction, main)
                # call function for further menu options. parse current menu and previous menu
                

        else: 
            print(f"\nUser ID {userId} does not exist")
            LastMenu(menuTransaction, main)
                          
    except KeyError:
        print("Please enter a valid User ID")
        LastMenu(menuTransaction, main)
    except ValueError:
        print("Enter a integer numerical value")
        LastMenu(menuTransaction, main)
    except UnboundLocalError:
        print("Error occured")
        LastMenu(menuTransaction, main)



# ## function for Other Menu Options

# In[ ]:


# function for Other Menu Options

def LastMenu(me, previous):
    # Last Menu   
    print("\n>> Press 5 to try again, 6 to go to Main Menu, press 7 to Exit")
    option = input(" >> ")
    if option == "5":
        me()
    elif option == "6":
        previous()
    elif option == "7":
        exit()
        print("  ---------------------------------  Bye !   --------------------------------------------------------")
        
    else: print("You entered an invalid option")


# In[ ]:





# ## Main function

# In[10]:


# Main function

def main():

    print()
    print()
    print("---------------------------------Fraud detention system-----------------------------------------")
    print()
    print("    Enter corresponding value for Action                  ")
    print()
    print("    1 : To retrieve User transaction       2: To calculate distance        3: For statistics      ")
    print("    7 : To Exit     ")
    print("")
    
    menu = input ("      >> ")
    print()
    print()
    if menu == "1":
        menuTransaction()
    elif menu == "2":
        menuDistance()
    elif menu == "3":
        menuStatistic()
    elif menu == "4":
        print("---------------------------------  Bye !   --------------------------------------------------------")
        exit()

    else: print("Invalid choice. Please enter a http://localhost:8888/notebooks/OneDrive%20-%20Sheffield%20Hallam%20University/Program%20Practice/Ass%201/seye/test_module_.ipynb#number from 1 to 4.")
        


# In[ ]:


main()


# In[ ]:




