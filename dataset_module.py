#!/usr/bin/env python
# coding: utf-8

# In[9]:


# function to load file and retrieve file
# to retrieve file from this fuction, 
# data['userID']['transactionID']['specific nested key - transaction description, cordinateX, cordinateY, amount, fraud status'])

class FileOperator:
    def __init__(self, filename = 'Transaction.txt'):
        self.filename = filename

    def read_transactions(self):
        try:
            data = {}
            with open(self.filename, 'r', encoding='ISO-8859-1') as f:
                for line in f:
                    line_items = line.strip().split(':')
                    user_id = int(line_items[0])
                    transaction_id = int(line_items[1])
                    description = line_items[2]
                    amount = float(line_items[3])
                    x_coordinate = float(line_items[4])
                    y_coordinate = float(line_items[5])
                    fraud = True if line_items[6] == "true" else False
                    data.setdefault(user_id, {})
                    data[user_id][transaction_id] = {'description': description, 'amount': amount, 'xCoordinate': x_coordinate, 'yCoordinate': y_coordinate, 'fraud': fraud}
            return data
        except FileNotFoundError:
            print('Error: File not found')
        except ValueError:
            print('Error: Invalid data in the file.')
        except:
            print('Uncaptured Error Occured')


# In[ ]:





# In[ ]:




