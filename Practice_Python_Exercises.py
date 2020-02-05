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
    

#Exercise 7 -- Lst comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x%2==0]
print(b)


#Exercise 8 -- Rock Paper Scissor --> Human vs. Computer
import random

Options=['Rock','Paper','Scissor']
continue_flag='y'
while continue_flag!='n':
    human_in=input('Enter choice (Rock, Paper, Scissor): ')
    computer_ctr=random.randrange(0,3)
    computer_choice=Options[computer_ctr]
    print('Computer choice: ',computer_choice)
    if (human_in.capitalize()=='Rock'):
        if computer_choice.capitalize()=='Scissor':
            print('You win!!')
        elif computer_choice.capitalize()=='Paper':
            print('You lose!')
        else:
            print('Draw')
    if (human_in.capitalize()=='Paper'):
        if computer_choice.capitalize()=='Rock':
            print('You win!!')
        elif computer_choice.capitalize()=='Scissor':
            print('You lose!')
        else:
            print('Draw')
    if (human_in.capitalize()=='Scissor'):
        if computer_choice.capitalize()=='Paper':
            print('You win!!')
        elif computer_choice.capitalize()=='Rock':
            print('You lose!')
        else:
            print('Draw')
    continue_flag=input('Continue(y/n)? ')


#Exercise 9
import random

flag='Y'
while flag=='y' or flag=='Y':    
    rnd_num=random.randint(1,9) # Generates a random integer between 1 and 9 including them
    user_in=int(input('Enter your guess (1 to 9):'))
    diff=rnd_num - user_in
    print(rnd_num)
    if diff==0:
        print('You got it!')
    elif diff<0:
        print('You guessed higher.')
    else:
        print('You guessed lower.')
    flag=input('Continue(y/n)? ')


#Exercise 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in a for y in b if x==y]
d = [x for x in c if c.count(x)==1]
print(d)


#Exercise 11 --> Check for a Prime number
import random

def check_if_prime(number_to_check):
    for i in range(2,number_to_check):
        if number_to_check%i==0:
            return("Number {} is not a Prime number".format(number_to_check))
        else:
            continue
    return("Number {} is a Prime number".format(number_to_check))

num=random.randint(1,100)
print(num)
print(check_if_prime(num))


#Exercise 12
a = [5, 10, 15, 20, 25]
print(a[0],a[len(a)-1])


#Exercise 13 --> Generate Fibonnaci numbers
def generate_fibonnaci(count):
    print('1',end=' ')
    two_previous=0
    one_previous=1
    for i in range(1,count):
        current=one_previous+two_previous
        print(current,end=' ')
        two_previous=one_previous
        one_previous=current
        
generate_fibonnaci(int(input('Enter no.s of Fibonnaci required: ')))


#Exercise 14 --> Include Lists and Sets
import random
def create_list(size):
    org_list=[]
    for i in range(0,size):
        org_list.append(random.randint(0,10))
    print('Initial List :', org_list)
    return org_list

def remove_list_duplication(input_list):
    out_list=list(set(input_list)) #results in retaining only the unique members in the list
    return out_list

list_size=random.randint(1,10)
print('De-duplicated List :',remove_list_duplication(create_list(list_size)))


#Exercise 15 --> Include split and join method in strings
input_str=input('Enter the input statement: ')
input_list=input_str.split()
print(" ".join(input_list[::-1]))


#Exercise 16 --> Password generator
import random
import string

#Create a tuple of possible values
'''
'''
#Way 1
pwd_set=[26,string.ascii_lowercase],[10,string.digits],[32,string.punctuation],[26,string.ascii_uppercase]

#print(pwd_set)
#for x in range(0,4):
#    for y in range(0,2):
#        print('x : ',x,' y: ',y,' Value : ',pwd_set[x][y],' Type : ',type(pwd_set[x][y]))

length=int(input('Enter password length: '))
psswd=''
for i in range(0,length):
    #Pick an input set at random from the tuple of possible values
    rnd_xpos=random.randint(0,3)
    
    #Pick a random position in the input set chosen based on the length of possible values of that set
    rnd_pos=random.randint(0,pwd_set[rnd_xpos][0]-1)
    
    #Pick the specific value in the chosen set string
    psswd+=(pwd_set[rnd_xpos][1][rnd_pos])
    
print(psswd)
'''
'''
#Way 2
pwd_set=string.ascii_letters+string.digits+string.punctuation
length=int(input('Enter password length: '))
psswd="".join(random.sample(pwd_set,length))
print(psswd)

#Exercise 17 --> Code as copied from the website directly
import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True #gotta play the game
    number = str(random.randint(0,9999)) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")
'''

#Exercise 22 --> Using Dictionary
file_ptr=open("nameslist_sample.txt","r")
#print(file_ptr.name)
name_list={}
line=file_ptr.readline()
while line:
   line=line.strip()
   if str(line) in name_list:
#       print('Already Existing')
       name_list[str(line)]+=1
   else:
#       print('New Key')
       name_list[str(line)]=1
   line=file_ptr.readline()

print(name_list)
file_ptr.close()