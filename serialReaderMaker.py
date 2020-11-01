#-------------------------------------------------------------------------------
# Name:        MAS2MBS.py
# Purpose:
#
# Author:      emericdefay
#
# Created:     22/10/2020
#-------------------------------------------------------------------------------

#Importations:

import os
import sys
import warnings
import exploit

# #
# Transcription en language Arduino. (90%)
# #

# Premiere partie STATIQUE du code arduino.
premierePartieDuCode = [
"/////////////////////////////////////////////////////////////////////////////////",
"//                                                                             //",
"//                               Print with Python.                            //",
"//                                                                             //",
"/////////////////////////////////////////////////////////////////////////////////",
"//                                                                             //",
"//            Use it if your Arduino is out of memory in your project.         //",
"//                            Still in development.                            //",
"/////////////////////////////////////////////////////////////////////////////////",
"",
"#define EN 8",
"",
"// Direction pin",
"#define X_DIR 5 // rollerBankMotor",
"#define Y_DIR 6 // headprinterMotor",
"#define Z_DIR 7 // perforationMotor",
"",
"// Step pin",
"#define X_STP 2 // rollerBankMotor",
"#define Y_STP 3 // headprinterMotor",
"#define Z_STP 4 // perforationMotor",
"",
"/////////////////////////////////////////////////////////////////////////////////",
"//                                   EDITED                                    //",
"// Steppers' Variables :",
"int stps = 200; // Steps to move the base",
"int stps2mm = 200; // Steps to move between lines",
"int stps1turn = 200; // Steps to do 1 turn.",
"//",
"//////",
"//",
"// Delays' Variables :",
"int delayBetweenActions = 100; // Delay between each steps.",
"int delayTime = 500; // Speed of the Motors [350:8000]",
"//                                                                             //",
"/////////////////////////////////////////////////////////////////////////////////",
"",
"// DO NOT CHANGE :",
"bool done = 0;",
"int note;",
"int numberNotes = 30;",
"byte ref = (byte)0;",
"int noteMidi = 0;",
"",
"",
"//Function that drive the motors.",
"void step(boolean dir, byte dirPin, byte stepperPin, int steps)",
"{",
"  digitalWrite(dirPin, dir);",
"  delay(delayBetweenActions);",
"",
"  for (int i = 0; i < steps; i++)",
"  {",
"    digitalWrite(stepperPin, HIGH);",
"    delayMicroseconds(delayTime);",
"    digitalWrite(stepperPin, LOW);",
"    delayMicroseconds(delayTime);",
"  }",
"}",
"",
"// Init.",
"void setup()",
"{",
"  Serial.begin(115200);",
"  pinMode(X_DIR, OUTPUT); pinMode(X_STP, OUTPUT);",
"  pinMode(Y_DIR, OUTPUT); pinMode(Y_STP, OUTPUT);",
"  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);",
"  pinMode(EN, OUTPUT)   ; digitalWrite(EN, LOW);",
"  pinMode(LED_BUILTIN, OUTPUT);",
"}",
"",
"// Printer function.",
"void printing()",
"{",
"  while((byte)Serial.read() ==(byte)255)",
"  {",
"  digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); //Standby.",
"  delay(500); // Wait Python commands.",
"  }",
"",
"  digitalWrite(LED_BUILTIN, LOW);",
"",
'  Serial.println("9999"); // Send to python : Ready to read datas.',
"",
"    delay(100);",
"    while(note < 30)",
"    {",
"      delay(2);",
'      Serial.println("3333"); // Send to python : Listening.',
"      delay(2);",
"      if((byte)Serial.read() == (byte)49)",
"      {",
"        {",
"          note++;",
"          noteMidi =  1;",
"",
"          delay(1);",
'          Serial.println("1111");// Send to python : note done, send me another.',
"          delay(1);",
"        }",
"        // Punch.",
"        step(false, Z_DIR, Z_STP, stps1turn); // PerforationMotor 1 turn",
"        delay(1);",
"       // Move the headprinter.",
"        step(false, Y_DIR, Y_STP, stps2mm); // Move by %stps2mm% steps.",
"        delay(1);",
"      }",
"",
"      delay(1);",
"",
"      if((byte)Serial.read() == (byte)48)",
"      {",
"        {",
"          note++;",
"          noteMidi =  0;",
"",
"          delay(1);",
'          Serial.println("1111");// Send to python : note done, send me another.',
"          delay(1);",
"        }",
"          // Move the headprinter.",
"          step(false, Y_DIR, Y_STP, stps2mm); // Move by %stps2mm% steps.",
"      }",
"    }",
"",
"  delay(1);",
'  Serial.println("2222"); // Send to python : column done, send me another',
"  delay(1);",
"",
"  // Move the headprinter to the default location.",
"  step(true, Y_DIR, Y_STP, numberNotes*stps2mm);",
"",
"  // Move the rollerBank at the next column.",
"  step(false, X_DIR, X_STP, stps);",
"",
"  delay(1);",
'  Serial.println("2222"); // Send to python : column done, send me another. Echoe.',
"  delay(1);",
"}",
"",
"void loop()",
"{",
"  printing();",
"  delay(100);",
"}",
"",
]


def writingStaticElement(liste,chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\serialReaderPrinter\\serialReaderPrinter.ino"):
    """ Ecris du texte à partir d'une liste de chaines dans le fichier donné. """
    with open(chemin, 'a') as writing:
        for ligne in liste:
            writing.write(ligne)
            writing.write("\n")
        writing.write("\n")
    pass

def writingDynamicElement(texte,chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\serialReaderPrinter\\serialReaderPrinter.ino"):
    """ Permet d'écrire du texte dans un fichier donné.
    Not use here. (for now) """
    with open(chemin, 'a') as writing:
        writing.write(texte)
        writing.write("\n")
    pass


def resetElement(chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\serialReaderPrinter\\serialReaderPrinter.ino"):
    """ Permet d'effacer le contenue d'un fichier.
    Pour ensuite réécrire du contenue sur un fichier vierge."""
    if os.path.exists(os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\serialReaderPrinter"):
        print("\tBuffer : Folder '{}' exist in {}".format("serialReaderPrinter",os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\"))

        with open(chemin, 'w') as writing:
            writing.write("")
        print("\tFile : serialReaderPrinter.ino : Reset")

    else:
        os.mkdir(os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\serialReaderPrinter")
        print("\tBuffer : Folder '{}' doesn't exist in {}. : Created".format("script_arduino",os.path.dirname(os.path.realpath(sys.argv[0]))))
        resetElement(chemin)



def start():
    """ Ecrit le script Arduino à partir des lignes de codes Arduino pré-établis. """
    resetElement()
    writingStaticElement(premierePartieDuCode)


if __name__ == '__main__':
    # Debuggage.
    start()
