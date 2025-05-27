import sys
import time
from time import sleep

def CLBK() :

    lirik = [
        ('\r\nSemua jadi masa lalu',0.08),
        ('Cerita terindah antara kau dan aku\r\n',0.08),
        ("Mau tak mau ku harus menolakmu",0.05),
        ("Kar'na ku sudah ada pengganti diri mu",0.05),
        ('Aku yang sekaran bukanlah yang dulu',0.05),
        ('Maafkan mantan aku tak mau\r\n',0.05),
        ('Cintaku padamu bersemi kembali',0.08),
        ('Maukah kau menjadi pacarku lagi\r\n',0.08)
    ]

    jeda = [
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.4,
        0.3,
        0.2,
    ]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(jeda[i])
        print('')

if __name__ == '__main__' :
    CLBK()