# MAS-to-MBS
Transform MIDI file into Arduino Script to print on Music Box Sheet

Use MAS2MBS.py
# Requirements
You have to get some stuff to make the printer but if you just want to get
the coordinates for your own Music Paper Sheet you just need to launch a special command.
Stuff required:
- Arduino (Mega or another with enough storage to store the amout of bytes)
- A Shield CNC with 3 motor drivers (for Nema 17)
- 3 Nema 17
- The gear of your printer : You need to make the rollerbank, the head and the puncher. With that, you need to defined the parameters in you .ino file (stps, stps2mm & stps1turn).
- Midi files : There is already one file ("default.mid") but if you want to put yours, you have to be aware of the range. Look at the "Notes Range" Section.

# The program

Type: <br/>`$ python MAS2MBS.py`.
It create :
- A .txt file that can be open in Excel to see the print map named : "matrice_%midiFileName%.txt"
- An Arduino's script : "script_arduino.ino" in arduino/

# The .ino script
You can change some values (I named few of them) to set your printer.
Steppers'Variables:
- stps : Value that change the rotation of your rollerBankMotor
- stps2mm : Value that change the rotation of your headPrinterMotor
- stps1turn : Value that change the rotation of your pincherMotor
Delays' Variables:
- delayBetweenActions : Value that change the time between each motor's action
- delayTime : Value that change the speed of your motors

# Notes Range
