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

def start(name="\\default.mid"):
    midi_arduino.start(name)
    return print("Done")

if __name__ == '__main__':
    start()