from tkinter import *
import tkinter as tk
import time
import random

wordCount = int(input("Enter amount of words: "))

i = wordCount + 1
a = time.perf_counter()

while i > 1:
    f = open('Typing Test\word_list.txt').read().splitlines()
    line = random.choice(f)
    print(line)
    answer = str(input())

    if answer == line:
        print("Correct!")
        pass
    else:
        print("Wrong!")
        break
    i -= 1
    
b = time.perf_counter()

time = b - a
print( "Your Time:", round(time, 1))