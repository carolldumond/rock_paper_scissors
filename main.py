import random as rdm

# r > s
# s > p
# p > r

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = rdm.choice(['r', 'p', 's'])
   # print(computer)
    if user == computer:
        return 'tie'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player, opponent):
    # if return True the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

