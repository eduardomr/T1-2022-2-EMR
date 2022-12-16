# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from socket import *
import json
import time
import datetime
import csv


global sala

# Configuracao do Servidor Distribuido (Escuta) ----------------------------------------------
def escuta1():
    with open('configuracao_sala_01.json', 'r') as f:
        data = json.load(f)
        host = data["ip_servidor_distribuido"]
        port = data["porta_servidor_distribuido"]
    f.close()
    global servidor_distribuido1
    servidor_distribuido1 = socket(AF_INET, SOCK_STREAM)
    servidor_distribuido1.bind((host, port))
    servidor_distribuido1.listen()
    global conexao1
    global docliente1
    conexao1, docliente1 = servidor_distribuido1.accept()

def configura_envio1():
    global servidor_distribuido_envia1
    with open('configuracao_sala_01.json', 'r') as f:
        data = json.load(f)
        ip_central = data["ip_servidor_central"]
        porta_central = data["porta_servidor_central"]
    # Closing file
    f.close()
    servidor_distribuido_envia1 = socket(AF_INET, SOCK_STREAM)
    destino = (ip_central, porta_central)
    servidor_distribuido_envia1.connect(destino)

def escuta2():
    with open('configuracao_sala_02.json', 'r') as f:
        data = json.load(f)
        host = data["ip_servidor_distribuido"]
        port = data["porta_servidor_distribuido"]
    f.close()
    global servidor_distribuido2
    servidor_distribuido2 = socket(AF_INET, SOCK_STREAM)
    servidor_distribuido2.bind((host, port))
    servidor_distribuido2.listen()
    global conexao2
    global docliente2
    conexao2, docliente2 = servidor_distribuido2.accept()

def configura_envio2():
    global servidor_distribuido_envia2
    with open('configuracao_sala_02.json', 'r') as f:
        data = json.load(f)
        ip_central = data["ip_servidor_central"]
        porta_central = data["porta_servidor_central"]
    # Closing file
    f.close()
    servidor_distribuido_envia2 = socket(AF_INET, SOCK_STREAM)
    destino2 = (ip_central, porta_central)
    servidor_distribuido_envia2.connect(destino2)

GPIO.setmode(GPIO.BCM)


# Configuracao das pinos GPIOs------------------------------------------------------
L_01 = -1
L_02 = -1
AC = -1
PR = -1
AL_BZ = -1
SPres = -1
SFum = -1
SJan = -1
SPor = -1
SC_IN = -1
SC_OUT = -1
DHT22 = -1
# ------------------------------------------------------------------------------------
def configuracao():
    global L_01
    global L_02
    global AC
    global PR
    global AL_BZ
    global SPres
    global SFum
    global SJan
    global SPor
    global SC_IN
    global SC_OUT
    global DHT22
    if sala ==1:
        escuta1()
        with open('configuracao_sala_01.json', 'r') as f:
            data = json.load(f)
            L_01 = data["outputs"][0]["gpio"]
            L_02 = data["outputs"][1]["gpio"]
            PR = data["outputs"][2]["gpio"]
            AC = data["outputs"][3]["gpio"]
            
            AL_BZ = data["outputs"][4]["gpio"]
            SPres = data["inputs"][0]["gpio"]
            SFum = data["inputs"][1]["gpio"]
            SJan = data["inputs"][2]["gpio"]
            SPor = data["inputs"][3]["gpio"]
            SC_IN = data["inputs"][4]["gpio"]
            SC_OUT = data["inputs"][5]["gpio"]
            DHT22 = data["sensor_temperatura"][0]["gpio"]
        f.close()
    elif sala ==2 :
        escuta2()
        with open('configuracao_sala_02.json', 'r') as f:
            data = json.load(f)
            L_01 = data["outputs"][0]["gpio"]
            L_02 = data["outputs"][1]["gpio"]
            PR = data["outputs"][2]["gpio"]
            AC = data["outputs"][3]["gpio"]
            
            AL_BZ = data["outputs"][4]["gpio"]
            SPres = data["inputs"][0]["gpio"]
            SFum = data["inputs"][1]["gpio"]
            SJan = data["inputs"][2]["gpio"]
            SPor = data["inputs"][3]["gpio"]
            SC_IN = data["inputs"][4]["gpio"]
            SC_OUT = data["inputs"][5]["gpio"]
            DHT22 = data["sensor_temperatura"][0]["gpio"]
        f.close()
    
   

    # Configuracao dos pinos GPIOs (SAIDA/ENTRADA)

    GPIO.setup(L_01, GPIO.OUT)
    GPIO.setup(L_02, GPIO.OUT)
    GPIO.setup(AC, GPIO.OUT)
    GPIO.setup(PR, GPIO.OUT)
    GPIO.setup(AL_BZ, GPIO.OUT)


    GPIO.setup(SJan, GPIO.IN)
    GPIO.setup(SPres, GPIO.IN)
    GPIO.setup(SFum, GPIO.IN)
    GPIO.setup(SPor, GPIO.IN)
    GPIO.setup(SC_IN, GPIO.IN)
    GPIO.setup(SC_OUT, GPIO.IN)
    # ------------------------------------------------------------------------------------


