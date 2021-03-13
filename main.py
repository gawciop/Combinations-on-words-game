import sys
import itertools
import argparse
import string
import random


def words_check(word, words_list, l):
    for i in range(len(word)-2*l+1):
        word1 = word[0+i:l+i]
        word2 = word[l+i:2*l]
        k1 = -1
        k2 = -1
        for wrod in words_list:
            if all([i == j for i, j in zip(wrod[0], word1)]):
                k1 = wrod[1]
            if all([i == j for i, j in zip(wrod[0], word2)]):
                k2 = wrod[1]
        if k1 == k2:
            return False
    return True

def main(opt):
    A = string.ascii_lowercase[:opt.alphabet]
    words_list = [[roll, random.randint(1, opt.color)] for roll in itertools.product(A, repeat = opt.words)]
    print("------------------------------------------------")
    print("GAME HAS NOW STARTED")

    if 2*opt.words > opt.length:
        print("GAME HAS NO POINT! PLAYER 1 WILL ALWAYS WIN! GAME WILL NOW EXIT!")
        sys.exit()
    count = 0
    word = []
    while count < opt.length:
        print(f"------------------------------------------------\nTURN {count+1}")
        place = random.randint(0, count)
        letter = input(f"What letter in place {place} do you want to insert? Remember the alphabet is {A}\n")
        while letter not in A or letter == "":
            letter = input(f"You chose the wrong letter! What letter in place {place} do you want to insert? Remember the alphabet is {A}\n")
        word.insert(place, letter)
        count += 1
        print(f"Current word is {word}")
        if count >= 2*opt.words:
            if words_check(word, words_list, opt.words):
                print("Everything OK!")
            else:
                print("Congratulations to player 1!")
                sys.exit("Game over")
    print("Congratulations! Player 2 won!")
    sys.exit("Game over")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--alphabet', type=int, default=10, help='length of alphabet')
    parser.add_argument('--color', type=int, default=3, help='amount of different colors')
    parser.add_argument('--words', type=int, default=3, help='length of words')
    parser.add_argument('--length', type=int, default=20, help="length of the game")
    opt = parser.parse_args()
    main(opt)