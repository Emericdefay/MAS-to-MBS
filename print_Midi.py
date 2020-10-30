#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Konatsune
#
# Created:     29/10/2020
# Copyright:   (c) Konatsune 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Librairies
from serial import *
import exploit
import time

# Port série COM4
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
def printing(liste=[(0) for val in range(30)]):
    print(liste)
    compteur = 0
    with Serial(port="COM3", baudrate=19200, timeout=0.1, writeTimeout=0.1) as port_serie:
        if port_serie.isOpen():
            #port_serie.write("0".encode())

            while True:
                note = 0
                #port_serie.write("0".encode())
                time.sleep(1)
                if b'9' in port_serie.readline(port_serie.inWaiting()):
                    while (b'2' not in port_serie.readline(port_serie.inWaiting())):
                        #a = (port_serie.readline(port_serie.inWaiting()))
                        #print(a)

                        if(b'1' in port_serie.readline()):
                            print("note : "+str(note),end="")
                            if liste[note] == 0:
                                port_serie.write(bytes(1))
                                print(" - percée.")
                            else:
                                port_serie.write(bytes(0))
                                print(" - indemne.")

                            note += 1

                            if note > len(liste)-1:
                                print("bout de colone.")
                                break

                        #a = (port_serie.readline())
                        #port_serie.write("1".encode())
                        #port_serie.read()

                        #print(a.decode())
                    a = (port_serie.readline())
                    print(a,note)
                    print("Liste terminée")
                    compteur += 1
                    port_serie.write(0b11001000)

                break
        pass

def start(name="default.mid"):
    pass
if __name__ == '__main__':
    printing()