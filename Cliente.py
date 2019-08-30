import socket
import sys
import threading

clienteHost = 'localhost'
clientePort = 8899

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((clienteHost, clientePort))

msg = input('Digite um comando:')
while (msg != 0):
    cliente.send(msg.encode("utf-8"))
    resposta = cliente.recv(1024)
    print(resposta.decode("utf-8"))
    sys.stdout.flush()
    msg = input('Digite um comando:')

cliente.close()