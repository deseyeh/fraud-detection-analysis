# fraud-detection-analysis

## INTRODUCTION

The objective of this project was to develop a system that can detect fraudulent transactions within a financial dataset. In this report, we will analyze the problem that the system aims to solve and briefly discuss its key features. The system can query transactions, computing the distance between transactions, generating various statistics on the transactions, and identifying and flagging fraudulent transactions. The user interface is designed to be user-friendly and flexible, allowing for ease of use.

The program can be executed by running the main module which provides a user-friendly interface for interacting with the functions.
Users could input the necessary data, select the required function, and obtain the relevant output. 

In this report, the solution requirements for the program are outlined and discussed. The implementation section of the project report provides an explanation of the program concept, supported by a program flowchart diagram that depicts the overall program flow. The pseudocode for the modules is also provided in Appendix A, which details the module code not covered in the flowchart. Finally, the report concludes with a personal reflection on the project, highlighting areas that went well and areas that could have been improved upon, along with suggestions for alternative solutions.
O
verall, this project has been a comprehensive exercise in creating a fraud detection system that provides a wealth of information and statistical insights into the transactions. 

## PROBLEM ANAYSIS
The main objective of the project is to develop a transaction analysis system that will help in detecting fraudulent transactions and provide insights for improving business strategies. The project involves working with a dataset that contains transaction details of different users and locations that can be used to gain insights into the transaction patterns and detect any fraudulent transactions.

This program addresses the problem of identifying suspicious or anomalous transactions by providing a way to query a user's transaction details and perform statistical analyses on them. The distance module of the program uses the Euclidean distance metric to calculate the distance between two transactions based on their x- and y-coordinates. While there are other metrics available, Euclidean distance is preferred for its simplicity and intuitiveness in this scenario.

This distance can be used to determine the proximity of transactions to each other and can be used to identify transactions that occur near each other, which may be indicative of fraudulent behavior. Additionally, the distance module can be used to calculate the distance traveled by the user between two transactions, which can be useful for tracking and monitoring purposes. All of these provide insights into the patterns of transactions and identifying potential areas of concern.

The statistics module provides various statistical functions on the transactions. These functions include computing the average, median, mode, standard deviation, and z-score of the transactions for any user or all users. We also added functions for computing outliers and abnormal transactions.

Finally, we integrated all the modules into the Main module. This module provides an interface for users to interact with the system, allowing them to get distance information, compute the distance between transactions and compute various statistics on the transactions.

## SOLUTION REQUIREMENTS

•	Implement a function to read the transaction data. 

•	Implement a function that computes the distance between any two given transactions of a user.

•	Implement a function that computes the distance of transactions of any two users.

•	Implement a function that computes the average transactions of any user and of all users.

•	Implement a function that computes the mode of transactions of any user and that of all users.

•	Implement a function that computes the median of all transactions of a user and that of all users.

•	Implement a function that computes the interquartile range of any user’s transactions and of all users.

•	Implement a function that computes the location centroid of any user, based on their transaction locations.

•	Implement a function that computes the standard deviation of any specific user’s transactions.

•	Implement a function that determines whether a transaction is fraudulent or not.

•	Implement a function that returns an abnormal transaction for any given user.

•	Implement a function that computes the Z score of any user’s transactions and for all users’ transactions.

•	Implement a function that computes those frequencies of transactions at any given location.

•	Implement a function that returns the outlier of any location and of any user.

•	Implement a function that returns the nth percentiles of transactions of any user and of all users.

•	Implement a user interface module that will prompt the user to 

•	query the transaction details. 

•	Perform various statistics.

•	Compute distance between transactions

## IMPLEMENTATION OF SOLUTION

Exception handling is utilized in the program, mainly to handle file handling errors, value errors, and key errors. For example, if the transaction file is found to be unreadable due to data corruption or not found in the directory, an exception is caught, and an error message is returned to the user. This approach makes the program more robust and less likely to experience unexpected crashes caused by missing files or directories. To prevent catching unintended errors, the program only catches the FileNotFound error, rather than catching all possible exceptions.

The program uses value error exception to handle user input of Transaction ID and User ID before passing it to a function. The test_module has a user interface with various menus for users to select operations, and a lastMenu function is implemented to provide options for users to try again, exit to main menu or exit the program. The lastMenu function is reusable in different functions without duplicating code.

The solution is implemented by breaking down the problem into smaller subproblems and designing individual functions to solve each problem. It started by creating a dataset_module to hold the transactions data and implemented Object oriented programming (OOP) with object functions to load and retrieve data from the module.

