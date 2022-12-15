# %% [markdown]
# ## Advent of Code Day 2

# %%
import pandas as pd

# %%
input  = '''A Z
A Z
A Z
B Z
C X
A Z
A Z
C Y
A Z
A Y
B Y
A Z
C X
A Z
A Z
A Z
A Z
A Y
A Z
A Z
C Y
C X
C X
C X
A Z
A Z
B Y
A Z
A Z
C Z
B Z
A Y
A Z
B Y
A Z
B Y
A X
B Z
A Z
A Z
A Z
C X
C X
A X
A Z
A Z
C X
A Z
B Y
A Z
B Z
A Z
A Z
B Z
B Z
C Y
B Z
A X
B Z
A Z
B Y
A Z
B Z
C X
A Z
B Y
B Z
A Z
B Y
C X
B Y
A Z
A Z
A Z
B Y
A Z
A Z
B Y
B Z
C Z
A X
A Z
A Z
C Z
C X
A Z
C X
A Z
A X
A Z
A Z
A Z
B X
B Y
A Z
A Z
A Z
C Y
B Y
C X
C X
A Z
A Z
A Z
A X
C X
B Z
C X
C X
A Z
A Z
A Z
A Z
B Z
A Y
A Y
C X
A Y
C X
B Y
A Z
C Z
A Z
B Y
A Z
C X
B X
A Y
C X
A Z
A Z
A Y
B Z
C X
C X
C X
B Y
A Z
A Z
B Y
A Z
B Z
C X
C Z
A Z
C X
B Z
A Z
B Y
C X
A Y
B Y
C X
C X
A Z
A Y
A Z
A Z
A Z
A Y
C X
A Z
A Z
B Z
A Z
B Z
A Z
C Z
C Z
A Z
A Z
B Z
A Z
B Z
A Z
B Z
B Y
B Y
B Z
B Y
A Z
A Z
A Z
A Z
A Z
A Z
A Z
A Z
C X
C X
A Z
A Z
C Y
A Z
C Y
B Y
C X
B Z
A Z
A Z
C X
A Z
B Y
A Z
A Z
A Z
B Z
A Z
B Y
A Z
B Y
A Z
A Z
C Z
A Z
C X
C Y
C X
C Y
C X
A Z
B Z
A Z
A Z
A Z
A Z
A Z
B Y
A Z
C X
C X
A Z
A Z
C Z
C Z
A Z
A Z
A Z
C X
A Z
A Z
A Z
A Y
A Z
C X
A Z
A Z
A Z
C X
C X
A Z
C Y
A X
A Z
A Z
A Y
B Z
A Z
A Z
A Z
C X
A Z
A Z
A Z
B Z
B Z
A Y
B Z
C X
B Y
A Z
A Z
A Z
A Z
A Z
A Z
B Z
C X
A Z
A Y
A Z
B Y
B Z
C Z
A Z
A Y
A Z
B Z
A Y
C X
A Z
A Y
A Z
C Y
A Z
A Z
B Y
C X
A Z
A Z
A X
A Z
C X
A Z
B Y
A Z
C X
A Z
B Y
A Z
C Y
B Z
C X
A Z
C X
B Y
A Z
C X
A Z
B Y
A Z
A Z
C Z
A Z
A Y
A Z
A Z
C X
A Y
A Z
B Z
A Z
A Y
C X
A Z
B Y
A Y
A Z
A Z
A Z
A Z
A Z
A Z
B Z
B Y
B X
C Y
B X
A Z
A Y
C X
A Z
A Z
C X
C Y
A Y
A Z
C X
B Y
B Y
C X
A Z
C Y
A Z
A Z
A Z
A Z
B X
A Z
A X
B Z
C Z
A Z
A Z
A Y
A Z
A Y
A Z
A Z
B Y
A Z
A Z
A Z
C X
A Z
A Z
A Z
B Z
A Z
A Z
A Z
A Z
A Z
B Z
A Z
A Z
C X
A Z
A Z
A Z
A Z
A Y
A Z
A Z
C Z
A Z
A Y
B Y
B Z
A Z
B Y
B Z
A Z
C X
A Z
B X
A Z
A Z
A Y
A Z
B X
B Z
A Z
B Z
A Y
A Z
A Z
A Z
B Y
A Z
B Z
A Z
B Z
A Z
A Y
A Z
B Z
A Z
C X
C X
A Z
A Z
B Z
A Z
A Z
C X
A Z
A X
A Z
A X
C X
A Y
C Y
B Y
A Z
A Y
A X
A Z
A Y
A Z
A Z
A Z
C X
B Z
A Z
B Y
A Z
A Y
A Z
A Z
B Z
C X
A Z
A Z
A Y
C X
C Y
B Z
A Z
A Z
B Z
C X
A Z
A Z
A Z
C Y
A Y
A Z
B Z
B Z
A Z
B Z
A X
A Z
B Z
A Z
A Z
B Y
A Z
A Y
B Y
A Z
B Z
C X
C Y
A Z
B Z
C X
A Z
B X
A Z
A Z
C X
A Z
A Y
B Z
B Y
A Z
A Y
C Y
A Z
C X
B Z
A X
A Z
A Z
A Z
A Z
A Z
A Z
A Z
A Y
A Z
A Z
C X
B Y
B Z
C X
C X
C X
A Z
A Z
B Z
B Y
A Z
A Z
B Y
B Y
A Y
A Y
A X
A Y
B Y
A Y
C X
A Z
A Z
A Z
A Y
B Y
A Z
C Y
B Z
C X
A Y
A Z
C Z
A Z
B Z
C X
B Z
C X
B Z
B Y
B Y
C X
A Z
A Z
B Z
B Z
B Z
A Z
A Z
A Z
A Z
A Z
C X
C X
C Y
B X
C X
A Z
A Z
A Z
A Z
A Z
A X
A Z
C X
A Z
C Z
A Z
C X
C Z
A Z
A Z
A Y
B Z
A X
A Z
A Z
A Z
C X
B Y
A Z
B Y
A Z
B Y
A Z
C X
A Z
C X
A Z
A Z
A Z
A Z
A Z
B X
B Y
C X
C X
A Z
C X
A Z
A Z
A Z
A Y
A Z
A Y
A Z
A Z
A Z
C Y
A Z
A Z
B Z
B Y
C X
A Y
A Z
B Z
A Z
A Z
A Z
B Y
C Z
A Y
C Y
A X
A X
B Z
A Y
C X
C X
B Z
A Z
B Z
A Z
A Z
A Y
B Z
C Y
A Z
A Z
A Z
C X
B Y
A X
A Z
C X
A Z
B Z
B Y
C X
B Y
A X
A Z
A Z
A Z
A Y
A Z
A Z
A Y
A Y
A Y
A X
A Z
A Z
B Z
A Y
A Z
C X
C X
A Z
A Z
B Z
B Y
A Z
A Z
C X
A Y
C X
B Z
A Z
A Z
A Z
A Y
A X
C Y
C X
C X
A Z
A Y
A Z
A Z
A Z
C X
A Z
A Z
B Z
C X
C X
B Z
B Z
C X
A Z
B X
A Z
B Z
A Y
A Z
A Z
C X
A Z
C Z
A Z
B Z
C X
A Z
B Y
A Y
A Z
A Z
B X
C X
B Z
C X
C X
C Y
B Z
C X
A Y
C X
A Z
A Z
A Z
A Y
A Z
C X
C Y
A Z
A Z
B Z
A Z
B Y
A X
A X
B Z
C X
B Y
A Z
C X
A Z
B Z
A Z
B Y
B Y
A X
B Y
A Z
A X
A Z
C X
A Z
A Z
B Y
C Y
A X
A Z
C Y
C X
A Z
A Z
A Z
A Y
A Z
C X
A Z
B Y
A Z
B Z
B Z
C X
B Y
A Z
C Y
A Y
A Z
A Z
C X
A Z
A Z
A Z
A Z
B Y
B Z
A Z
A Z
C Y
A Z
A Z
A Z
A Z
A Y
A Z
A Z
C Y
B Y
B Z
A Z
B Z
A Z
B Z
A Z
A Z
A Y
A Z
A Z
B Z
C Y
A Z
B Z
A X
C X
C X
A Z
A Z
A Z
A Z
A Z
C X
A Z
C X
A Z
B Y
A Z
C Y
A Y
B Z
C X
A Y
A Z
A Y
A Z
B Z
B Y
A Y
B Z
A Z
A Z
C Z
C Z
A Y
A Z
A Z
C X
A Z
A X
C Y
C X
A Z
A Z
B Y
B Z
C Y
A Z
B Z
A Z
C Z
A Z
A Y
B Y
C X
A Z
A Z
A Z
C X
A Z
A Y
A Z
A Z
B Z
C X
C X
C X
A Z
A Z
A Z
C X
A Z
A Z
A Z
A X
A Z
C X
C X
B Z
A Z
A Z
A Z
B Y
A Z
C X
A X
B Z
C X
A Z
C X
A Y
A Z
A Z
A Y
A Z
A Y
A X
C X
A Z
A Y
B Y
A Z
A Y
C Z
B Y
A Z
A Z
A Y
A Z
C X
A Z
B Y
B Z
B Z
A Z
A Z
A Z
C X
A Z
B Y
B Y
A Z
A Y
C X
A Z
C X
A Z
C X
C X
A Y
B Z
A Z
A Z
A Z
A Y
A X
B Y
A Z
B Z
B Y
C Y
C X
C Y
A Z
B Z
A Z
A Y
B X
C Z
A X
A Z
A Z
A Z
A Y
A Y
A Z
A Y
C X
A Z
A Y
C X
A Z
A Z
C Y
A Z
B Z
A Y
B Z
B X
B Z
C X
A Z
A Z
C X
A Z
A Z
C X
B Z
B Z
B Z
A Z
A Z
B Y
A Z
A Z
C Z
C Z
B Z
A Z
B Y
A Z
A Z
C X
B Z
A Z
A Z
A Z
C Y
B Y
C X
A Z
A Z
A Z
A Y
A Z
C X
A Z
C X
A Z
A Z
C Y
C X
C X
C X
C X
C X
B Z
B Z
B Y
B Y
C Z
A Z
B Z
A Z
A X
A Z
A Z
A Z
C X
A Z
C X
A Z
A Z
C X
C X
B Y
A Z
C Y
A Z
A Y
C Y
B Z
B Y
C X
A Z
C Y
A Z
A Z
A Z
B Y
C X
B Z
B Z
C X
B Y
B Z
A Z
C X
A Z
B Y
B Z
A Y
A Z
A Z
A Z
A Z
C Y
A Z
C Y
A Z
B Y
C X
B Z
A Z
A Z
B Z
C X
B Z
A Z
A Z
A X
B Y
A Z
A Z
A Z
A Z
A Y
B Z
A Z
A Z
A Z
B Z
C Y
C X
C X
B Z
A Z
B Z
C X
A Y
C X
B Y
B Z
C Y
B Y
B Y
A Y
C Y
A Z
A Z
B Z
B Z
A X
A Z
A Z
B Z
A Z
B Z
A X
A Z
A Y
A Y
A Z
B Z
A Z
B Z
A Z
B Z
C X
A Z
A Z
C X
A Z
A Z
A Z
C X
B Y
A X
B Z
B Z
C Y
A Z
A Z
C X
B Y
C X
A Z
A X
A Z
A Z
A Z
A Z
A Z
A Z
A Z
A Z
A Z
C X
B Z
B Z
C X
A Y
C Z
A Y
A Z
C Y
A Z
A Z
A Y
A Z
C X
C Z
A Z
A Y
A Z
A X
A Y
A Z
C X
B Z
A Z
B Z
C Y
C X
A Z
A Z
A X
A Z
B Z
C X
A Z
B Y
A Z
A X
A Z
B Z
A Z
A Z
C X
B Z
B X
A Z
A Z
C Z
A Z
A Z
A Y
B Z
A Z
C X
B Z
A Z
C Y
A Z
B Z
B Z
A Z
A Z
C X
B Z
C Y
A Y
A Y
B Z
A Z
A Z
C Z
B Z
A Y
A Y
C Z
C Z
A Z
B Z
B Y
A Z
B Y
A Z
A Z
A Z
C Y
A Y
A Z
A Z
A Z
A Z
C Z
A Z
B Y
A Z
B Z
C Y
A Z
B Y
B Z
A Z
A Y
A Z
A Z
B Z
A Z
A Z
A Z
C Z
B Z
C X
B Z
A Z
A Z
A Y
A Z
A Z
A Z
A Z
C Y
A Z
A Z
A Z
A X
A Y
B Y
C X
A Z
A Z
B Y
A Z
C X
A Y
A Z
A Z
C X
A X
A Z
A Z
A Z
B Y
B Z
A X
A Z
C X
A Z
C X
B Z
B Y
A Z
B Y
A Y
A Z
A Y
A Z
B Y
C X
B X
B Y
C X
A Z
A Z
A Y
A Z
A Y
B Z
B Y
B Y
A Y
A X
A Z
C X
A Z
B X
A Z
A Z
C X
B Y
B Z
B Z
B Y
B Z
A Y
C X
C Z
A Z
A Y
B Y
B Y
A Z
A Y
C Y
B Y
B Z
A Z
A Y
A Z
B Z
A Z
A Z
A Z
A Z
B Z
A Y
C X
A Z
A Z
B Y
A Z
B Y
B Z
A Z
C X
A Z
C X
B Y
A Z
B Z
C X
A Z
A Z
A Z
C X
C X
A Z
A Z
A Z
B Y
A Z
A Z
A Z
A Z
A Z
A Y
B Z
C Y
A Y
C X
A Z
A Z
B Y
B X
A Z
C Z
A Z
A Y
A Z
A X
A Z
A Z
A Z
C Z
C X
C X
B Y
C X
C X
B Y
C Z
C X
C X
A Y
A Z
C X
C Z
B Y
A Z
C X
C X
A Z
A Z
A Z
A Y
A Z
A Y
B Z
A Z
A Z
A Z
A Z
A Z
A Z
C X
C X
C X
C X
A Z
A Z
B Z
A Y
A Z
A Z
B Z
A Z
A Z
A Z
A Z
A Z
C X
C X
A Z
A Z
C X
C Z
C Z
A Z
A Z
B Y
B Z
A Z
A Z
B Y
B X
C X
B Y
C X
C X
A Z
C X
C X
C Y
C X
C X
C X
B Z
B Z
A Z
A Z
B Z
A Z
C X
A Z
B Y
A Y
A Z
C Z
B Y
B Z
B Z
A Z
C X
B Z
A X
B Y
A Y
B Y
B Z
A Z
A Z
A Z
A Z
A Z
A Z
C X
C X
B Z
A Z
B Y
A Z
B Z
A Z
B Y
A Z
A X
A Z
B Y
B Y
A Y
C X
A Z
A Z
C Y
A Z
A Z
B Z
C Z
B Z
A Z
A Z
C X
C Y
B Z
A Z
C X
A Z
C X
B Y
C X
B Z
A Z
A Z
C X
A Z
C X
A Y
C X
C X
C Y
B Z
C X
B Z
C X
A Z
A Z
C X
A Y
B Z
C X
B Z
C X
A Z
C X
C X
A Z
A Z
B Y
C Z
A X
A X
A Z
C X
A Z
A Z
A Z
A Y
A Z
A Z
A Z
A Z
B Z
C X
B Y
A Z
A Z
B Y
A Z
A Z
A Z
A Z
B Y
A Z
B Z
A Y
A Y
A Y
A Z
A Y
A Z
B Z
A Z
B Y
A Z
C X
A Y
C X
A Z
B Y
A Y
A Z
A Y
A Z
C Z
A Z
B Z
A Z
C X
B Z
A Z
A Z
C X
B Y
A Z
C X
C Y
A Z
B Y
A Z
B X
B Y
B Y
C Z
C X
A Z
C X
A Y
A Y
B Z
A Z
C X
B Z
A Z
A Z
A Y
C X
C X
A Z
A X
B Z
A Z
A Z
A X
A Z
C X
A Z
B Y
A Z
B X
B Y
A Y
C X
A Z
A X
A X
A Y
B Y
A Y
A Z
C X
B Z
A Z
A X
A X
A Z
C X
B Z
C X
B Y
A Z
C X
A Y
A Z
A Z
A Z
A Z
C Z
B Z
C Z
A Z
A Z
C X
B Y
A Y
B Z
C X
B Z
A Z
A Z
A Z
A X
B Y
C X
B Y
B Z
B Z
A Z
A Y
C Y
A Y
A X
A Z
C X
A Z
A Z
A X
A Z
A Z
C X
A Z
A X
A Z
C Y
A Z
B Z
A Y
A Z
C Z
A Y
A Y
B Z
A Y
A Y
A Y
A Z
A Z
A Z
A Z
C X
A Z
A Z
A Z
A Z
A Z
A Z
A X
A Z
A Z
A Z
A Z
A Z
A Y
B Z
A Y
A Z
C X
A X
B Z
A Z
A X
C Y
B Y
B Y
B Z
C X
C X
A Z
A Z
C X
C X
A Z
A X
A Z
A Z
A Z
A X
C X
C X
A Z
A Y
A Z
A Z
A Z
A Z
C Z
A Z
C X
B Z
C Z
C X
A Z
B Y
C X
C X
B Z
C X
B Y
A Y
B X
A Z
A Z
A Z
B Z
C X
A X
B Z
A X
A Z
C Z
B Z
A Z
A Z
C X
C X
A X
C X
C Y
A Z
A Z
A Z
B Z
C Z
A Z
A Z
A Z
A Z
A Z
B Z
A Z
A Z
C X
B Y
A Z
B Z
A Z
C X
A Z
A Z
A Z
B Z
C X
B Y
A Z
A Z
A Z
C Y
A Z
A Z
C X
C X
A Y
B Z
A Z
C Y
C X
A Z
A Z
A Z
C X
A Z
A Z
B Z
B Z
A Z
A Z
A Z
C X
C X
A Z
B Z
A X
B Y
C X
C X
C X
A Z
C X
A Z
A Z
B Y
A Y
B Z
B Z
A Z
A Z
C Z
A Y
A Y
A Z
A Z
C X
C Z
A Z
A Z
A Z
A Z
C Y
B Y
B Y
C Y
A Z
C X
B Z
A X
A Y
B Z
A Z
A Z
A Z
A X
A Z
A Z
A Z
A Y
C Z
A Y
C X
A Y
A X
C X
A Z
B Y
A Y
B Y
A Z
C X
C Z
A Z
C Z
A Y
A Z
A Z
B Z
B X
B Z
B Z
B Y
C Z
C X
A X
C Z
B Z
A Z
A Z
B Z
A Y
A Z
B Y
C X
A Z
B Z
C X
A X
B Z
A Z
A Z
C X
C X
C X
B Z
C Z
A Z
C X
A Z
A Z
A Z
A Z
C Z
C X
A X
B Y
A Z
C X
C Z
A Z
C X
B Z
B Y
A Z
C X
A Z
B Z
C Z
A Z
A Z
A X
B Y
C X
A Z
C X
A Z
A X
C X
A Z
C X
A Y
A Z
C X
C Z
C Y
B Z
B Z
A Y
B Z
A Z
A Z
A Y
A Z
C X
C X
A Z
A Z
C X
B Z
A Z
B Y
A Z
A Z
A Z
C X
A Z
A Y
B Y
A Z
C X
A Z
A X
A Z
A Z
C X
C Y
A Z
C X
A Z
A Y
C X
B Z
C Z
B Y
A Z
A Z
B Y
A Z
B Y
A Z
A Z
A Z
C X
A Y
C X
A Z
C Y
A Z
A Z
A Z
B Y
B Z
B Z
C Z
A X
A Z
A Z
C X
A Z
C X
A Z
A X
C Z
C X
A Z
A Z
A Z
A Z
B Z
A Z
A Z
C Y
A Y
A Z
C Y
C Y
A Z
B Z
A Z
B Z
A Z
B Z
C Y
C X
C X
A Y
A Z
B Z
C X
A X
A Z
A Z
A Y
A Z
A Z
A Z
C X
C X
A Y
A Z
A Z
C X
B Z
B Y
A Y
A Z
B Z
A Z
A Z
A X
A Z
A Z
B Y
A Z
A Y
B Z
C X
A Z
A Z
A Z
C X
A Z
B Z
B Z
A Z
A Z
A Z
A Z
B Z
A Z
A Z
A Z
A Z
C X
C X
A Z
B X
A Z
B Y
C Z
A Z
A Z
A Z
C Z
A Z
B Y
A X
A Z
C Z
A Z
C Z
A Z
C X
A Y
C X
C Z
A Y
A Z
A Z
C X
C X
A Z
A Z
A Z
B Z
B Z
A Y
B Y
C Z
B Z
B X
A Z
A Z
A Z
C X
B Y
A Z
B Z
C X
A Z
A Z
C X
C X
A Z
A Z
A Z
A Z
B Z
A Z
A Z
A Z
A Z
A Z
B Z
A Z
A Z
B Z
A Y
A Z
B Y
A Z
A Z
A Z
B Z
A Z
A Z
C X
B Y
C X
A Y
C X
A Z
A Z
A Z
C X
B Z
A Z
A Z
A Z
A Z
A Z
C X
A Z
A Z
A Z
A Z
A Z
A Y
C X
B Y
C X
A Z
A Z
A Z
A Z
A Z
B Y
A Z
C X
A Z
A Z
A Z
A Z
A Z
A Z
A Z
C X
A Z
C X
A Y
B Z
A Z
C X
A Z
C X
B Z
B Z
A Z
A Z
A Z
C X
A Z
B Z
B Y
C X
C X
C X
B Z
A X
A Y
A Z
A Z
A Z
A Y
A Z
A Z
A Y
A X
A Y
C X
A Y
C X
B Z
B Y
C X
B Y
B Y
C X
A Z
A Z
B Z
C X
A Z
A Z
B Y
A Z
B Y
A Z
A X
C Y
C X
B Z
C X
A Z
A Z
A Z
C X
A Z
C X
A X
A Y
A Z
A Z
C X
A Y
A Z
B X
A Y
A Z
A Z
A Z
A Z
A Z
A Z
C X
A Z
C X
A Z
C Y
A Z
A Z
B Z
A Y
A Z
B Y
B Y
A Z
C X
A Z
C X
C Z
A Z
B Z
B Z
A Z
A Z
C X
C X
B Y
A Z
A Z
B Z
C Z
B Y
B Y
C X
A Z
A Z
B Y
A Z
C X
C Z
A Z
B Z
C X
A Y
C X
A Z
B Y
B Y
A Y
A Z
A Z
A Z
A Z
A Z
A Y
A Z
A Y
A Z
B Y
B Y
B Y
C X
A Z
A Z
A Y
A Z
A Z
C X
A Y
C X
A Z
A Z
A Z
B Y
A Z
A Z
B Z
C X
A Z
B Y
B Y
C X
C Z
B Y
A Z
A Z
A Z
C X
A Z
B Z
C Z
C X
B Y
A Z
A Z
A Y
A X
A Z
A Z
A Z
A Z
A Z
A Y
B Y
A Z
B Z
B Z
A Z
C Y
A X
A Z
A Z
C X
C X
C Y
B Y
B Y
B X
A Z
A Z
B Z
A Z'''

