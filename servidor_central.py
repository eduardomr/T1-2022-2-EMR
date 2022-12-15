from socket import *
import threading
import time
import json


def configura():
    global ip_distribuido1
    global ip_distribuido2
    
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
    #servidor_central2 = socket(AF_INET, SOCK_STREAM)
    destino1 = (ip_distribuido1,porta1)
    #destino2 = (ip_distribuido2,porta2)
    servidor_central1.connect(destino1)
    #servidor_central2.connect(destino2)











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
    print("7 - Sistema de Alarme")
    opt = int(input())
    if opt == 1:
        servidor_central1.send(bytes("L01","utf8"))
    elif opt == 2:
        servidor_central1.send(bytes("DL01","utf8"))
    elif opt == 3:
        servidor_central1.send(bytes("L02","utf8"))
    elif opt == 4:
        servidor_central1.send(bytes("DL02","utf8"))
    elif opt == 5:
        servidor_central1.send(bytes("AC","utf8"))
    elif opt == 6:
        servidor_central1.send(bytes("DAC","utf8"))
    elif opt == 7:
        servidor_central1.send(bytes("AL","utf8"))
    else:
        print("Opção inválida!")
        menu_sala1()


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
    print("7 - Sistema de Alarme")
    opt = int(input())
    if opt == 1:
        servidor_central2.send(bytes("L01","utf8"))
    elif opt == 2:
        servidor_central2.send(bytes("DL01","utf8"))
    elif opt == 3:
        servidor_central2.send(bytes("L02","utf8"))
    elif opt == 4:
        servidor_central2.send(bytes("DL02","utf8"))
    elif opt == 5:
        servidor_central2.send(bytes("AC","utf8"))
    elif opt == 6:
        servidor_central2.send(bytes("DAC","utf8"))
    elif opt == 7:
        servidor_central2.send(bytes("AL","utf8"))
    else:
        print("Opção inválida!")
        menu_sala1()

def apresenta_menu():
    opcao = 0
    print("Bem vindo ao sistema de automação de predial!")
    print("Escolha uma das opções abaixo:")
    print("1 - Controlar Sala 1")
    print("2 - Controlar Sala 2")
    print("3 - Controlar salas em conjunto ")
    print("4 - Sair do sistema")
    opcao = int(input())
    if opcao == 1:
        menu_sala1()
    elif opcao == 2:
        menu_sala2()
        


def main():
    configura()
    apresenta_menu()


if __name__ == "__main__":
    main()