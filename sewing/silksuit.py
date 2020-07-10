#!/usr/bin/python3

import threading

import time

def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print("Orion you are primed for launch. Count down begins...")

mythread = threading.Thread(target=groundcontrol)

mythread.start()
