"""In this game, the player is in a land full of dragons. The dragons all live in caves with their large piles of collected treasure. Some dragons are friendly, and will share their treasure with you. Other dragons are greedy and hungry, and will eat anyone who enters their cave. The player is in front of two caves, one with a friendly dragon and the other with a hungry dragon. The player is given a choice between the two."""

import random
import time

def intro():
    print("You are in a land full of dragons. In front of you, \nyou see two caves. In one cave, the dragon is friendly\nand will share his treasure with you. The other dragon\nis greedy and hungry, and will eat you on sight.\n")

def chooseCave():
    cave = 0
    while cave != 1 and cave != 2:
        cave = int(input("Which cave will you go into? (1 or 2): "))
        print(cave)
        print(type(cave))
    return cave

def checkCave(cave):
    hungryDragon = random.randint(1, 2)
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)
    if cave == hungryDragon:
        print("Gobbles you down in one bite!")
    else:
          print("Gives you his treasure!")
          
def playAgain():
    play = input("Play again?")
    if play.lower() == "y":
          return True
    return False


if __name__ == "__main__":
    play = True
    while play == True:
          intro()
          cave = chooseCave()
          checkCave(cave)
          play = playAgain()
