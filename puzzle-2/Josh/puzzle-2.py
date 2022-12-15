
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

# PART TWO:
# For some reason it massively feels like I'm cheating with these maps 🤔

# lose, draw, win
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

# Rock: lose via scissors, draw via rock, win via paper etc.
play_score = {
    'A': {'X': 3, 'Y': 1, 'Z': 2},
    'B': {'X': 1, 'Y': 2, 'Z': 3},
    'C': {'X': 2, 'Y': 3, 'Z': 1},
}

with open('input.txt') as input_file:
    score = 0
    for line in input_file:
        opponent, desired_outcome = line[:3].split(' ')  # first three chars to avoid newline \n
        score = score + outcome_score[desired_outcome]
        score = score + play_score[opponent][desired_outcome]

print("part two score", score)
