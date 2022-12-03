def priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27

rucksacks = open("input").read().splitlines()

result = 0
for i in range(0, len(rucksacks), 3):
    a, b, c = rucksacks[i:i+3]
    item = set(a).intersection(b, c).pop()
    result += priority(item)

print(result)
