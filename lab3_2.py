# -*- coding: utf-8 -*-

Created on Tue Feb 20 12:09:32 2018

@author: Muhammed Niyas K P
#Asking the user value
limit = input('Enter the range')
limit = int(limit)

#Printing the odd numbers upto the range
print('The odd numbers upto', limit, 'are')
for x in range(limit):
   if (x%2 != 0):
      print(x)


    
    





