from socket import *
import threading
import time
import json


def configura():
    global servidor_central1

    with open('configuracao_sala_01.json', 'r') as f:
        data = json.load(f)
        ip_distribuido1 = data["ip_servidor_distribuido"]
        porta1 = data["porta_servidor_distribuido"]
    # Closing file
    f.close()

    with open('configuracao_sala_02.json', 'r') as f:
        data = json.load(f)
        ip_distribuido2 = data["ip_servidor_distribuido"]
        porta2 = data["porta_servidor_distribuido"]
    f.close()

    servidor_central1 = socket(AF_INET, SOCK_STREAM)
    servidor_central2 = socket(AF_INET, SOCK_STREAM)
    destino1 = (ip_distribuido1,porta1)
    destino2 = (ip_distribuido2,porta2)
    print(destino1)
    servidor_central1.connect(destino1)
    servidor_central2.connect(destino2)

def menu_sala1():
    global servidor_central1
    print("SALA 1")
    print("Escolha uma das opções abaixo:")
    print("1 - Ligar Luz 1")
    print("2 - Desligar Luz 1")
    print("3 - Ligar Luz 2")
    print("4 - Desligar Luz 2")
    print("5 - Ligar Ar Condicionado")
    print("6 - Desligar Ar Condicionado")
    print("7 - Ligar Sistema de Alarme")
    print("8 - Ligar todas as lâmpadas da sala")
    print("9 - Desligar todas as lâmpadas da sala")
    print("10 - Ligar todas as cargas da sala")
    print("10 - Desligar todas as cargas da sala")
    opt = int(input())
    if opt == 1:
        servidor_central1.send(bytes("L01","utf8"))
        menu_sala1()
    elif opt == 2:
        servidor_central1.send(bytes("DL01","utf8"))
        menu_sala1()
    elif opt == 3:
        servidor_central1.send(bytes("L02","utf8"))
        menu_sala1()
    elif opt == 4:
        servidor_central1.send(bytes("DL02","utf8"))
        menu_sala1()
    elif opt == 5:
        servidor_central1.send(bytes("AC","utf8"))
        menu_sala1()
    elif opt == 6:
        servidor_central1.send(bytes("DAC","utf8"))
        menu_sala1()
    elif opt == 7:
        servidor_central1.send(bytes("AL","utf8"))
    elif opt == 8:
        servidor_central1.send(bytes("L12","utf8"))
    elif opt == 9:
        servidor_central1.send(bytes("D12","utf8"))
    elif opt == 10:
        servidor_central1.send(bytes("LG","utf8"))
    elif opt == 7:
        servidor_central1.send(bytes("DG","utf8"))
        menu_sala1()
    else:
        print("Opção inválida!")
        menu_sala1()

def menu_salas12():
    print("Você está controlando as salas 1 e 2")
    print("Escolha uma das opções abaixo:")
    print("1 - Ligar Luz 1")
    print("2 - Desligar Luz 1")
    print("3 - Ligar Luz 2")
    print("4 - Desligar Luz 2")
    print("5 - Ligar Ar Condicionado")
    print("6 - Desligar Ar Condicionado")
    print("7 - Ligar Sistema de Alarme")
    print("8 - Ligar todas as lâmpadas da salas")
    print("9 - Desligar todas as lâmpadas das salas")
    print("10 - Ligar todas as cargas das salas")
    print("11 - Voltar ao menu principal")
    opt = int(input())
    if opt == 1:
        servidor_central1.send(bytes("L01","utf8"))
        servidor_central2.send(bytes("L01","utf8"))
        menu_salas12()
    elif opt == 2:
        servidor_central1.send(bytes("DL01","utf8"))
        servidor_central2.send(bytes("DL01","utf8"))
        menu_salas12()
    elif opt == 3:
        servidor_central1.send(bytes("L02","utf8"))
        servidor_central2.send(bytes("L02","utf8"))
        menu_salas12()
    elif opt == 4:
        servidor_central1.send(bytes("DL02","utf8"))
        servidor_central2.send(bytes("DL02","utf8"))
        menu_salas12()
    elif opt == 5:
        servidor_central1.send(bytes("AC","utf8"))
        servidor_central2.send(bytes("AC","utf8"))
        menu_salas12()
    elif opt == 6:
        servidor_central1.send(bytes("DAC","utf8"))
        servidor_central2.send(bytes("DAC","utf8"))
        menu_salas12()
    elif opt == 7:
        servidor_central1.send(bytes("AL","utf8"))
        servidor_central2.send(bytes("AL","utf8"))
        menu_salas12()
    elif opt == 8:
        servidor_central1.send(bytes("L12","utf8"))
        servidor_central2.send(bytes("L12","utf8"))
        menu_salas12()
    elif opt == 9:
        servidor_central1.send(bytes("D12","utf8"))
        servidor_central2.send(bytes("D12","utf8"))
        menu_salas12()
    elif opt == 10:
        servidor_central1.send(bytes("LG","utf8"))
        servidor_central2.send(bytes("LG","utf8"))
        menu_salas12()
    elif opt == 11:
        menu_principal()

