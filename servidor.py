from http import client
import socket
import threading
#HOST é onde o servidor está.
HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

"""
Percorre as pessoas da sala e envia mensagem para todas as mensagens
Se a mensagem for string a gente codigicaum instância de str
"""
def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()

        #print(i)   
        i.send(mensagem)

def enviarMensagem(nome, sala, cliente):
    while True:
        mensagem = cliente.recv(1024)
        # Fica escutando uma mensagem, se receber executa os passos abaixo.
        mensagem = f"{nome}: {mensagem.decode()}\n"
        broadcast(sala, mensagem)

"""

"""


#O While True - Conecta os clientes coloca na sala e envia para todos na sala que alguém se conectou!
while True:
    cliente, addr = server.accept()
    #Envio a mensagem em binário para o cliente
    cliente.send(b'SALA')
    #Escutar a salva o decode é para decodificar
    sala = cliente.recv(1024).decode()
    #Escutar o nome  o decode é para decodificar
    nome = cliente.recv(1024).decode()

    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(cliente)
    print(f'{nome} se conectou na sala: {sala}! INFO {addr}')
    broadcast(sala, f'{nome}: Entrou na sala!\n')
    thread = threading.Thread(target=enviarMensagem, args=(nome, sala, cliente))
    thread.start()

