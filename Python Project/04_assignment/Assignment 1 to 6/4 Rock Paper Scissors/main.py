import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    

    #  r > s, s > p, p > r
    if is_win(user, computer):
        return "You Won!"
    
    return "You Lost!"

def is_win(player, opponent):
    # return True if player wins
    #  r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'r') \
    or (player == 'p' and opponent == 'r'):
        return True
    

if __name__ == "__main__":
    print(play())