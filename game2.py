#!/usr/local/bin/python3

import random
import sys


if len(sys.argv)< 3:
    print(f"Usage: {sys.argv[0]} change/nochange runcount", file=sys.stderr)
    exit(1)

mode=sys.argv[1]
tries=int(sys.argv[2])

correct=0
counter=0
while counter < tries:
    random.seed()
    guess = random.randrange(1,4,1)
    random.seed()
    door=random.randrange(1,4,1)

    print(f"Door is {door} and the contestant guessed {guess}")

    if door != 1 and guess !=1:
        open=1
    elif door !=2 and guess !=2:
        open=2
    else:
        open=3
    print(f"I opened door {open}")

    if guess != 1 and open != 1:
        ng=1
    elif guess != 2 and open != 2:
        ng=2
    else:
        ng=3

    if mode == "change":
        guess=ng
        print(f"The contestant has changed to door: {guess}")
    if guess == door:
        print("You are correct!")
        correct+=1
    else:
        print("You lose!")
    
    counter+=1

if correct > 0 and tries > 0:
    percent=correct/tries*100
else:
    percent=0
print(f"Contestant got {correct} correct out of {tries} tries ({percent} percent).")

