
play_score = {'X': 1, 'Y': 2, 'Z': 3}
# Rock: A, X
# Paper: B, Y
# Scissors: C, Z

outcome_score = {
    'X': {'A': 3, 'B': 0, 'C': 6},
    'Y': {'A': 6, 'B': 3, 'C': 0},
    'Z': {'A': 0, 'B': 6, 'C': 3},
}

with open('input.txt') as input_file:
    score = 0
    for line in input_file:
        opponent, player = line[:3].split(' ')  # first three chars to avoid newline \n
        score = score + play_score[player]
        score = score + outcome_score[player][opponent]

print("final score:", score)