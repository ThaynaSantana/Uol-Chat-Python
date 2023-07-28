from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcao de enviar mensagem
@socketio.on("message")
def manage_message(message):
    send(message, broadcast=True)

# cria nossa 1°pagina primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")
# roda nosso aplicativo
#app.run(debug=True) # debug=True não preciso ficar rodando o site toda hora
socketio.run(app, host="localhost")

# websocket