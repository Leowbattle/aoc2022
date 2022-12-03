def half(l):
    x = len(l) // 2
    return (l[:x], l[x:])

def priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27

rucksacks = [half(r) for r in open("input").read().splitlines()]
result = sum(priority(set(first).intersection(second).pop()) for first, second in rucksacks)
print(result)
