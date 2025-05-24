import sys
import time
from time import sleep

def print_lagu():
    lirik = [
        ("I know what you want, what you want from me",0.08),
        ("I know what you think, what you think you see",0.08),
        ("I know what you lookin'for but i complete",0.09),
        ("I know what you need, but it won't be me\r\n",0.08),
        ("I know what you want, what you want from me",0.08),
        ("I know what you think, what you think you see",0.08),
        ("I know what you lookin'for but i complete",0.09),
        ("I know what you need, but it won't be me\r\n",0.08),
    ]

    delay = [0.1, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2]

    for i, (line, char_delay) in enumerate(lirik):
        for char in line :
            print(char, end = '')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delay[i])
        print('')

print_lagu()