import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


# Configuração das GPIOs

L_01 = 26
L_02 = 19
AC = 13
PR = 6
AL_BZ = 5
SPress = 0
SFum = 11
SJan = 9
SPor = 10
SC_IN = 22
SC_OUT = 27
DHT22 = 18

entrada = "x"
GPIO.setup(L_01, GPIO.OUT)
GPIO.setup(L_02, GPIO.OUT)

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


while(1):
    entrada = input("Digite o comando: ")
    if(entrada == "1"):
        ligaLuz01()

    if(entrada == "2"):
        ligaLuz02()
    
    if(entrada == "3"):
        desligaLuz01()
    
    if(entrada == "4"):
        desligaLuz02()

    if(entrada == "5"):
        break

    





