import socket
import threading
import platform
from uuid import getnode as get_mac

serverHost = 'localhost'
serverPort = 8899

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((serverHost, serverPort))
server.listen(5)

print('[*] Escutando %s:%d' %(serverHost, serverPort))

def cliente(cliente_socket):
    resposta = cliente_socket.recv(1024)
    print(resposta.decode("utf-8"))

    if resposta.decode("utf-8") == '/quem':
        msg = platform.node()
        cliente_socket.send(msg.encode("utf-8"))
        #cliente_socket.recv()

    elif resposta.decode("utf-8") == '/ip':
        msg2 = socket.gethostbyname(socket.gethostname())

        cliente_socket.send(msg2.encode("utf-8"))
        #cliente_socket.close()


    elif resposta.decode("utf-8") == '/mac':
        msg = str(':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2)))
        print(msg)
        cliente_socket.send(msg.encode("utf-8"))
        #cliente_socket.close()
        pass

    elif resposta.decode("utf-8") == '/sys':
        msg = platform.platform()
        print(msg)
        cliente_socket.send(msg.encode("utf-8"))
        #cliente_socket.close()
        pass

    elif resposta.decode("utf-8") == '/dev':
        msg = ('Gustavo, Mauricio')
        print(msg)
        cliente_socket.send(msg.encode("utf-8"))
        #cliente_socket.close()
        pass
    else:
        msg = ('comando invalido')
        print(msg)
        cliente_socket.send(msg.encode("utf-8"))
        #cliente_socket.close()
        pass


while True:
    client, addr = server.accept()
    print('[*] Conexão aceita de: %s:%d' %(addr[0], addr[1]))
    client_thread = threading.Thread(target=cliente, args=(client,))
    client_thread.start()