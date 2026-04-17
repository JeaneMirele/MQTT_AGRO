import paho.mqtt.client as mqtt
import json
import time
import random

broker = "localhost"
client = mqtt.Client()
client.connect(broker)

while True:
    dados = {
        "temperatura": round(random.uniform(20.0, 35.0), 2),
        "umidade_solo": round(random.uniform(10.0, 60.0), 2)
    }
    client.publish("agro/sensores", json.dumps(dados))
    print(f"Enviado: {dados}")
    time.sleep(5)