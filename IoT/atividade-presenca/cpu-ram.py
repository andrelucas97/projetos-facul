import paho.mqtt.client as mqtt
import sys
from time import sleep
import psutil

TOPICO = 'channels/1756854/publish'
CLIENT_ID = 'DTgjBhg1BD0cMCIDHwkjCzg'
USERNAME = 'DTgjBhg1BD0cMCIDHwkjCzg'
PASSWORD = 'swiBhXJrQF9sTXMgiHeE/q3i'
BROKER = 'mqtt3.thingspeak.com'
PORT = 1883

def conectou(client, userdata, flags, rc):
    if rc==0:
        print('Conectado ao broker!!!')
    else:
        print('Não conectado, falha na conexão!!! ERRO = ', rc)

client = mqtt.Client(client_id = CLIENT_ID)
client.on_connect = conectou
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT)
client.loop_start()

while True:
        
    cpuPercent = psutil.cpu_percent()
    ramPercent = psutil.virtual_memory().percent
    payload="field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)
    client.publish(TOPICO, payload, qos=0)
    print (" CPU =",cpuPercent,"   RAM =",ramPercent)
    sleep(20)
