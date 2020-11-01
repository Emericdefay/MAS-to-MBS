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

def createScript(name="default.mid"):
    print("Program launched :")
    print("\tOpen : " + name)
    midi_arduino.start(name)
    print("\tFile : script_arduino.ino : Created on /arduino/script_arduino/")
    print("Program done.\n")
    return print("If the script_arduino.ino is to much for your arduino board, use createSerialMaker()")

def createSerialMaker(name="default.mid",arduino_COM="COM3",warningMsg=True):
    print("Using Serial method.")
    serialReaderMaker.start()
    try:
        serialSender.start(name,arduino_COM,warningMsg)
    except serial.serialutil.SerialException:
        print("Not the arduino_COM.")
        pass

if __name__ == '__main__':
    #createScript() #Create the script_arduino.ino
    createSerialMaker("default.mid","COM3",False) # Use Serial Method, when storage of board is not enough.