# Configuracao dos pinos GPIOs (DETECCAO DE EVENTOS)
    GPIO.add_event_detect(SJan, GPIO.BOTH)
    GPIO.add_event_detect(SPor, GPIO.BOTH)
    GPIO.add_event_detect(SPres, GPIO.BOTH)
    GPIO.add_event_detect(SFum, GPIO.RISING)
    GPIO.add_event_detect(SC_IN, GPIO.RISING)
    GPIO.add_event_detect(SC_OUT, GPIO.RISING)
# ------------------------------------------------------------------------------------


# funcoes de leitura dos sensores
def leituraSensorJan():
    if GPIO.event_detected(SJan):
        if GPIO.input(SJan)==1:
            return 1
        else:
            return 0


def leituraSensorPor():
    if GPIO.event_detected(SPor):
        if GPIO.input(SPor)==1:
            return 1
        else:
            return 0


def leituraSensorPres():
    if GPIO.event_detected(SPres):
        if GPIO.input(SPres)==1:
            return 1
        else:
            return 0

# ------------------------------------------------------------------------------------




## Funcoes Ligar e desligar luzes
def ligaLuz01():
    GPIO.output(L_01, GPIO.HIGH)
    print("Luz 01 ligada")

def ligaLuz02():
    GPIO.output(L_02, GPIO.HIGH)
    print("Luz 02 ligada")

def desligaLuz01():
    GPIO.output(L_01, GPIO.LOW)
    print("Luz 01 desligada")

def desligaLuz02():
    GPIO.output(L_02, GPIO.LOW)
    print("Luz 02 desligada")

# ------------------------------------------------------------------------------------


## funcoes ligar e desligar ar condicionado e projetor
def ligaAC():
    GPIO.output(AC, GPIO.HIGH)
    print("Ar condicionado ligado")

def desligaAC():
    GPIO.output(AC, GPIO.LOW)
    print("Ar condicionado desligado")

def ligaPR():
    GPIO.output(PR, GPIO.HIGH)
    print("Projetor ligado")

def desligaPR():
    GPIO.output(PR, GPIO.LOW)
    print("Projetor desligado")
# ------------------------------------------------------------------------------------
#Funcoes de agrupamento de cargas

def ligaCargas():
    ligaLuz01()
    ligaLuz02()
    ligaAC()
    ligaPR()

def desligaCargas():
    desligaLuz01()
    desligaLuz02()
    desligaAC()
    desligaPR()

def ligaLuzes():
    ligaLuz01()
    ligaLuz02()

def desligaLuzes():
    desligaLuz01()
    desligaLuz02()

# Sistema de alarme
def ligarAlarme():
    global alarme
    if GPIO.input(SJan)==1 or GPIO.input(SPor)==1 or GPIO.input(SPres)==1 or GPIO.input(SFum)==1 or GPIO.input(SC_IN)==1 or GPIO.input(SC_OUT)==1:
        print("Não é possível ligar o sistema de alarme")
        print("Verifique os sensores!")
        data = datetime.datetime.now()
        with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([data, 'Não foi possivel ligar o sistema de alarme, verifique os sensores'])
        alarme = 0
    else:
        data = datetime.datetime.now()
        with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([data, 'alarme ligado'])	
        alarme = 1

def desligarAlarme():
    print("Sistema de larme desligado")
    global alarme
    alarme = 0
    if leituraSensorJan() == 1 or leituraSensorPor() == 1 or leituraSensorPres() == 1:
        ligaLuzes()
        time.sleep(15)
        desligaLuzes()
        



def monitoraFumaca():
    if GPIO.event_detected(SFum):
        print("Fumaça detectada!")
        GPIO.output(AL_BZ, GPIO.HIGH)
        print("Sirene ligada!")

