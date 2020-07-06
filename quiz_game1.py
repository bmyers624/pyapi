#!/usr/bin/env python3

import time

true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]
correct = 0 #Storing the correct answers

name = input ("Please input your name: ") #Stores the user's name

print ("\nHello, " +  name +", let's begin the quiz. The following answers are only True or False.")
time.sleep(3)

print ("\nLondon is the captial of the United Kingdom.")
choice = input(">>> ")
if choice in true:
  correct += 1 #If correct, user gets one point
else:
  correct += 0
  
print ("\nBangladesh is an island.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0  

print ("\nHong Kong is part of Great Britian.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print ("\nRome is the capital of Italy.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  
  
print ("\nSparta was a city-state in ancient Greece")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\nThe major axis powers in WW2 were Germany, Japan and Great Britain")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
print ("\nAll done, " + name +".... You got", correct, "out of 6 correct!")
