from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the 3x3 board state
        self.current_winner = None # Keep track of the winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'.join(row))
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 ... (Tells us what number corresponds to what box in the board)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'.join(row))

        

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # return []
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', '0' ] --> [(0, 'x'), (1, 'x'), (2, '0')]
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign the square to the letter)
        # then return true. Otherwise, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 
        
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diogonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all of these fail, then there is no winner
        return False
    
    def play(self, x_player, o_player, print_game=True):
        # return the winner of the game! or None if it's a tie
        if print_game:
            self.print_board_nums()

        letter = 'X'  # starting letter
        # iterate while the game still has empty squares
        while self.empty_squares():
            if letter == '0':
                square = o_player.get_move(self)
            else:
                square = x_player.get_move(self)

            if self.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    self.print_board()
                    print('')

                if self.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter

                # after we make a move we need to alternate letters
                letter = '0' if letter == 'X' else 'X'  # switches player

        if print_game:
            print('It\'s a tie!')
        return None

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('0')
    t = TicTacToe()
    t.play(x_player, o_player, print_game=True)