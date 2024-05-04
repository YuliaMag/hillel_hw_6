
dic_t = {}

with open("test.txt", "r") as f:
    for ln in f:
        dic_t[len(ln)] = ln

print(dic_t[sorted(dic_t)[-1]])
