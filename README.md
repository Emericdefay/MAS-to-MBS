# MAS-to-MBS
Transform MIDI file into Arduino Script to print on Music Box Sheet.

## Todo

- [ ] Change the arduino program construction : Make a serial reader  
- [ ] Describe the modules, never enough description  
- [ ] Optimize the arduino matricial usage, reducing the memory sued
- [ ] Add the printer montage  
- [ ] Add pictures  

## Requirements
You have to get some stuff to make the printer but if you just want to get
the coordinates for your own Music Paper Sheet you just need to launch the program and use matrice_%midiFileName%.txt.<br/>
Stuff required:
- Arduino (Mega or another with enough storage to store the amout of bytes)
- A Shield CNC with 3 motor drivers (for Nema 17)
- 3x Nema 17
- The gear of your printer : You need to make the rollerbank, the head and the puncher. With that, you need to defined the parameters in you .ino file. Look at ""The .ino script" Section.
- Midi files : There is already one file ("default.mid") but if you want to put yours, you have to be aware of the range. Look at the "Notes Range" Section.

## The program

##### How to use it?
###### If you want to see a partition by default.
> Type: `$ python MAS2MBS.py`.<br/><br/>
It create :  
- A .txt file that can be open in Excel to see the print map named : "matrice_%midiFileName%.txt"
- An Arduino's script : "script_arduino.ino" in arduino/
<br/>
Then compile the script_arduino.ino on an Arduino and it will print. Make sure to get the requirements.

###### If you want to make your own partition
> Put your Midi file on /midi. Launch MAS2MBS.py from an IDLE,  at the line 20, write start("%YourMidiFileName%.mid") and compile.<br/><br/>
It create :  
- A .txt file that can be open in Excel to see the print map named : "matrice_%midiFileName%.txt"
- An Arduino's script : "script_arduino.ino" in arduino/
<br/>
Then compile the script_arduino.ino on an Arduino and it will print. Make sure to get the requirements.

## The .ino script
You can change some values (I named few of them) to set your printer.

__Steppers'Variables:__ <br/>
- stps : Value that change the rotation of your rollerBankMotor
- stps2mm : Value that change the rotation of your headPrinterMotor
- stps1turn : Value that change the rotation of your pincherMotor

__Delays'Variables:__ <br/>
- delayBetweenActions : Value that change the time between each motor's action
- delayTime : Value that change the speed of your motors

## Notes Range
If you look at your Music Box's Sheet, you can see the range of the notes :<br/>
> C,D,G,A,B,C1,D1,E1,F1,F1#,G1,G1#,A1,A1#,B1,C2,C2#,D2,D2#,E2,F2,F2#,G2,G2#,A2,A2#,B2,C3,D3,E3<br/>

Well, creating music at those octaves is misleading and poor so I adapted it.
If you want to print your .mid file, its notes has to be in:<br/>
> C2,D2,G2,A2,B2,C3,D3,E3,F3,F3#,G3,G3#,A3,A3#,B3,C4,C4#,D4,D4#,E4,F4,F4#,G4,G4#,A4,A4#,B4,C5,D5,E5<br/>

I could convert the notes from other octaves but it could figure a bad quality sheet. 
