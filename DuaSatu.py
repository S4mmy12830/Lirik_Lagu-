import time
from time import sleep
import sys

def duasatu() :
    lirik = [
        ("\r\nTanpa ragu ku bilang",0.09),
        ("Kamu yang paling paham aku",0.09),
        ("Dua jadi satu",0.09),
        ("Belah hati aku",0.09),
        ("Aku mau maju",0.09),
        ("Tapi tinggal tunggu waktu\r\n",0.08),
        ("Ku merasakan", 0.08),
        ("Apa yang kau rasakan",0.07),
        ("Tanpa ragu kubilang",0.07),
        ("Kamu yang paling paham aku",0.07),
        ("Dua jadi satu",0.08),
        ("Belah hati aku",0.08),
        ("Aku mau maju",0.08),
        ("Tapi tinggal tunggu waktu\r\n",0.08),
        
    ]

    jeda = [0.1, 0.1, 0.5, 0.5, 0.5, 0.0, 0.3, 0.5, 0.1, 0.1, 0.6, 0.6, 0.6, 0.2]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(jeda[i])
        print('')

if __name__ == '__main__' :
    duasatu()