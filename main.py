from flask import Flask, render_template # estruturas para criar o site
from flask_socketio import SocketIO, send # estruturas para criar o chat

app = Flask(__name__) # cria o site
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") # define que a função abaixo vai ser acionada quando o evento de "message" acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem para todo mundo conectado no site

@app.route("/") # cria a página do site
def home():
    return render_template("index.html") # essa página vai carregar esse arquivo html que está aqui

socketio.run(app, host='192.168.1.8') # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado