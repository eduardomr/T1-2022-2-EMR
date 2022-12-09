import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


# Configuração das GPIOs

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

entrada = "x"

GPIO.setup(L_01, GPIO.OUT)
GPIO.setup(L_02, GPIO.OUT)
GPIO.setup(AC, GPIO.OUT)
GPIO.setup(PR, GPIO.OUT)


GPIO.setup(SJan, GPIO.IN)
GPIO.setup(SPres, GPIO.IN)
GPIO.setup(SFum, GPIO.IN)
GPIO.setup(SPor, GPIO.IN)
GPIO.setup(SC_IN, GPIO.IN)
GPIO.setup(SC_OUT, GPIO.IN)

## Funções de leitura dos sensores
GPIO.add_event_detect(SJan, GPIO.BOTH)
def leituraSensorJan():
    if GPIO.event_detected(SJan):
        if GPIO.input(SJan)==1:
            print("Sensor da janela ativado!")
        else:
            print("Sensor da janela desativado!")

GPIO.add_event_detect(SPor, GPIO.BOTH)
def leituraSensorPor():
    if GPIO.event_detected(SPor):
        if GPIO.input(SPor)==1:
            print("Sensor da porta ativado!")
        else:
            print("Sensor da porta desativado!")

GPIO.add_event_detect(SPres, GPIO.BOTH)
def leituraSensorPres():
    if GPIO.event_detected(SPres):
        if GPIO.input(SPres)==1:
            print("Sensor de presença ativado!")
        else:
            print("Sensor de presença desativado!")






## Ligar e desligar luzes
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



## Ligar e desligar ar condicionado e projetor
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

##



while(1):
    leituraSensorJan()
    leituraSensorPor()
    leituraSensorPres()

    
    


    





