from socket import *
import threading
import time
import json


def configura():
    global servidor_central1
    global servidor_central2

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
    print("11 - Desligar todas as cargas da sala")
    print("12 - Voltar ao menu principal")
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
        menu_sala1()
    elif opt == 8:
        servidor_central1.send(bytes("L12","utf8"))
        menu_sala1()
    elif opt == 9:
        servidor_central1.send(bytes("D12","utf8"))
        menu_sala1()
    elif opt == 10:
        servidor_central1.send(bytes("LG","utf8"))
        menu_sala1()
    elif opt == 11:
        servidor_central1.send(bytes("DG","utf8"))
        menu_sala1()
    elif opt == 12:
        menu_principal()
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
    print("8 - Desligar Sistema de Alarme")
    print("9 - Ligar todas as lâmpadas da salas")
    print("10 - Desligar todas as lâmpadas das salas")
    print("11 - Ligar todas as cargas das salas")
    print("12 - Voltar ao menu principal")
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
        servidor_central1.send(bytes("DAL","utf8"))
        servidor_central2.send(bytes("DAL","utf8"))
        menu_salas12()
    elif opt == 9:
        servidor_central1.send(bytes("L12","utf8"))
        servidor_central2.send(bytes("L12","utf8"))
        menu_salas12()
    elif opt == 10:
        servidor_central1.send(bytes("D12","utf8"))
        servidor_central2.send(bytes("D12","utf8"))
        menu_salas12()
    elif opt == 11:
        servidor_central1.send(bytes("LG","utf8"))
        servidor_central2.send(bytes("LG","utf8"))
        menu_salas12()
    elif opt == 12:
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
    print("8 - Desigar Sistema de Alarme")
    print("9 - Ligar todas as lâmpadas da sala")
    print("10 - Desligar todas as lâmpadas da sala")
    print("11 - Ligar todas as cargas da sala")
    print("12 - Desligar todas as cargas da sala")
    print("13 - Voltar ao menu principal")
    opt = int(input())
    if opt == 1:
        servidor_central2.send(bytes("L01","utf8"))
        menu_sala2()
    elif opt == 2:
        servidor_central2.send(bytes("DL01","utf8"))
        menu_sala1()
    elif opt == 3:
        servidor_central2.send(bytes("L02","utf8"))
        menu_sala2()
    elif opt == 4:
        servidor_central2.send(bytes("DL02","utf8"))
        menu_sala2()
    elif opt == 5:
        servidor_central2.send(bytes("AC","utf8"))
        menu_sala2()
    elif opt == 6:
        servidor_central2.send(bytes("DAC","utf8"))
        menu_sala2()
    elif opt == 7:
        servidor_central2.send(bytes("AL","utf8"))
    elif opt == 8:
        servidor_central2.send(bytes("DAL","utf8"))
        menu_sala2()
    elif opt == 9:
        servidor_central2.send(bytes("L12","utf8"))
        menu_sala2()
    elif opt == 10:
        servidor_central2.send(bytes("D12","utf8"))
        menu_sala2()
    elif opt == 11:
        servidor_central2.send(bytes("LG","utf8"))
        menu_sala2()
    elif opt == 12:
        servidor_central2.send(bytes("DG","utf8"))
        menu_sala2()
    elif opt == 13:
        menu_principal()
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
    print("5 - Sair do sistema")

    opcao = int(input())
    if opcao == 1:
        menu_sala1()
    elif opcao == 2:
        menu_sala2()
    elif opcao == 3:
        menu_salas12()
    elif opcao == 4:
        menu_principal()
       # monitora_pessoas()
    elif opcao == 5:
        print("Saindo do sistema...")
        servidor_central1.close()
        servidor_central2.close()
        exit()
        


def main():
    configura()
    menu_principal()





if __name__ == "__main__":
    main()
