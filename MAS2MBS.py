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

def start(name="default.mid"):
    print("Program launched :")
    print("\tOpen : " + name)
    midi_arduino.start(name)
    print("\tFile : script_arduino.ino : Created on /arduino/script_arduino/")
    return print("Program done.")

if __name__ == '__main__':
    start()