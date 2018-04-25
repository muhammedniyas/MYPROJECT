# -*- coding: utf-8 -*-

Created on Wed Feb 21 12:12:03 2018

@author: Muhammed Niyas K P
 #Program to print to the sum of exponenetial series upto a range
 
 #Recieving the limit of series
 limitnumber = int(input('Enter the limit'))
 
 sum = 1.0
 
 #Program logic
 for x in range(limitnumber-1, 1, -1):
     sum = 1+1*sum/x
     
print('The sum of series is', sum)
 
 
