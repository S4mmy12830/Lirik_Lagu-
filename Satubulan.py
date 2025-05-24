import sys
from time import sleep
import time

def print_lirik() :
    lirik = [
        ("Apa sudah ada kabar lain yang kau tunggu",0.10),
        ("Sudah ada kah yang gantikan ku",0.09),
        ("Yang khawatirkan mu setiap waktu",0.07),
        ("Yang cerita tentang apapun sampai hal-hal tak perlu",0.10),
    ]

    delay = [2, 2.3, 3.2, 1]

    for i, (line, char_delay) in enumerate(lirik):
        for char in line :
            print(char, end = '')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delay[i])
        print('')

print_lirik()