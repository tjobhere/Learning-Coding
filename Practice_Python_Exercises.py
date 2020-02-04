#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:10:04 2020

@author: thomas
"""
'''
This is file is to code against all the Exercises given in http://www.practicepython.org/

#Exercise 1

import datetime

name=input("Enter your name: ")
age=int(input("Enter your age: "))
now=datetime.datetime.now()
print('Current Year : ',now.year)
years_till_100=100-age
print('Years to go till 100 : ',years_till_100)
print('Hi {}. You will become 100 years in {}'.format(name,now.year+years_till_100))

#Exercise 2
num=int(input('Enter number:'))
if (num%4)==0:
    print('Number {} is Even and a multiple of 4'.format(num))
elif (num%2)==0:
    print('Number {} is Even and not a multiple of 4'.format(num))
else:
    print('Number {} is Odd'.format(num))


#Exercise 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
for counter in a:
    if counter<5:
        new_list.append(counter)
print(new_list)
'''

#Exercise 4
num=int(input('Enter number:'))
for x in range(1,num):
   if (num%x)==0:
        print(x)
print(num)

#Exercise 5
