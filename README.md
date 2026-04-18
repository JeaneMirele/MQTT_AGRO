# Simulador de Agricultura 4.0 - Monitoramento e Controle de Irrigação

Este projeto simula um ecossistema de Agricultura 4.0 utilizando comunicação indireta via protocolo MQTT. 
O sistema integra sensores de campo virtuais, um painel de monitoramento web e um atuador para controle de irrigação, simulando um ambiente real de automação agrícola.

##  Funcionalidades

- **Sensores Virtuais:** Geração contínua de dados de temperatura e umidade do solo.
- **Painel Web (Dashboard):** Interface em Flask para visualização em tempo real dos dados recebidos.
- **Lógica de Automação:** Disparo automático de comandos de irrigação quando a umidade do solo desce abaixo de 30%.
- **Atuador Virtual:** Recebe e processa comandos de ativação do sistema de rega.

##  Arquitetura

A comunicação é baseada no modelo **Publish/Subscribe** através de um Broker MQTT:

1. Os **Sensores** publicam dados no tópico `agro/sensores`.
2. O **Painel Web** subscreve o tópico dos sensores e publica comandos no tópico `agro/atuadores/irrigador`.
3. O **Atuador** subscreve o tópico de comandos para executar a ação de rega.

##  Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Broker MQTT:** Eclipse Mosquitto (via Docker)
- **Framework Web:** Flask
- **Biblioteca MQTT:** Paho-MQTT
- **Interface:** HTML5/CSS3 com atualização via API (Fetch)

##  Estrutura do Projeto

```text
simulador-agro/
├── app.py                  # Servidor Flask e lógica de monitoramento
├── sensor_ambiente.py      # Simulação dos sensores de campo
├── atuador_irrigador.py    # Simulação do sistema de irrigação
├── templates/
│   └── index.html          # Interface visual do Dashboard
└── venv/                   # Ambiente virtual Python
```

## Como Executar
 1. Preparar o Broker
Certifique-se de que o Docker está em execução e inicie o Mosquitto:

```bash
# Inicia o broker MQTT no Docker
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto
```

2. Configurar o Python
Ative o seu ambiente virtual e instale as dependências:

```bash
pip install paho-mqtt flask
```

3. Iniciar o Sistema
Abra três terminais e execute os arquivos na seguinte ordem:

Terminal 1 (Atuador):
```bash
python atuador_irrigador.py

```
Terminal 2 (Painel Web):
```Bash
python app.py
```
Acesse http://localhost:5000 no seu navegador.

Terminal 3 (Sensores):
``` Bash
python sensor_ambiente.py
```

## Licença
Este projeto foi desenvolvido para fins acadêmicos na UFRN (Universidade Federal do Rio Grande do Norte).
