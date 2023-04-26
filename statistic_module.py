#!/usr/bin/env python
# coding: utf-8

# ## OOP implementation
# 
# In super class StatisticModule, only data was set/get
# 
# In sub Class TransactionStatistic, it inherits the data from superclass - StatisticModule. and getAmount function. 
#         
# and it contains functions getAvg, getMode, getMedian, getInterquartile, getCentroid, getStd, isFraud, getAbnormal, getZscore, getOutlier
# 
# In sub Class Frequency and Percentile, it inherits data from superclass - StatisticModule. and getAmount function.
# contains functions - getFreq and getPercentile respectively
# 
# A Helper function - MedianHelper is first implemented to support re-use of Median computation.
# 

# ## Median Helper function

# In[151]:


# helper function for median

def medianHelper(listValue):
    
    #this first sorts the list in ascending order
    listValue.sort()
    # gets the lenght of the list
    n = len(listValue)
    
    # test if lenght is even or odd. if even, add the 2 middle numbers and divide by 2
    # if odd. median is the middle number using slicer
    
    if n % 2 == 0:
        median = (listValue[n//2 - 1] + listValue[n//2]) /2
    else:
        median = listValue[n//2]
    
    # return the median of all users
    return round(median, 2)


# ## Statistic Module Super class


class StatisticModule:
    
    def __init__(self, data):
        self.__data = data
    
    def getData(self):
        return self.__data
    
    # AMount
    def getAmount(self, user_id=None):
        user_amounts = []
        if user_id is None:
            for transaction in self.__data:
                for trans in self.__data[transaction]:
                    user_amounts.append(self.__data[transaction][trans]['amount'])
            return user_amounts
        
        elif user_id in self.__data:
            user_transactions = self.__data[user_id]
            user_amounts = [user_transactions[t]['amount'] for t in user_transactions]
            return user_amounts
        
        else:
            #print(f"user ID {user_id} does not exist")
            return None
        


# # the Transaction Statistic of any user and of all users
# 
# getAvg
# 
# getMode
# 
# getMedian
# 
# getInterquartile
# 
# getCentroid
# 
# getStd
# 
# isFraud
# 
# getAbnormal
# 
# getZscore
# 
# getOutlier

# In[154]:


class TransactionStatistics(StatisticModule):
    
    def __init__(self, data, user_id=None, transaction_id=None):
        super().__init__(data)
        self.__user_id = user_id
        self.__transaction_id = transaction_id
        
    def getUser_id(self):
        return self.__user_id
    
    def setUser_id(self, user_id):
        self.__user_id = user_id
        
    def getTransaction_id(self):
        return self.__transaction_id
    
    def setTransaction_id(self, transaction_id):
        self.__transaction_id = transaction_id
        
#Average of all transaction of any user and all user
    
    def getAvg(self):
        
        # get amounts from super class function getAmount()
        user_amount = super().getAmount(self.__user_id)
        
        if user_amount is not None:
            try:
                average = sum(user_amount) / len(user_amount)
                return round(average, 2)
            except ZeroDivisionError:
                return "\nError: Average can not be computed"
        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"
        
#Mode of all transaction of any user and all user 

    def getMode(self):
        
        #initialize mode
        mode_amount = None
        mode_count = 0
        # get amounts from super class function getAmount()
        user_amount = super().getAmount(self.__user_id)  

        #checks if there is transaction
        if user_amount is not None: 
            
            #coumpute mode
            for amount in user_amount:
                count = user_amount.count(amount)
                if count > mode_count:
                    mode_count = count
                    mode_amount = amount

            return mode_amount

        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"
        
#Median of all transaction of any user and all user

    def getMedian(self):

        user_amount = super().getAmount(self.__user_id)

        # check if user_amount is not empty
        if user_amount is not None :
            # parse user_amount to Medianhelper function to compute mmedian and return
            return medianHelper(user_amount)

        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"    

# the interquartile range of any user’s transactions and of all users

    def getInterquartile(self):

        # get amount 
        user_amount = super().getAmount(self.__user_id)

        if user_amount is not None :
            # sort amounts    
            sorted_user_amount = sorted(user_amount)

            #lenght of list
            len_amount = len(sorted_user_amount)

             # checks the list has an odd number of elements, exclude the median from the quartile calculation
            if len_amount % 2 == 1:
                lowerQ = sorted_user_amount[:len_amount//2]
                higherQ = sorted_user_amount[len_amount//2 + 1:]

            # checks the list has an even number of elements, include the median in both halves
            else:
                lowerQ = sorted_user_amount[:len_amount//2]
                higherQ = sorted_user_amount[len_amount//2:]

            # get the mean of lowerQ and HigherQ
            lowerQ_mean = medianHelper(lowerQ)
            higherQ_mean = medianHelper(higherQ)

            return (higherQ_mean - lowerQ_mean)

        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"   
        
# the location centroid of any user, based on their transaction locations

    def getCentroid(self):

        # checks if user ID exist in the data
        if self.__user_id in super().getData():  
            # gets the transaction for the specific user
            user_transactions = super().getData()[self.__user_id]

            # gets the list of x and y COrdinates 
            xCoord = [ user_transactions[t]['xCoordinate'] for t in user_transactions ]
            yCoord = [ user_transactions[t]['yCoordinate'] for t in user_transactions ]

            # computes the avergae of xCordinate and yCordinate    
            avgXcoord = round(sum(xCoord) / len(xCoord), 1)
            avgYcoord = round(sum(yCoord)/len(yCoord), 1)

            return(avgXcoord, avgYcoord)

        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"
        
# the standard deviation of any specific user’s transactions

    def getStd(self):

        # get amount and average  for all users or any particular
        user_amount = super().getAmount(self.__user_id)
        avg = self.getAvg()

        # checks if transaction exist
        if user_amount is not None :

            # compute the deviation for each amount
            deviation = [(amount - avg) ** 2 for amount in user_amount]

            # Compute the variance of the transactions
            variance = sum(deviation) / (len(user_amount) - 1)
            std_dev = round(variance ** 0.5, 2)
             # return the standard deviation of the transactions as sqrt of variance
            return std_dev
           
        else:
            return f"Error: No Transaction found for user ID {self.__user_id}"
        
# whether a transaction is fraudulent or not. It should provide details of such transactions  

    def isFraud(self):
        
        data = super().getData() 

        if self.__user_id in data and self.__transaction_id in data[self.__user_id]:
            
            transaction = data[self.__user_id][self.__transaction_id]
            a  = transaction['description']

            with open('description.txt', 'r') as fileGenuine:

                for line in fileGenuine :
                    if a in line:
                        print(f"The transaction {self.__transaction_id} is Not Fraudulent ")
                        return transaction

            with open('fraud-description.txt', 'r') as fileFraud:

                for line in fileFraud :
                    if a in line:
                        print(f"The transaction {self.__transaction_id} is Fraudulent ")
                        return transaction

        elif self.__user_id not in data:
            return f"user Id {self.__user_id} does not exist"

        elif self.__user_id in data and self.__transaction_id not in data[self.__user_id]:
            
            return f"Transaction Id {self.__transaction_id} is not in user Id {self.__user_id}"
        
        
## an abnormal transaction for any given user.

    def getAbnormal(self):

        #initialize abnormal transaction list
        abnormal_transaction = []

        if self.__user_id in super().getData():

            # get amount fot a particular user
            user_amount = super().getAmount(self.__user_id)

            # gets mean for a particular user from average function
            mean = self.getAvg()
            
            # gets Standard Deviation for a particular user from getStd function
            std = self.getStd()

            # set a criterial for value more thaan 2 Standard deviation
            crit = mean + 2 * std

            #loops through each amount to test if abnormal or not
            abnormal_transaction = [amount for amount in user_amount if amount > crit ]
           
            # return abnormal transactions        
            return abnormal_transaction

        else: return f" User ID {self.__user_id} does not exist"
        

# the Z score of any user’s transactions and for all users’ transactions.

    def getZscore(self):
        
        data = super().getData()
        
        # get amount, average and std  for all users or any particular
        
        #test if transaction ID is parsed and computes zscores for a particular transaction Id
        if self.__transaction_id is not None:
            try:
                #get the amount of that particular transaction
                user_amount = data[self.__user_id][self.__transaction_id]['amount']
                avg = self.getAvg()
                std = self.getStd()
                z = (user_amount - avg) / std
                return (round(z, 2))
            except KeyError:
                return f"Error: No Transaction found for Transaction ID {self.__transaction_id}"
                
        else:
            user_amount = super().getAmount(self.__user_id)           
            avg = self.getAvg()
            std = self.getStd()
        
        #deviation = [(amount - avg) ** 2 for amount in user_amount]
        # compute zScore 
        if user_amount is not None:
            zscore = [round((amount - avg) / std, 2) for amount in user_amount ]

            return zscore

        else:
            return f" User ID {self.__user_id} does not exist" 
        
 # Outlier 

    def getOutlier(self):
               
        # get amount fot a particular user
        user_amount = super().getAmount(self.__user_id)

        #sort the value in asceding order
        user_amount.sort()

        #lenght of amount
        n = len(user_amount)

        # If the list has an odd number of elements, exclude the median from the quartile calculation

        if n % 2 == 1:
            lowQ = user_amount[:n//2]
            highQ = user_amount[n//2+1:]
        # If the list has an even number of elements, include the median in both halves
        else:
            lowQ = user_amount[:n//2]
            highQ = user_amount[n//2:]

        q3 = medianHelper(highQ)
        q1 = medianHelper(lowQ)

        iqr =  q3 - q1

        l = q1 - 1.5 * iqr
        h = q3 + 1.5 * iqr
        
        outlier = [ amount for amount in user_amount if amount  < l or amount > h]
        
        return outlier


# ## Sub Class for Freqeuncy of transaction

# In[155]:



class Frequency(StatisticModule):
    
    def __init__(self, data, xCoord, yCoord ):
        super().__init__(data)
        self.__xCoord = xCoord
        self.__yCoord = yCoord
        
    def getFreq(self):
        
        data = super().getData()
        
        # initialize frequency
        freq = 0
        
        # loop throught all locations (xcoordinate, ycoordinates)
        for transaction in data:
            for trans in data[transaction]:

                # set each transaction detail to t
                t = data[transaction][trans]

                # check if xcordinate is xCoord and if xCordinate is yCoord
                if t['xCoordinate'] == self.__xCoord and t['yCoordinate'] == self.__yCoord:

                    freq += 1

        return  freq
    
    


# ## SUb CLass for Percentile

# In[156]:


class Percentile(StatisticModule):
    
    def __init__(self, percentile, data,user_id = None):
        super().__init__(data)
        self.__percentile = percentile
        self.__user_id = user_id
        
    def getPercentile(self):

        # get amount fot a particular user or all user
        user_amount = super().getAmount(self.__user_id)

        # checks if transaction exist
        if user_amount is not None :
            try:  
                # Sort the transaction amounts
                user_amount_sorted = sorted(user_amount)
                
                # Calculate the index of the nth percentile
                index = int(self.__percentile / 100 * len(user_amount_sorted))

                # Return the value at the calculated index
                return user_amount_sorted[index]
                

            except IndexError:
                print("nth Percentile must be between 0 - 100 ")

        else: return f" User ID {self.__user_id} does not exist"  


# In[ ]:





# ## Some metrics used for computation

# ## the interquartile range of any user’s transactions and of all users
# 
# Use the getTransaction() function to retrieve a list of all transaction amounts for the given user.
# 
# Sort the list of transaction amounts in ascending order.
# 
# check if the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
# 
# Split the sorted list into two halves: one half containing all the elements less than the median, and the other half containing all the elements greater than the median.
# 
# Calculate the median of each half using the same method as step 3.
# 
# Subtract the lower quartile (Q1) from the upper quartile (Q3) to get the interquartile range (IQR).
# 

# ## the location centroid of any user, based on their transaction locations

# ## the standard deviation of any specific user’s transactions
# 
#  [4042.34, 3949.97, 4134.79, 4038.09, 3874.92, 3976.08, 3855.62, 4070.97, 3937.79, 3914.93]
#  first retrieves the transactions for the given user
#  
#  calculates the number of transactions 
#  
#  Find the mean (average) of the data set.
#  
#  Subtract the mean from each data point, and square the result for each data point.
#   
#  The variance is then calculated as the sum of these squared deviations divided by the number of transactions minus one.
#  
#  Finally, the standard deviation is calculated as the square root of the variance
#  
#  s = √(Σ(x - μ)² / (n - 1))

# ## an abnormal transaction for any given user.
# 
# checks whether the amount is more than two standard deviations away from the mean.
# 
# If it is, the transaction is considered abnormal and added to the list of abnormal transactions. 
# 
# If no abnormal transactions are found, it returns a message indicating that.

# ## returns the outlier of any location and of any user. 
# 
# sort data
# 
# get lenght of data set
# 
# find q1 and q3
# 
# use q1 and q3 to get iqr 
# 
# use the above to calculate first quatile and third quatile 
# 
# check data set for amounts less than first quatile and amounts higher than 3rd quartile 
# 

# ##  A function that returns the nth percentiles of transactions of any user and of all user
# 
# The nth percentile of a set of data is the value at which n percent of the data is below it
# 
# In everyday life, percentiles are used to understand values such as test scores, health indicators, and other measurements.
# 
# Percentiles for the values in a given data set can be calculated using the formula:
# 
# n = (P/100) x N
# 
# They are often used to interpret test scores—such as SAT scores—so that test-takers can compare their performance to that of other students. For example, a student might earn a score of 90 percent on an exam. 
# 
# That sounds pretty impressive; however, it becomes less so when a score of 90 percent corresponds to the 20th percentile, meaning only 20 percent of the class earned a score of 90 percent or lower.

# In[ ]:




