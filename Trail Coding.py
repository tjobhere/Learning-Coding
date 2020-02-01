#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:50:42 2020

@author: thomas
"""

'''
Multi-line
comment
'''

#print ('Thomas\'s Hello World..')
#quote='Simple string'
#multi_line = '''just 
#list this '''

'''

print("%s %s %s" % ('Directly', quote, quote+multi_line))

print('5 times ' *5)
print ('No new line', end='')
print('newline')
'''

'''
#Playing with lists
grocery_list = ['Juice', 'Potato', 'Fruits', 'Bread']
print(grocery_list)
print('First item : ', grocery_list[0])
print(grocery_list[1:3])

other_tasks = ['Buy Stationary', 'Wash Car', 'Visit Doctor', 'Pay bill']
to_do_list = [other_tasks, grocery_list]
print(to_do_list)
print(to_do_list[1])
print(to_do_list[0][1])
grocery_list.append('Onions')
print(grocery_list)
grocery_list.insert(1,'Jam')
print(to_do_list)
grocery_list.sort()
print(to_do_list)
other_tasks.sort()
print(other_tasks)
other_tasks.reverse()
print(other_tasks)
print(to_do_list)
del other_tasks[2]
#other_tasks.remove('Pay bill')
print(other_tasks)
print(to_do_list)
to_do_list2 = grocery_list+other_tasks
print(to_do_list2)
print('Length : ',len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list))


#Playing with Tuples
tup1=1,2,3,5
print (tup1)
print(len(tup1))
print(type(tup1))
new_list=list(tup1)
print(new_list)
print(type(new_list))
new_tup=tuple(new_list)
print(type(new_tup))
print(min(new_tup), ' ', max(new_tup))


#Playing with Dictionaries
shopping_list = {'Fruit' : 'Banana', 'Leafy' : 'Spinach', 'Meat' : 'Chicken', 'Drink' : 'Pepsi'}
print(type(shopping_list))
print(shopping_list['Meat'])
del shopping_list['Meat']
print(shopping_list)
shopping_list['Meat']= 'Lamb'
print(shopping_list)
shopping_list['Meat']='Chicken'
print(shopping_list)
print(shopping_list.keys())
print(shopping_list.values())


#Playing with If Else Elif
age=int(input())
if age<=17 :
    print("Still can't vote")
elif age==18:
    print("Just turned 18")
elif (age>18) and (age<60) :
    print('I can vote and am mid age!')
else :
    print('I am a senior citizen')


#Playing with Loops
for x in range(0,5):
    print(x,' ', end='')
    
print('\n')
grocery_list = ['Juice', 'Potato', 'Fruits', 'Bread']
for x in grocery_list:
    print(x)
num_list=[[1,2,3],[10,20,30],[100,200,300]]
print(len(num_list))
for x in range(0,len(num_list)):
#    print(num_list[x])
    for y in range(0,len(num_list[x])):
        print(num_list[x][y])
        
import random

random_num = random.randrange(0,100)
while random_num > 20:
    print(random_num)
    random_num=random.randrange(0,100)

    
#playing with strings
test_string = "I know that this is a really long string for a test"

print(len(test_string))
print(test_string)
print(test_string[0:len(test_string)])
print(test_string[-5:]) #the last 5 characters
print(test_string[:-5]) #start till the last 5 characters

print(test_string.capitalize())
print(test_string.find("that this"))
print(test_string.isalpha())
print(test_string.isalnum())
print(test_string.replace("string","sentence"))
quote_list=test_string.split(" ") #convert the consituents of a string into a list using the defined separater
print(quote_list)
print(type(quote_list))
'''

#Playing with files

