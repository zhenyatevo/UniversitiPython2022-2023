from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda c,x: c + 1 if x[0]!=x[1] else c,list(zip(s1,s2)),0)


s1 = str(input())
s2 = str(input())

print(HammingDistance(s1, s2))
