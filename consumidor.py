from paho.mqtt.client import Client

default_broker = "wild.mat.ucm.es"
default_topic = "clients/cris_numbers"

def is_prime(n):
    i=2
    while i*i < n and n%i!=0:
        i+=1
    return i*i>n

def on_message(mqttc, data, msg):
    number = int(msg.payload)
    print("MESSAGE:", data, msg.topic, number)
    if is_prime(number):
        print(f"{number} es primo")
    else:
        print(f"{number} no es primo")


def main(broker, topic):
    data = {'client' : None,
            'broker': broker}
    mqttc = Client(client_id="numbers", userdata=data)
    mqttc.on_message = on_message
    mqttc.connect(broker)
    mqttc.subscribe(topic)
    mqttc.loop_forever()


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