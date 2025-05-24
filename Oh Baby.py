import sys
from time import sleep
import time

def print_lirik() :
    lines = [
        ("Oh, baby you gonna stop", 0.09),
        ("I see that you're calling", 0.10),
        ("I told you that I ain't picking up", 0.12),
        ("I know that you wanna start", 0.10),
        ("Cause we got our problems", 0.10),
        ("I love you but i just need tonight off", 0.11),
        ("............", 0.20)

    ]

    delay = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line :
            print(char, end = '')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delay[i])
        print('')

print_lirik()