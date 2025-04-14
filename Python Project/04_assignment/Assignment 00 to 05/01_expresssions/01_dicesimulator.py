"""
Program dicesimulator
---------------------------
Simulate rolling two dice three times. Prints
the result of each roll. This program is used 
to show how variable scopes work."""

# Import the random module to generate random numbers
import random

#Number of  sides on the dice
NUM_SIDES = 6

def roll_dice():
    """
    Simulate rolling two dice and return the result.
    """
    die1: int= random.randint(1, NUM_SIDES)  # Roll the first die
    die2: int = random.randint(1, NUM_SIDES)  # Roll the second die
    total: int = die1 + die2  # Return the result as a tuple
    print("Total of the two dice is: ", total)  # Print the result

def main():
    die1: int = 10
    print("die1 in main() starts as: ", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() ends as: ", str(die1))


if __name__ == "__main__":
    main()