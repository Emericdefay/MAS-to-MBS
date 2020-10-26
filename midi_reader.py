# Name:        midi_reader.py
#-------------------------------------------------------------------------------
# Purpose:     Gérer la lecture et la conversion en tableau [[note,temps],[note,temps],...] du fichier midi
#
# Author:      emericdefay
#
# Created:     22/10/2020
#-------------------------------------------------------------------------------

#Importations:
import os
import sys
import warnings

# Appelles des fonctions:
"""
INTERNE:
reader(midi_file)
path_to_midi()
midi_file(name)
midi_convertor(tableau)

EXTERNE:

start(name)
# Sortie : piste_midi, Tempo, Duree_noire
"""

# Definitions:

## Lit le fichier midi et le converti en un tableau [hex,hex,...]
def reader(midi_file):
    # Entrée : Fichier.mid
    # Sortie : [hex,hex,...]
    with open(midi_file,"rb") as raw_midi:
        hexa_midi = ["{:02x}".format(c) for c in raw_midi.read()]
    return hexa_midi

## Depuis la racine de se fichier, cherche le dossier midi
def path_to_midi():
    # Sortie : X:\.\..\midi\
    midi_base = os.path.dirname(os.path.realpath(sys.argv[0]))
    sys.path.append(midi_base)
    return midi_base + "\midi\\"

def midi_file(name):
    # Entrée : fichier_midi.mid
    # Sortie : X:\.\..\midi\fichier_midi.mid
    if(name[-4:] != ".mid"):
        warnings.warn("This file is not a .mid format", ImportWarning)
    else:
        return path_to_midi()+name

def conv_hexTab_to_int(tableau):
    # Entrée : [hex,hex,...] en str
    # Sortie : int
    conv = "0x"
    for k in range(len(tableau)):
        conv += tableau[k]
    conv = int(conv,16)
    return conv

def midi_convertor(tableau):
    # voir site : http://manivelles.occitanes.pagesperso-orange.fr/site-arrangements/Solfege/Fichiers-midi2.html
    # Entrée : Tableau [hex,hex,hex,...]
    # Sortie : tableau [[note,durée],[note,durée],...]

    index_pistes = [[],[]]
    piste_midi = []
    tempo_hex = []
    tempo = 0

    debut_piste = 0
    fin_piste = 0

    #Acquisition des meta données
    for k in range(len(tableau)-3):
        if (tableau[k:k+4] == ["4d","54","72","6b"]):
            # Début du bloc de la piste
            debut_piste = k
            index_pistes[0].append(k)

        if (tableau[k:k+4] == ["00","ff","2f","00"]) and (debut_piste != 0):
            # Fin du bloc de la piste
            fin_piste = k
            index_pistes[1].append(k)

        if (tableau[k:k+3] == ["ff","51","03"]):
            # Tempo k4 k5 k6 = duree d'une noire en ms : 60,000,000 /'k4'+'k5'+'k6' = BPM
            tempo_hex.append(tableau[k+3])
            tempo_hex.append(tableau[k+4])
            tempo_hex.append(tableau[k+5])
            #print(tempo_hex)
            #print(conv_hexTab_to_int(tempo_hex))
            tempo = int(60000000/conv_hexTab_to_int(tempo_hex))
            #print("BPM : "+str(tempo)) #DEBUG

    # Vérifications du fichier midi.
    if len(index_pistes[0])> 3 or len(index_pistes[0])!=len(index_pistes[1]):
        print("\tAttention : ",end="")
        if len(index_pistes[0]) > 3:
            # Trop de pistes, pas imprimable.
            print("Plus d'une piste MIDI.")
        elif len(index_pistes[0]) != len(index_pistes[1]):
            # Fichier endommagé ou mal lu.
            print("Fichier corrompu.")

    #print(index_pistes) #DEBUG

    # Acquisition de la piste UNIQUE.
    if(len(index_pistes[0])==len(index_pistes[1])==3):
        for k in range(index_pistes[0][-1]+4,index_pistes[1][-1]):
            piste_midi.append(tableau[k])
        #print(piste_midi) #DEBUG

    duree_noire = conv_hexTab_to_int(tempo_hex)

    #retourne la piste et le tempo
    return piste_midi,tempo, duree_noire


#Utilisation:

def start(name):
    return midi_convertor(reader(midi_file(name)))

if __name__ == "__main__":
    print("[Debuggage]\n\n")
    a = start("default.mid")
    print("fini")



