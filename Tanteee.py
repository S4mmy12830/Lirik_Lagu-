import time
from time import sleep
import sys

def lagu():
    lirik = [
    ('Tantee..',0.08),
    ('Sudah terbiasa terjadi tanteeee',0.09),
    ('Teman datang ketika lagi butuh sajaaaa',0.08),
    ('Coba kalau lagi susahhhh',0.10),
    ('Mereka semuan menghilaaaaaaaang',0.10)
    ]

    jeda = [1.0, 2.5, 1.0, 1.0, 1.0]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(jeda[i])
        print('')

if __name__ == '__main__' :
    lagu()