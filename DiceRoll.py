#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    rolls[dice2+dice1-1] = rolls[dice2+dice1-1]+1
  #print statictics for dice rolls
  dice = 1 
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1
if __name__ == '__main__':
  main()
