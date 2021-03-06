# MAS-to-MBS
Transform MIDI file into Arduino Script to print on Music Box Sheet.<br/>
![HIW_Diagram](https://github.com/Emericdefay/MAS-to-MBS/blob/main/HIW_Diagram.png?raw=true)

## Todo

- [x] Change the arduino program construction : Make a serial reader -> serialSender.py
- [ ] Describe the modules, never enough description  (70%)
- [ ] Optimize the arduino matricial usage, reducing the memory used - On it.
- [ ] Add the printer montage - Still in construction.
- [ ] Add pictures - Will do with printer done.

## Requirements
You have to get some stuff to make the printer but if you just want to get
the coordinates for your own Music Paper Sheet you just need to launch the program and use matrice_%midiFileName%.txt.<br/>
### Stuff required to print :
- Arduino (**Mega** or another with enough storage to store the amout of bytes and enough processor ressources.)
- A Shield CNC with 3 motor drivers (for Nema 17) - I use 3x DRV8825 on a CH340 CNC Shield.
- 3x Nema 17
- The gear of your printer : You need to make the rollerbank, the head and the puncher. With that, you need to defined the parameters in you .ino file. Look at ""The .ino script" Section.
- Midi files : There is already one file ("default.mid") but if you want to put yours, you have to be aware of the range. Look at the "Notes Range" Section.

## The program

### How to use it?
Use your commands line you be in the root of the MAS-to-MBS file.
#### If your Arduino board has enough space (or if you just wanna create the map):
> Type: `$ python -c 'import MAS2MBS; MAS2MBS.createScript("%YourMidiFileName%.mid")'`.<br/>  

It creates :  
- A .txt file that can be open in Excel to see the print map named : "matrice_default.txt"
- An Arduino's script : "script_arduino.ino" in arduino/
<br/>
Then compile the script_arduino.ino on an Arduino and it will print. Make sure to get the requirements.

#### If your board doesn't have enough space :
You need to install pySerial : `pip install pyserial`<br/>
> Type: `$ python -c 'import serialReaderMaker; serialReaderMaker.start()'`.<br/>

It creates :  
- An Arduino's script : "serialReaderPrinter.ino" in arduino/
<br/>
Then compile the serialReaderPrinter.ino on your Arduino and then <br/><br/> 

> type: `$ python -c 'import MAS2MBS; MAS2MBS.createSerialMaker("%YourMidiFileName%.mid","%ArduinoPORT%",True)'`.<br/>

It will communicate with your arduino and sends notes one by one. This method is still in developpement. (Work)<br/> 
Make sure to get the requirements.<br/><br/>
**I invite you to use an IDLE to control it and look at the functions.**

## The .ino scripts
You can change some values to set your printer :

__Steppers Variables:__ <br/>
- stps : Value that changes the rotation of your rollerBankMotor
- stps2mm : Value that changes the rotation of your headPrinterMotor
- stps1turn : Value that changse the rotation of your pincherMotor

__Delays Variables:__ <br/>
- delayBetweenActions : Value that changes the time between each motor action
- delayTime : Value that changes the speed of your motors

## Notes Range
If you look at your Music Box's Sheet, you can see the range of the notes :<br/>
> C,D,G,A,B,C1,D1,E1,F1,F1#,G1,G1#,A1,A1#,B1,C2,C2#,D2,D2#,E2,F2,F2#,G2,G2#,A2,A2#,B2,C3,D3,E3<br/>

Well, creating music at those octaves is misleading and poor so I adapted it.
If you want to print your .mid file, its notes have to be in:<br/>
> C2,D2,G2,A2,B2,C3,D3,E3,F3,F3#,G3,G3#,A3,A3#,B3,C4,C4#,D4,D4#,E4,F4,F4#,G4,G4#,A4,A4#,B4,C5,D5,E5<br/>

I could convert the notes from other octaves but it could figure a bad quality sheet. 
