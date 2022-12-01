print(max(sum(int(x) for x in l.splitlines()) for l in open("input").read().split("\n\n")))
