import sys
import time
from time import sleep

def stecu() :
    #lirik
    lirik = [
        ("\r\nAduh abang bukan maksudku begitu.", 0.09),
        ("Masalah stecu bukan brarti tak mauu", 0.09),
        ("Jual mahal dikit kan bisa", 0.08),
        ("Coba kase effort nya saja", 0.08),
        ("Kalo memang cocok bisa datang ke rumah\r\n", 0.07),
        ("Stecu stecu stelan cuek baru malu", 0.08),
        ("Adu ade ini mau juga abang yang rayu", 0.09),
        ("Stecu stecu stelan cuek baru malu", 0.08),
        ("Adu ade ini mau juga abang yang maju\r\n", 0.09),
    ]

    #delays
    delay = [0.2, 0.3, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2 ]

    for i, (line, char_delay) in enumerate(lirik) :
        for char in line :
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delay[i])
        print('')

if __name__ == '__main__' :
    stecu()