import paho.mqtt.client as mqtt
from random import randint
from time import sleep
########################################

default_broker = "wild.mat.ucm.es"
default_topic = "clients/cris_numbers"


def main(broker, topic):
    client = mqtt.Client() #create new instance
    client.connect(broker) #connect to broker
    print("Conexion establecida")
    client.loop_start() #start the loop
    while True:
        num = randint(0, 10)
        print(f"Publicando: {num}")
        client.publish(topic, num)
        sleep(1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} broker topic")
        broker = default_broker
        topic = default_topic
    else:
        broker = sys.argv[1]
        topic = sys.argv[2]
    
    main(broker, topic)        