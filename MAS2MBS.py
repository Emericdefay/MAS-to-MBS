#-------------------------------------------------------------------------------
# Name:        MAS2MBS.py
# Purpose:
#
# Author:      emericdefay
#
# Created:     22/10/2020
#-------------------------------------------------------------------------------

#Importations:
import midi_arduino
import serialSender
import serialReaderMaker
import serial
import sys

def createScript(name="default.mid"):
    try:
        print("Program launched :")
        print("\tOpen : " + name)
        midi_arduino.start(name)
        print("\tFile : script_arduino.ino : Created on /arduino/script_arduino/")
        print("Program done.\n")
        print("If the script_arduino.ino is to much for your arduino board, use createSerialMaker()")
        pass
    except FileNotFoundError:
        print("The file {} doesn't exist.".format(name))
        pass

def createSerialMaker(name="default.mid",arduino_COM="COM3",warningMsg=True):
    print("Using Serial method :\n")
    serialReaderMaker.start()
    try:
        serialSender.start(name,arduino_COM,warningMsg)
        pass
    except serial.serialutil.SerialException:
        print("Not the arduino_COM.")
        pass
    except KeyboardInterrupt:
        print("Abort the program.")
        pass
    except FileNotFoundError:
        print("The file {} doesn't exist.".format(name))
        pass

if __name__ == '__main__':
    #createScript("default.mid") #Create the script_arduino.ino
    #createSerialMaker("default.mid","COM3",True) # Use Serial Method, when storage of board is not enough.
    pass