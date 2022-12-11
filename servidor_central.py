from socket import *
import threading
import time


host = '127.0.0.1'
port = 5000
servidor_central = socket(AF_INET, SOCK_STREAM)
destino = (host,port)
servidor_central.connect(destino)


while(1):
    mensagem = input()
    servidor_central.send(bytes(mensagem,"utf8"))
    if mensagem == "x":
        tcp.close()
        break