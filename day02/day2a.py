shape_score = {'X': 1, 'Y': 2, 'Z': 3}
winner = {'A': 'Y', 'B': 'Z', 'C': 'X'}
mapper = {'A': 'X', 'B': 'Y', 'C': 'Z'}
strategy = [l.split(' ') for l in open("input").read().splitlines()]

def score(opponent, me):
    if me == mapper[opponent]:
        return 3 + shape_score[me]
    elif me == winner[opponent]:
        return 6 + shape_score[me]
    else:
        return 0 + shape_score[me]

total = sum(score(*args) for args in strategy)
print(total)