round_winner_scores = {'win': 6, 'draw': 3, 'lose': 0}
shape_scores = {'rock': 1, 'paper': 2, 'scissors': 3}

# %%
rounds = [[x[0], x[2]] for x in input.split('\n')]
rounds

def result(opponent, own):
    if opponent == own:
        return [round_winner_scores['draw'], round_winner_scores['draw']]
    elif (opponent == 'rock' and own == 'paper') or (opponent == 'paper' and own == 'scissors') or (opponent == 'scissors' and own == 'rock'):
        return [round_winner_scores['lose'], round_winner_scores['win']]
    elif (own == 'rock' and opponent == 'paper') or (own == 'paper' and opponent == 'scissors') or (own == 'scissors' and opponent == 'rock'):
        return [round_winner_scores['win'], round_winner_scores['lose']]
    else:
        print('Investigate')

def result_with_dict(opponent_mapping, own_mapping, opponent_choice, own_choice):
    opponent_dict = {'A': opponent_mapping[0], 'B': opponent_mapping[1], 'C': opponent_mapping[2]}
    own_dict = {'X': own_mapping[0], 'Y': own_mapping[1], 'Z': own_mapping[2]}
    if opponent_dict[opponent_choice] == own_dict[own_choice]:
        return [round_winner_scores['draw'], round_winner_scores['draw']]
    elif (opponent_dict[opponent_choice] == 'rock' and own_dict[own_choice] == 'paper') or (opponent_dict[opponent_choice] == 'paper' and own_dict[own_choice] == 'scissors') or (opponent_dict[opponent_choice] == 'scissors' and own_dict[own_choice] == 'rock'):
        return [round_winner_scores['lose'], round_winner_scores['win']]
    elif (own_dict[own_choice] == 'rock' and opponent_dict[opponent_choice] == 'paper') or (own_dict[own_choice] == 'paper' and opponent_dict[opponent_choice] == 'scissors') or (own_dict[own_choice] == 'scissors' and opponent_dict[opponent_choice] == 'rock'):
        return [round_winner_scores['win'], round_winner_scores['lose']]
    else:
        print('Investigate')

