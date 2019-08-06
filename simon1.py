#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:58:50 2019

@author: simon
"""

import random


number = random.randint(1, 10)
tries = 1



uname = input("hello, What's your name?" )


print("hello", uname + ".", )

question = input("Would you like to play a game? [y/n]" ) 
if question == "n":
    print("oh...okey")
    
    
if question == "y":
    print("I am thinking of a number between 1 and 10")
    guess = int(input("have a guess: "))
    if guess > number:
        print("guess lower ....")
    if guess < number:
        print("guess higher ....")
    while guess != number:
        tries += 1
        guess = int(input("try again: "))
        if guess < number:
            print("guess higher")
    if guess == number:
        print("you're right! you win! the number was", number, \
              "and it only", tries,"tries!")
        