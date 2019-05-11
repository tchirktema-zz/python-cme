import serial
import time
import os

#declaration du port de l'arduino
arduino = serial.Serial('/dev/ttyUSB0',9600)
#patiente durant 2 second
time.sleep(2)

#lire les informations de arduino
# print(arduino.readline())

print("Entrer 1 pour ON et 0 pour OFF")

while 1:
    choix = input()
    # choix = int(choix)
    if(choix == '1'):
        arduino.write(choix.encode())
        print('LED ROUGE est ON')
        time.sleep(1)
    elif(choix == '0'):
        arduino.write(choix.encode())
        print('LED ROUGE est OFF')
        time.sleep(1)
    else:
        print('Oupss choix invalide')