import sys
import time
from time import sleep

def laguflower() :
    lirik = [
        ("\r\nYou can ask a flower",0.09),
        ("I sit for hours",0.09),
        ("Tellin all the bluebirds",0.09),
        ("The bill and coo birds",0.09),
        ("Pretty little baby",0.09),
        ("I'm so in love with youuuuu\r\n",0.09),
    ]

    jeda = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(jeda[i])
        print('')

if __name__ == '__main__' :
    laguflower()