# ------------------------------------------------------------------------------------
         
# CONTADOR DE PESSOAS
def contadorPessoas():
    global pessoas
    global sala
    if sala == 1:
        if GPIO.event_detected(SC_IN):
            pessoas += 1
            servidor_distribuido1.send(bytes(pessoas,"utf8"))
        elif GPIO.event_detected(SC_OUT):
            pessoas+= -1
            servidor_distribuido1.send(bytes(pessoas,"utf8"))
    elif sala == 2:
        if GPIO.event_detected(SC_IN):
            pessoas += 1
            servidor_distribuido2.send(bytes(pessoas,"utf8"))
        elif GPIO.event_detected(SC_OUT):
            pessoas+= -1
            servidor_distribuido2.send(bytes(pessoas,"utf8"))
        

# ------------------------------------------------------------------------------------
def main():
    global alarme
    global sala
    sala = int(input("Esta sala usa configuração 1 ou 2?"))
    configuracao()
    desligarAlarme()
    GPIO.output(AL_BZ, GPIO.LOW)
    while True:

        if sala == 1: 
            msg = conexao1.recv(1024)
            if not msg:
                break
            print("recebido:", msg.decode())
            conexao1.send(msg)

            if msg.decode() == "L01":
                ligaLuz01()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 01 ligada'])
            elif msg.decode() == "DL01":
                desligaLuz01()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 01 desligada'])
            elif msg.decode() == "L02":
                ligaLuz02()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 02 ligada'])
            elif msg.decode() == "DL02":
                desligaLuz02()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 02 desligada'])
            elif msg.decode() == "AC":
                ligaAC()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'AC ligado'])
            elif msg.decode() == "DAC":
                desligaAC()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'AC desligado'])
            elif msg.decode() == "PR":
                ligaPR()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Projetor ligado'])
            elif msg.decode() == "DPR":
                desligaPR()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Projetor desligado'])
            elif msg.decode() == "AL":
                ligarAlarme()
            elif msg.decode() == "DAL":
                desligarAlarme()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Alarme desligado'])
            elif msg.decode() == "L12":
                ligaLuzes()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luzes ligadas'])
            elif msg.decode() == "D12":
                desligaLuzes()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luzes desligadas'])
            elif msg.decode() == "LG":
                ligaCargas()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Cargas ligadas'])
            elif msg.decode() == "DG":
                desligaCargas()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Cargas desligadas'])
            elif msg.decode() == "x":
                servidor_distribuido1.close()
                break
        elif sala == 2:
            msg = conexao2.recv(1024)
            if not msg:
                break
            print("recebido:", msg.decode())
            conexao2.send(msg)

            if msg.decode() == "L01":
                ligaLuz01()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 01 ligada'])
            elif msg.decode() == "DL01":
                desligaLuz01()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 01 desligada'])
            elif msg.decode() == "L02":
                ligaLuz02()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 02 ligada'])
            elif msg.decode() == "DL02":
                desligaLuz02()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luz 02 desligada'])
            elif msg.decode() == "AC":
                ligaAC()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'AC ligado'])
            elif msg.decode() == "DAC":
                desligaAC()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'AC desligado'])
            elif msg.decode() == "PR":
                ligaPR()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Projetor ligado'])
            elif msg.decode() == "DPR":
                desligaPR()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Projetor desligado'])
            elif msg.decode() == "AL":
                ligarAlarme()
            elif msg.decode() == "DAL":
                desligarAlarme()
                data = datetime.datetime.now()
                with open('./logs/log_sala1.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Alarme desligado'])
            elif msg.decode() == "L12":
                ligaLuzes()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luzes ligadas'])
            elif msg.decode() == "D12":
                desligaLuzes()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Luzes desligadas'])
            elif msg.decode() == "LG":
                ligaCargas()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Cargas ligadas'])
            elif msg.decode() == "DG":
                desligaCargas()
                data = datetime.datetime.now()
                with open('./logs/log_sala2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=':' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data, 'Cargas desligadas'])
            elif msg.decode() == "x":
                servidor_distribuido1.close()
                break
        if alarme == 1:
            if leituraSensorJan() == 1 or leituraSensorPor() == 1 or leituraSensorPres() == 1:
                ## INTEGRAR COM O SERVIDOR CENTRAL
                GPIO.output(AL_BZ, GPIO.HIGH)
                print("Sirene ligada!")

if __name__ == "__main__":
    main()



        

    

   
    

    
    


    





