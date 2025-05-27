import sys
import time
from time import sleep

def lagu() :
    lirik = [
        ("\r\nKami dari ",0.11),
        ("27 bulan Mei",0.11),
        ("\033[32mBulan Mei \033[0m",0.09),
        ("Ayo dong bantai kami",0.11),
        ("\033[32mAyo dong bang \033[0m",0.08),
        ("Kalo elu punya nyali",0.10),
        ("\033[32mKalo punya nyali yee \033[0m",0.08),
        ("\r\nTongkrongan kami",0.10),
        ("bukan tongkrongan pecundang",0.09),
        ("\033[32mpecundang pecundang \033[0m",0.06),
        ("Kami siap membuktikan",0.09),
        ("\033[32mbuktikan \033[0m",0.08),
        ("Coba daerah perkampungan",0.10),
    ]

    jeda = [
        0.3,
        0.3,
        0.3,
        0.2,
        0.3,
        0.2,
        0.3,
        0.3,
        0.1,
        0.3,
        0.2,
        0.3,
        0.3,
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