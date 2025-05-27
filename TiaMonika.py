import sys
import time
from time import sleep

def lagu() :
    lirik = [
        ("\r\nTimbul cinta lam dada",0.08),
        ("Pada padangan pertama",0.08),
        ("Dari itulah aku terlena\r\n",0.08),
        ("Owh dek",0.08),
        ("Tia Monika",0.08),
        ("Apakah mau jadi",0.08),
        ("Pacar kanda\r\n",0.08),
        ("Owh dek",0.08),
        ("Tia Monika",0.08),
        ("Membuat dirimu",0.08),
        ("Tergila - gilaaaa\r\n",0.08)
    ]

    jeda = [
        0.2,
        0.2, 
        1.5, 
        0.2,
        0.4,
        0.2,
        0.4,
        0.2,
        0.4,
        0.2,
        0.8
    ]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(jeda[i])
        print('')

if __name__ == '__main__' :
    lagu()