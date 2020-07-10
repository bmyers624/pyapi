#!/usr/bin/python3

import threading

import time

def groundcontrol(x):
    for i in range(x, -1, -1):
        print(i)
        time.sleep(1)

def orion():
    print("I forgot my socks.")
    time.sleep(1)
    print("Can we stop this ride?")
    time.sleep(2)
    print("No? Alright. Ugh. I forgot to close the garage too.")
    time.sleep(1)
    print("To infinity, and beyond!")

print("Orion, you are primed for launch. Count down begins...")

countdown = 10

mythread = threading.Thread(target=groundcontrol, args=(countdown, ))

astrothread = threading.Thread(target=orion)


mythread.start()
astrothread.start()

mythread.join()
astrothread.join()

input("Press Enter to exit.")
exit()
