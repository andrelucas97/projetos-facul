#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep
from random import randint

luzCozinha = "area10/5000/cozinha"
luzGaragem = "area10/5000/garagem"
luzSala = "area10/5000/Sala"
luzJardim = "area10/5000/jardim"

PORTA_TCP = 1883

# gera valor 0 na cozinha
def sensorCozinha():
    return 0

def sensorGaragem():
    return 0

def sensorSala():
    return 0

def sensorJardim():
    return 0

# cria um cliente MQTT
cliente = mqtt.Client()

# conecta ao broker
cliente.connect("broker.hivemq.com", PORTA_TCP)

while True:
    # Sensor Gas GLP
    cozinha = str(sensorCozinha())
    cliente.publish(luzCozinha,cozinha,qos=1)

    print ("Luz Acesa!")
    sleep(5)

    garagem = str(sensorCozinha())
    cliente.publish(luzGaragem,garagem,qos=1)

    garagem = str(sensorGaragem())
    cliente.publish(luzGaragem,garagem,qos=1)

    sala = str(sensorSala())
    cliente.publish(luzSala,sala,qos=1)   

    jardim = str(sensorJardim())
    cliente.publish(luzJardim,jardim,qos=1)    