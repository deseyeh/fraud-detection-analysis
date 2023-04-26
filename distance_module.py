#!/usr/bin/env python
# coding: utf-8

# ## A function that computes the distance between any two given transactions of a user

# In[95]:


class DistanceModule:
    
    def __init__(self, data):
        self.__data = data
    
    #implement encapsulation with get and set 
    def getData(self):
        return self.__data

        
#function to compute distance between 2 transaction of 1 user

    def getDistance(self, userId, transactionId_1, transactionId_2):
        
        # get user's transaction or empty dictionary if user does not exist
        if userId in self.__data:
            transaction = self.__data[userId]
            try:
                 # get the x and y cordinate of each transaction
                x1, y1 = transaction[transactionId_1]["xCoordinate"], transaction[transactionId_1]["yCoordinate"]
                x2, y2 = transaction[transactionId_2]["xCoordinate"], transaction[transactionId_2]["yCoordinate"]

                # using Euclidean distance metrics
                distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

                # return distance between the 2 transcations
                return round(distance, 1)

            #exception handling for wrong Key
            except KeyError:            
                if transactionId_1 not in transaction and transactionId_2 not in transaction:
                    return f"TransactionID {transactionId_1} and {transactionId_2} does not exist for user ID {userId}"
                elif transactionId_2 not in transaction or transactionId_1 not in transaction:
                    return f"Either TransactionID {transactionId_2} or {transactionId_1} does not exist for user ID {userId}"
        
        else: 
            return None

#function to compute distance between 2 transaction of 1 user

    def getDistance_TwoUser(self, userId_1, userId_2, transactionId_1, transactionId_2):
        # get user's transaction or empty dictionary if user does not exist
        
        if userId_1 in self.__data and userId_2 in self.__data:
            User1 = self.__data[userId_1]  
            User2 = self.__data[userId_2]

            # get the x and y cordinate of each transaction
            try:
                xCoordinate_1, yCoordinate_1 = User1[transactionId_1]["xCoordinate"], User1[transactionId_1]["yCoordinate"]
                xCoordinate_2, yCoordinate_2 = User2[transactionId_2]["xCoordinate"], User2[transactionId_2]["yCoordinate"]
                distance = ((xCoordinate_2 - xCoordinate_1)**2 + (yCoordinate_2 - yCoordinate_1)**2)**0.5
                return round(distance, 1)

            #exception handling for wrong Key
            except KeyError:
                if transactionId_1 not in User1:
                    return f"TransactionID {transactionId_1} does not exist for userID {userId_1}"
                elif transactionId_2 not in User2:
                    return f"TransactionID {transactionId_2} does not exist for userID {userId_2}"
        else:
            return None


# In[ ]:





# In[ ]:





# In[ ]:




