import socket
import threading
import time


host = gethostname()
port = 5000
servidor_central = socket(AF_INET, SOCK_STREAM)
servidor_central.bind((host, port))
servidor_central.listen()
conexao, docliente = servidor_central.accept()

print("o cliente =", docliente, "conectou-se ao servidor")
while(1):
    msg = conexao.recv(1024)
    if not msg:
        break
    print("recebido:", msg.decode())
    conexao.send(msg)