def mappings(opponent, own):
    dict = {'A': opponent[0], 'B': opponent[1], 'C': opponent[2], 'X': own[0], 'Y': own[1], 'Z': own[2]}
    return dict

def total_points(opponent_mapping, own_mapping, opponent_choice, own_choice):
    opponent = mappings(opponent_mapping, own_mapping)[opponent_choice]
    own = mappings(opponent_mapping, own_mapping)[own_choice]

    scores = [result(opponent, own)[0] + shape_scores[opponent], result(opponent, own)[1] + shape_scores[own]]
    return scores

# %%
def combination(x, y, z):
    opponent_total = 0
    own_total = 0
    dictionary = mappings(['rock', 'paper', 'scissors'], [x, y, z])
    for round in rounds:
        round_points = total_points(['rock', 'paper', 'scissors'], [x, y, z], round[0], round[1])
        opponent_total += round_points[0]
        own_total += round_points[1]
    return [opponent_total, own_total]

# %%
options = [['rock', 'paper', 'scissors'], ['rock', 'scissors', 'paper'], ['paper', 'scissors', 'rock'], ['paper', 'rock', 'scissors'], ['scissors', 'rock', 'paper'], ['scissors', 'paper', 'rock']]

for option in options:
    scores = combination(option[0], option[1], option[2])
    print(option, scores[1])
