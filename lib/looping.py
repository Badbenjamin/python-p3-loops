#!/usr/bin/env python3
import ipdb

def happy_new_year():
    i = 10
    while i >= 0:
        
        if i >= 1:
            print (i)
        elif i == 0:
            print ("Happy New Year!")
        i = i - 1


def square_integers(int_list):
    return [int * int for int in int_list]

def fizzbuzz():
   i = 1
   while (i <= 100):
        # print("Helllo", i)
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i = i + 1

fizzbuzz()