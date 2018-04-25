# -*- coding: utf-8 -*-

Created on Tue Feb 20 09:46:52 2018

@author: Muhammed Niyas K P
 
#PROGRAM TO FIND WHETHER AN USER GIVEN INPUT NUMBER IS ODD OR EVEN

#Recieve the input number from the user
InputNumber = input('Enter the number to be checked')

#Convert the input into an integer format
InputNumber = int(InputNumber)

#Displaying user given input
print ('The given number is', InputNumber)

#Checking whether the given number is odd or even
if (InputNumber%2 == 0):
   print('The given number', InputNumber, 'is even')
else:
    print('The given number', InputNumber, 'is odd')

 
 