# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 11:23:50 2019

@author: devadmin
"""
from kafka import KafkaConsumer
topic_name=input('Enter TOPIC name :')
consumer = KafkaConsumer(topic_name,bootstrap_servers='localhost:9093')
for message in consumer:
    #Also convert the message value that is in byte into string and then print
    msg=message.value.decode(encoding='UTF-8')
    print(msg)
    if msg=="STOP":
        break
print('Stopping..')