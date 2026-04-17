from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
import json
import threading

app = Flask(__name__)

dados_atuais = {"temperatura": "--", "umidade_solo": "--"}

def on_connect(client, userdata, flags, rc):
    client.subscribe("agro/sensores")

def on_message(client, userdata, msg):
    global dados_atuais
    dados_atuais = json.loads(msg.payload.decode())
    
    if dados_atuais["umidade_solo"] != "--" and float(dados_atuais["umidade_solo"]) < 30.0:
        comando = {"acao": "ligar_irrigador", "motivo": "umidade baixa"}
        client.publish("agro/atuadores/irrigador", json.dumps(comando))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883)

threading.Thread(target=client.loop_forever, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dados')
def dados():
    return jsonify(dados_atuais)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)