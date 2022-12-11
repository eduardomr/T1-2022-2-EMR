import RPi.GPIO as GPIO
from socket import *

host = '127.0.0.1'
port = 5000
servidor_distribuido = socket(AF_INET, SOCK_STREAM)
servidor_distribuido.bind((host, port))
servidor_distribuido.listen()
conexao, docliente = servidor_distribuido.accept()



GPIO.setmode(GPIO.BCM)


# Configuração das pinos GPIOs------------------------------------------------------
L_01 = 26
L_02 = 19
AC = 13
PR = 6
AL_BZ = 5
SPres = 0
SFum = 11
SJan = 9
SPor = 10
SC_IN = 22
SC_OUT = 27
DHT22 = 18
# ------------------------------------------------------------------------------------

# Configuração dos pinos GPIOs (SAIDA/ENTRADA)

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


# Configuração dos pinos GPIOs (DETECÇÃO DE EVENTOS)
GPIO.add_event_detect(SJan, GPIO.BOTH)
GPIO.add_event_detect(SPor, GPIO.BOTH)
GPIO.add_event_detect(SPres, GPIO.BOTH)
GPIO.add_event_detect(SFum, GPIO.RISING)
GPIO.add_event_detect(SC_IN, GPIO.RISING)
GPIO.add_event_detect(SC_OUT, GPIO.RISING)
# ------------------------------------------------------------------------------------


# funções de leitura dos sensores
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




## Funções Ligar e desligar luzes
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


## funções ligar e desligar ar condicionado e projetor
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


# Sistema de alarme
def ligarAlarme():
    ## ANTES DE LIGAR, VERIFICAR SE HÁ ALGUM SENSOR ATIVADO
    if leituraSensorJan() == 1 or leituraSensorPor() == 1 or leituraSensorPres() == 1:
        ## INTEGRAR COM O SERVIDOR CENTRAL
        GPIO.output(AL_BZ, GPIO.HIGH)
        print("Sirene ligada!")

def monitoraFumaca():
    if GPIO.event_detected(SFum):
        print("Fumaça detectada!")
        GPIO.output(AL_BZ, GPIO.HIGH)
        print("Sirene ligada!")

# ------------------------------------------------------------------------------------
         
# CONTADOR DE PESSOAS
pessoas = 0
def contadorPessoas():
    global pessoas
    if GPIO.event_detected(SC_IN):
        pessoas = pessoas + 1
        print(pessoas)
    elif GPIO.event_detected(SC_OUT):
        pessoas = pessoas -1
        print(pessoas)

# ------------------------------------------------------------------------------------

while(1):
    msg = conexao.recv(1024)
    if not msg:
        break
    print("recebido:", msg.decode())
    conexao.send(msg)

    if msg.decode() == "l1":
        ligaLuz01()
    elif msg.decode() == "dl1":
        desligaLuz01()
    elif msg.decode() == "l2":
        ligaLuz02()
    elif msg.decode() == "dl2":
        desligaLuz02()
    elif msg.decode() == "lac":
        ligaAC()
    elif msg.decode() == "dlac":
        desligaAC()
    elif msg.decode() == "lp":
        ligaPR()
    elif msg.decode() == "dlp":
        desligaPR()
    elif msg.decode() == "x":
        tcp.close()
        break

   
    

    
    


    





