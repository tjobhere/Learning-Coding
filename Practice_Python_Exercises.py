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


#Exercise 4
num=int(input('Enter number:'))
for x in range(1,num+1): #+1 is to include the number itself in the range
   if (num%x)==0:
        print(x)


#Exercise 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 1, 1, 1, 5, 6, 7, 7 ,2, 3, 4]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
outcome=[]

for x_a in a:
    if x_a in b:
        print('Found : ',x_a)
        if x_a in outcome:
            continue
        else:
            outcome.append(x_a)
outcome.sort()
print(outcome)


#Exercise 6
input_str=input('Enter String:')
inverse_str=input_str[::-1]
if input_str.capitalize()==inverse_str.capitalize():
    print('You have entered a Palindrome')
else:
    print('Not a Palindrome')
    
'''