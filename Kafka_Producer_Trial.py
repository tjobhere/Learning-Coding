# -*- coding: utf-8 -*-
"""
Working with Kafka via Python

"""
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9093')
topic_name=input('Enter TOPIC name :')
message=bytes(input('Enter message :'),'utf-8')
producer.send(topic_name,message)

