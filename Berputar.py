import sys
import time
from time import sleep

def lagu() :
    lirik = [
        ("\r\nAku bingung sendiri",0.09),
        ("Melihat mu begini",0.09),
        ("Kau buat aku jadi pusingg",0.09),
        ("Aku tau maumu",0.10),
        ("Aku tau maksudmu",0.10),
        ("Aku mau jawaban",0.10),
        ("Cukup satu jawabann",0.09),
        ("Ahhhhhhhh ok Ahhhhhhhhh ok",0.20),
    ]

    jeda = [
        0.3,
        0.3,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.3,
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