# x = 'rock'
# y = 'paper'
# z = 'scissors'
# round = rounds[0]
# round
# dictionary = mappings(['rock', 'paper', 'scissors'], [x, y, z])
# dictionary[round[1]]
# round_points = total_points(['rock', 'paper', 'scissors'], [x, y, z], round[0], round[1])
# round_points

# %%
def decrypt(opponent, result):
    if result == 'X':
        necessary_score = [round_winner_scores['win'], round_winner_scores['lose']]
    elif result == 'Y':
        necessary_score = [round_winner_scores['draw'], round_winner_scores['draw']]
    elif result == 'Z':
        necessary_score = [round_winner_scores['lose'], round_winner_scores['win']]
    for item in ['X', 'Y', 'Z']:
        if necessary_score == result_with_dict(['rock', 'paper', 'scissors'], ['rock', 'paper', 'scissors'], opponent, item):
            preferable_result = item
    return preferable_result
        

# %%
decrypt('A', 'X')
# opponent = 'rock'
# result = 'X'
# if result == 'X':
#     necessary_score = [round_winner_scores['win'], round_winner_scores['lose']]
# elif result == 'Y':
#     necessary_score = [round_winner_scores['draw'], round_winner_scores['draw']]
# elif result == 'Z':
#     necessary_score = [round_winner_scores['lose'], round_winner_scores['win']]
# necessary_score

# %%
decrypt('C', 'X')

# %%
victory_mappings = {'A': 'Y', 'B': 'Z', 'C': 'X'}
loss_mappings = {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw_mappings = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points = 0
for round in rounds:
    if round[1] == 'X':
        choice = loss_mappings[round[0]]
    elif round[1] == 'Y':
        choice = draw_mappings[round[0]]
    elif round[1] == 'Z':
        choice = victory_mappings[round[0]]
    # print(total_points(['rock', 'paper', 'scissors'], ['rock', 'paper', 'scissors'], round[0], choice))
    points += total_points(['rock', 'paper', 'scissors'], ['rock', 'paper', 'scissors'], round[0], choice)[1]

    print(round, choice, points)
    


