from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda c,x: c + 1 if x[0]!=x[1] else c,list(zip(s1,s2)),0)

def ApproximatePatternMatch(pattern, text, d):
    c=[]
    for i in range (0,len(text)-len(pattern)+1):
        if HammingDistance(text[i:i+len(pattern)],pattern)<=d:
            c.append(i)
    return c


pattern = str(input())
text = str(input())
d = int(input())

#print(HammingDistance( pattern,text))
print(*ApproximatePatternMatch(pattern, text, d))