def menu_sala2():
    global servidor_central2
    print("SALA 2")
    print("Escolha uma das opções abaixo:")
    print("1 - Ligar Luz 1")
    print("2 - Desligar Luz 1")
    print("3 - Ligar Luz 2")
    print("4 - Desligar Luz 2")
    print("5 - Ligar Ar Condicionado")
    print("6 - Desligar Ar Condicionado")
    print("7 - Ligar Sistema de Alarme")
    print("8 - Ligar todas as lâmpadas da sala")
    print("9 - Desligar todas as lâmpadas da sala")
    print("10 - Ligar todas as cargas da sala")
    print("10 - Desligar todas as cargas da sala")
    opt = int(input())
    if opt == 1:
        servidor_central2.send(bytes("L01","utf8"))
        menu_sala2()
    elif opt == 2:
        servidor_central2.send(bytes("DL01","utf8"))
        menu_sala1()
    elif opt == 3:
        servidor_central2.send(bytes("L02","utf8"))
        menu_sala1()
    elif opt == 4:
        servidor_central2.send(bytes("DL02","utf8"))
        menu_sala1()
    elif opt == 5:
        servidor_central2.send(bytes("AC","utf8"))
        menu_sala1()
    elif opt == 6:
        servidor_central2.send(bytes("DAC","utf8"))
        menu_sala1()
    elif opt == 7:
        servidor_central2.send(bytes("AL","utf8"))
    elif opt == 8:
        servidor_central2.send(bytes("L12","utf8"))
    elif opt == 9:
        servidor_central2.send(bytes("D12","utf8"))
    elif opt == 10:
        servidor_central2.send(bytes("LG","utf8"))
    elif opt == 7:
        servidor_central2.send(bytes("DG","utf8"))
        menu_sala2()
    else:
        print("Opção inválida!")
        menu_sala2()

def menu_principal():
    opcao = 0
    print("Bem vindo ao sistema de automação de predial!")
    print("Escolha uma das opções abaixo:")
    print("1 - Controlar Sala 1")
    print("2 - Controlar Sala 2")
    print("3 - Controlar salas em conjunto ")
    print("4 - Monitorar Entrada e Saida de Pessoas")

    opcao = int(input())
    if opcao == 1:
        menu_sala1()
    elif opcao == 2:
        menu_sala2()
    elif opcao == 3:
        menu_salas12()
    elif opcao == 4:
        monitora_pessoas()
        

def escuta_sala1():
    with open('configuracao_sala_01.json', 'r') as f:
        data = json.load(f)
        host = data["ip_servidor_distribuido"]
        port = data["porta_servidor_central"]
    f.close()

    servidor_distribuido = socket(AF_INET, SOCK_STREAM)
    servidor_distribuido.bind((host, port))
    servidor_distribuido.listen()
    global conexao
    global docliente
    conexao, docliente = servidor_distribuido.accept()


def escuta_sala2():
    with open('configuracao_sala_02.json', 'r') as f:
        data = json.load(f)
        host = data["ip_servidor_distribuido"]
        port = data["porta_servidor_central"]
    f.close()

    servidor_distribuido2 = socket(AF_INET, SOCK_STREAM)
    servidor_distribuido2.bind((host, port))
    servidor_distribuido2.listen()
    global conexao2
    global docliente2
    conexao2, docliente2 = servidor_distribuido2.accept()

def monitora_pessoas():
    global pessoas_sala1
    global pessoas_sala2
    global pessoas
    global conexao
    global conexao2

    while True:
        print("Pessoas na sala 1: ", pessoas_sala1)
        print("Pessoas na sala 2: ", pessoas_sala2)
        print("Pessoas no predio: ", pessoas)
        print("Aguardando atualização...")
        msg = conexao.recv(1024)
        msg = msg.decode("utf8")
        if msg == "ENTROU":
            pessoas_sala1 += 1
            pessoas += 1
        elif msg == "SAIU":
            pessoas_sala1 -= 1
            pessoas -= 1
        msg = conexao2.recv(1024)
        msg = msg.decode("utf8")
        if msg == "ENTROU":
            pessoas_sala2 += 1
            pessoas += 1
        elif msg == "SAIU":
            pessoas_sala2 -= 1
            pessoas -= 1

def main():
    global pessoas
    pessoas = 0
    global pessoas_sala1
    global pessoas_sala2
    pessoas_sala1 = 0
    pessoas_sala2 = 0
    configura()
    escuta_sala1()
    escuta_sala2()
    menu_principal()
    


if __name__ == "__main__":
    main()
