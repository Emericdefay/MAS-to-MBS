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

# Port série :
# Vitesse de baud : 115200
# Timeout en lecture : 0.5 sec
# Timeout en écriture : 0.02 sec
def printingLap(liste=[1 for val in range(30)],arduino_COM="COM3",lap=1,allLaps=1):
    """  """
    #print(liste) DEBUGGAGE
    with Serial(port=arduino_COM, baudrate=115200, timeout=0.2, writeTimeout=0.02) as port_serie:
        if port_serie.isOpen():
            attempt = 0
            while True:
                attempt += 1

                port_serie.write('2'.encode('utf-8'))
                print("Launching lap n°{} - Waiting Arduino information - Request n°{}...".format(lap,attempt))

                time.sleep(1)
                if b'9' in port_serie.readline(port_serie.inWaiting()):
                    print("Start printing Lap n°{}".format(lap))

                    while (b'4' not in port_serie.readline(port_serie.inWaiting())):

                        note = 0
                        while (b'2' not in port_serie.readline(port_serie.inWaiting())):

                            if(b'3' in (port_serie.readline())):
                                if liste[note] == 1:
                                    port_serie.write('1'.encode('utf-8'))
                                    port_serie.readline()
                                else:
                                    port_serie.write('0'.encode('utf-8'))

                                if note > len(liste):
                                    print("Lap done : Waiting for next Lap...")
                                    break

                            if(b'1' in (port_serie.readline())):
                                print("Lap n°{}/{}-[{:02};{}]".format(lap,allLaps,note+1,liste[note]))
                                note += 1
                            if(b'2' in (port_serie.readline()) or note == len(liste)):
                                break

                        note = 0
                        break

                    break
    pass

def start(name="default.mid",arduino_COM="COM3",warningMsg=True):
    """ name : MidiFileName.mid
    arduino_COM : The port of your arduino.
    warningMsg : False/True. If true, remember the user to upload 'serialReaderPrinter.ino' on arduino board. """
    if warningMsg:
        print("Remember to upload 'serialReaderPrinter.ino' on your arduino board.")
        print("This warning will stay 20 seconds. To make sure that you have the time to check.")
        print("You can disable this reminder : start('MidiFileName.mid',False)")
        time.sleep(20)

    liste = exploit.start(name,False)
    print("Start to print : {} - Amount of laps : {}.".format(name,len(liste)))
    print("Average time : {} min.".format(int((10*len(liste))/60)))
    time.sleep(2)
    for k in range(len(liste)):
        printingLap(liste[k],arduino_COM,k+1,len(liste))
    Return ("Printing done.")

if __name__ == '__main__':
    #Debugging
    #printingLap(liste=[1 for val in range(30)],arduino_COM="COM3",lap=1,allLaps=1) # Use it to debug.
    start("default.mid","COM3",False) # Use it to start you printing project.