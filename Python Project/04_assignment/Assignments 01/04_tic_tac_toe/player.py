import math
import random


class Player:
    def __init__(self, letter):
        # letter is 'X' or 'O'
        self.letter = letter

    # we want all player to get their next move given a board
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # we're going to check that this is a correct value by trying to cast it to an int and if it's not in the available moves
            # if it's not, then we raise an error and ask for a new input
            # if it's not a number, or it's not in the available moves, then we raise a value error
            # if it's a number, then we check if it's in the available moves    

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val