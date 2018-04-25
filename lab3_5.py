# -*- coding: utf-8 -*-

Created on Tue Feb 20 17:17:27 2018

@author: Admin

#Choosing whether the user needs to convert into either fahrenheit or kelvin
celsius = int(input('Enter the degree celsius value'))
print('Press 1.Fahrenheit 2. Kelvin')
choice=int(input('Enter choice'))

#Calculation of equivalent degree celsius
if (choice==1):
    fahrenheit = (9/5)*celsius + 32
    print('Equivalent of', celsius, '=', fahrenheit)
elif (choice==2):
    kelvin = celsius + 273.15
    print('Equivalent of', celsius, '=', kelvin)
else:
    print('You have entered a wrong choice')

