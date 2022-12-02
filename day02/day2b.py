shape_score = {'X': 1, 'Y': 2, 'Z': 3}
winner = {'A': 'Y', 'B': 'Z', 'C': 'X'}
loser = {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

strategy = [l.split(' ') for l in open("input").read().splitlines()]

def score(opponent, outcome):
    if outcome == 'X':
        return shape_score[loser[opponent]]
    elif outcome == 'Y':
        return shape_score[draw[opponent]] + 3
    elif outcome == 'Z':
        return shape_score[winner[opponent]] + 6

total = sum(score(*args) for args in strategy)
print(total)
