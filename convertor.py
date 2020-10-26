#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Konatsune
#
# Created:     24/10/2020
# Copyright:   (c) Konatsune 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import warnings

## Depuis la racine de se fichier, cherche le dossier data
def path_to_data():
    # Sortie : X:\.\..\data\
    data_base = os.path.dirname(os.path.realpath(sys.argv[0]))
    sys.path.append(data_base)
    return data_base + "\data\\"

def exploit_file(name):
    # Entrée : exploit.txt
    # Sortie : X:\.\..\midi\exploit.txt
    if(name[-4:] != ".txt"):
        warnings.warn("This file is not a .txt format", ImportWarning)
    else:
        return path_to_data()+name

def lire_exploit_txt(data_file):
    # Entrée : X:\.\..\midi\exploit.txt
    # Sortie : data : [...]
    with open(data_file,'r') as raw_data:
        data = raw_data.readlines()
    return data

# supprime les retours à la ligne et les tabulations
def chaines_clear(tableau_chaines):
    #
    chaines_clear = []
    char_tamp = ""
    for chaine in tableau_chaines:
        chaine = chaine.replace("\n", "")
        chaine = chaine.replace("\t", " ")
        chaines_clear.append(chaine)
    return chaines_clear

def split_tableau(tableau):
    tab = []
    for term in tableau:
        tab.append(term.split(" "))
    return tab

def tableau_conversion(data_file):
    return split_tableau(chaines_clear(lire_exploit_txt(exploit_file(data_file))))

def start():
    data_file = "midi_exploit.txt"
    return tableau_conversion(data_file)

if __name__ == '__main__':
    print("[Debuggage]")
    a = tableau_conversion("midi_exploit.txt")
    #a = lire_exploit_txt(exploit_file("midi_exploit.txt"))
    print("fini")
