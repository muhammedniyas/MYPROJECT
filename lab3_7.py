# -*- coding: utf-8 -*-

Created on Sun Mar 18 19:54:48 2018

@author: Muhammed Niyas K P
#Program to find whether an user enetered number is prime or not

Number = int(input('Enter the number'))

if Number > 1:
   # check for factors
   for i in range(2,Number):
       if (Number % i) == 0:
           print(Number,"is not a prime number")
           break
   else:
       print(Number,"is a prime number")


