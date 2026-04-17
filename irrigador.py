import paho.mqtt.client as mqtt
import json

broker = "localhost"

def on_connect(client, userdata, flags, rc):
    print("Atuador conectado.")
    client.subscribe("agro/atuadores/irrigador")

def on_message(client, userdata, msg):
    comando = json.loads(msg.payload.decode())
    
    if comando.get("acao") == "ligar_irrigador":
        print(f"Irrigador ativado! Motivo: {comando.get('motivo')}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker)

print("Atuador aguardando comandos...")
client.loop_forever()