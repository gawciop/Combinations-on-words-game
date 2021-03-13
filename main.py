import sys
import itertools
import numpy as np
import string
import random


def words_check(word):
    for i in range(len(word)-2*l+1):
        word1 = word[0+i:l+i]
        word2 = word[l+i:2*l]
        k1 = -1
        k2 = -1
        for wrod in words_list:
            if all([i == j for i, j in zip(wrod[0], word1)]):
                k1 = wrod[1]
                print(k1)
            if all([i == j for i, j in zip(wrod[0], word2)]):
                k2 = wrod[1]
                print(k2)
        print(k1, k2)
        if k1 == k2:
            return False
    return True


lenA = 10
A = []
l = 3
n = 20
k = 3
A = string.ascii_lowercase[:lenA]
words_list = [[roll, random.randint(1, k)] for roll in itertools.product(A, repeat = l)]
print("------------------------------------------------")
print("GAME HAS NOW STARTED")

if 2*l > n:
    print("GAME HAS NO POINT! PLAYER 1 WILL ALWAYS WIN! GAME WILL NOW EXIT!")
    sys.exit()
count = 0
word = []
while count < n:
    print(f"------------------------------------------------\nTURN {count+1}")
    place = random.randint(0, count)
    letter = input(f"What letter in place {place} do you want to insert? Remember the alphabet is {A}\n")
    while letter not in A:
        letter = input(f"You chose the wrong letter! What letter in place {place} do you want to insert? Remember the alphabet is {A}\n")
    word.insert(place, letter)
    count += 1
    print(f"Current word is {word}")
    if count >= 2*l:
        if words_check(word):
            print("Everything OK!")
        else:
            print("Congratulations to player 1!")
            sys.exit("Game over")
print("Congratulations! Player 2 won!")
sys.exit("Game over")