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
"//Code generate by the script MAS2MBS.",
"",
"#define EN 8",
"",
"//Direction pin",
"#define X_DIR 5 // rollerBankMotor",
"#define Y_DIR 6 // headprinterMotor",
"#define Z_DIR 7 // puncherMotor",
"",
"//Step pin",
"#define X_STP 2 // rollerBankMotor",
"#define Y_STP 3 // headprinterMotor",
"#define Z_STP 4 // puncherMotor",
"",
"///////////////////////////////////////////////////////////////",
"//                        MODIFIE                            //",
"// Steppers' Variables :",
"int stps=200;// Steps to move the rollerBankMotor",
"int stps2mm=200;// Steps to move headprinterMotor",
"int stps1turn=200; // Steps to do 1 turn on the puncherMotor",
"//",
"//Delays' Variables :",
"int delayBetweenActions = 100; // Delay between each steps.",
"int delayTime=350; // Speed of the Motors [350:8000]",
"//                                                           //",
"///////////////////////////////////////////////////////////////",
"",
"// Do not change",
"bool done = 0;"
]

# Deuxieme partie STATIQUE du code arduino.
deuxiemePartieDuCode = [
"};",
"",
"void step(boolean dir, byte dirPin, byte stepperPin, int steps){",
"  digitalWrite(dirPin, dir);",
"  delay(delayBetweenActions);",
"  for (int i = 0; i < steps; i++) {",
"    digitalWrite(stepperPin, HIGH);",
"    delayMicroseconds(delayTime);",
"    digitalWrite(stepperPin, LOW);",
"    delayMicroseconds(delayTime);",
"  }",
"}",
"",
"void setup(){",
"  pinMode(X_DIR, OUTPUT); pinMode(X_STP, OUTPUT);",
"  pinMode(Y_DIR, OUTPUT); pinMode(Y_STP, OUTPUT);",
"  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);",
"  pinMode(EN, OUTPUT);",
"  digitalWrite(EN, LOW);",
"}",
"",
"void printing(){",
"  // Read the matrice column by column.",
"  for (int i = 0; i < numberColumns;i++) {",
"    // Read the current column : note by note.",
"    for(int j = 0; j < numberNotes;j++){",
"      // Move the headprinter.",
"      step(false, Y_DIR, Y_STP, stps2mm); // Move by %stps2mm% steps.",
"",
"      // If there is a note on the current column : Perforate.",
"      if(matriceMidi[i][j]==1){",
"        step(false, Z_DIR, Z_STP, stps1turn); // PuncherMotor 1 turn",
"      }",
"    }",
"    // Move the headprinter to the default location.",
"    step(true, Y_DIR, Y_STP, numberNotes*stps2mm);",
"",
"",
"    // Move the rollerBank at the next column.",
"    step(false, X_DIR, X_STP, stps);",
"  }",
"}",
"",
"void loop(){",
"  if(done == false){",
"    printing();",
"    done = true;",
"  }",
"  delay(10000);",
"}"
]


def writingStaticElement(liste,chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino\\script_arduino.ino"):
    """ Ecris du texte à partir d'une liste de chaines dans le fichier donné. """
    with open(chemin, 'a') as writing:
        for ligne in liste:
            writing.write(ligne)
            writing.write("\n")
        writing.write("\n")
    pass

def writingDynamicElement(texte,chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino\\script_arduino.ino"):
    """ Permet d'écrire du texte dans un fichier donné. """
    with open(chemin, 'a') as writing:
        writing.write(texte)
        writing.write("\n")
    pass

def writingListElement(liste,chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino\\script_arduino.ino"):
    """ Ecrit des éléments d'une liste - Non réutilisable en l'état.
    N'a qu'un seul but : écrire les données Midi dans Arduino sous la forme :
    {{0,1,0},{1,1,0},{0,0,0},...}"""
    with open(chemin, 'a') as writing:
        for j in range(len(liste)):
            writing.write("{")
            for k in range(len(liste[j])):
                writing.write(str(liste[j][k]))
                if not k == len(liste[j])-1:
                    writing.write(",")
            writing.write("}")
            if not j == len(liste)-1:
                writing.write(",")
            writing.write("\n")

def resetElement(chemin=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino\\script_arduino.ino"):
    """ Permet d'effacer le contenue d'un fichier.
    Pour ensuite réécrire du contenue sur un fichier vierge."""
    if os.path.exists(os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino"):
        print("\tBuffer : Folder '{}' exist in {}".format("script_arduino",os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\"))

        with open(chemin, 'w') as writing:
            writing.write("")
        print("\tFile : script_arduino.ino : Reset")

    else:
        os.mkdir(os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"+"arduino\\script_arduino")
        print("\tBuffer : Folder '{}' doesn't exist in {}. : Created".format("script_arduino",os.path.dirname(os.path.realpath(sys.argv[0]))))
        resetElement(chemin)



def start(name="default.mid"):
    """ Ecrit le script Arduino à partir des elements de la matrice et des lignes de codes Arduino pré-établis. """
    matrice = exploit.start(name)
    resetElement()
    writingStaticElement(premierePartieDuCode)
    writingDynamicElement("int numberColumns = {};".format(len(matrice)))
    writingDynamicElement("int numberNotes = {};".format(len(matrice[0])))
    writingDynamicElement("\n")
    writingDynamicElement("// List")
    writingDynamicElement("bool matriceMidi[][{}] = {}".format(len(matrice[0]),"{"))
    writingListElement(matrice)
    writingStaticElement(deuxiemePartieDuCode)

if __name__ == '__main__':
    # Debuggage.
    start()