Next, several functions were implemented in the distance_module using OOP to compute the distance between given transactions using the Euclidean distance metrics and, in the statistics_module to compute various statistics on the transaction data. 

Additionally, functions to detect fraudulent transactions for a given user was designed by comparing a transaction data with data in both the description.txt file which contains nonfraudulent transactions and the fraud-description.txt file that has the fraudulent transactions. 

The program employs if statements to determine the user's menu options. Each menu option contains if-statements to verify the user's input is valid. If the user enters an invalid option, the program displays an error message and prompts the user to return to the previous menu or exit the program using the lastMenu function.

Methods and helper methods in the statistics_module utilize parameters to accept variables and objects. In many of the functions, the parameter is set to None to allow for flexibility in the input. For instance, the getAvg function has parameters “self” that reference the instance of the class and user ID set as None. This allows for the function to compute the average of all data by providing only the data argument or to compute the average of all transactions of a specific user by providing the dataset and user ID arguments.

The implementation was tested by calling each method on an instance of a class with different input values and comparing the output with expected results. It was also tested using invalid input values to ensure that the functions handle these scenarios properly.

## PROGRAM EXECUTION
To run the program successfully, it is required to place the following files in the same folder: 'test_module.ipynb', 'dataset_module.py', 'distance_module.py', 'statistic_module.py', 'transaction.txt', 'description.txt', and 'fraud-description.txt'.

The program can be executed by running the main() function in the test_module.ipyn’. This function displays a menu of options to the user, allowing them to perform various tasks such as querying transactions, calculating statistics, and computing distance. The user can select an option by entering the corresponding number, and the program will perform the appropriate action based on the user's input. To navigate out of any point in the program, enter an invalid option to retrieve the menu options.

Overall, the program is designed to be user-friendly and easy to navigate, with clear instructions and error messages to guide the user through the various tasks.

## PROGRAM STRUCTURE - FLOWCHART

![image](https://user-images.githubusercontent.com/100138272/234719827-38aeb931-661c-47a7-94fe-5ec51242ee79.png)

# REFLECTION
This report discussed the development of a fraud detection system, which aimed to provide insights and statistical information on transactions made by various users. The report started with the problem analysis, where the problem statement was clearly defined, and the requirements for the solution were identified.

The system uses simple Euclidean distance metrics to calculate the distance between transactions, which is a good starting point for simple fraud detection. However, more advanced distance metrics could be explored, such as Mahalanobis distance, to better account for differences in the transaction features. Additionally, it is important to consider the appropriate unit of measurement for the coordinates when computing distances.

It may be useful to consider more advanced statistical techniques and machine learning models to further analyze the dataset and identify patterns or anomalies. One of the challenges in identifying abnormal transactions is that it can be difficult to determine a clear threshold for what constitutes abnormal behavior. In addition, some types of fraud or abnormal behavior may not be easily detectable through traditional methods such as analyzing transaction amounts or frequency.

In the program, z-score is used to identify abnormal transactions by determining how many standard deviations a particular transaction is from the mean of the user's transaction. However, this method may not be effective in all cases, as it assumes a normal distribution of transaction amounts and may not be sensitive to certain types of fraud or abnormal behavior. Therefore, it is important to continually update and refine fraud detection methods and to incorporate multiple approaches to identify and prevent fraudulent activity.

Also, using the "description.txt" and "fraud-description.txt" files to identify fraudulent transactions has its challenge as it is important to have access to a dataset of known fraudulent transactions in order to be able to identify them accurately. This requires a significant amount of effort to compile, as well as a careful analysis of the characteristics and patterns of fraudulent transactions to be able to effectively distinguish them from legitimate ones.

Furthermore, it is important to keep in mind that fraudulent activities can change over time, and that new types of fraud may emerge that are not accounted for in the existing dataset. Therefore, it is necessary to constantly update and refine the criteria used to identify fraudulent transactions, to ensure that they remain effective and accurate. Overall, the use of such datasets is a valuable tool in the fight against fraud, but it is important to approach their use with caution and to continually monitor and evaluate their effectiveness.

The use of Object-Oriented Programming (OOP) in this project has proven to be beneficial. It allowed for a modular and scalable design that facilitated analyzing transactions and better organizing the system. Encapsulating data and methods within classes helped to maintain the integrity of the system and improved data access control. Additionally, inheritance reduced code duplication and improved code reusability. However, it came with the challenge of a steep learning curve, especially in designing for efficiency and avoiding overly complex code structures. 

