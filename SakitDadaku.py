import sys
from time import sleep
import time

def lagu() :
    lirik = [
        ("\r\nSakit dadaku",0.09),
        ("Ku mulai merindu",0.09),
        ("Ku bayangkan jika kamu tidur disampingku",0.09),
        ("Di malam yang semu",0.09),
        ("Pejamkan mataku",0.09),
        ("Ku bayangkan tubuhmu jika di pelukanku\r\n",0.09),
        #2
        ("\r\nSakit dadaku",0.09),
        ("Ku mulai merindu",0.09),
        ("Ku bayangkan jika kamu tidur disampingku",0.09),
        ("Di malam yang semu",0.09),
        ("Pejamkan mataku",0.09),
        ("Ku bayangkan tubuhmu jika di pelukanku\r\n",0.09),
    ]

    jeda = [
        #1,
        0.4, 
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.8,
        #2
        0.4, 
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
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
