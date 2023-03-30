from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda c,x: c + 1 if x[0]!=x[1] else c,list(zip(s1,s2)),0)

def ReverseComplement(dna):
    res=''
    for c in dna:
        if c == 'A':
            res+='T'
        elif c == 'C':
            res+= 'G'
        elif c == 'G':
            res+= 'C'
        elif c == 'T':
            res+='A'
    return res[len(res)-1::-1]
def PatternCount(index, k):
    s=''
    while k>0:
        s+=str(index%4)
        index = index//4
        k-=1
    d = {'0':'A', '1':'C', '2':'G', '3':'T'}
    res=''
    s = s[::-1]
    for c in s:
        res+=str(d[c])
    return res 

def ApproximateFrequentWords(text,k,d):
    freq_map = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        r_pattern = ReverseComplement(pattern)
        for j in range(4**k):
            p = PatternCount(j,k)
            if HammingDistance(p,pattern) <= d:
                if p in freq_map:
                    freq_map[p] += 1
                else:
                    freq_map[p] = 1
            if HammingDistance(p,r_pattern) <= d:
                if p in freq_map:
                    freq_map[p] += 1
                else:
                    freq_map[p] = 1
    max_count = max(freq_map.values())
    res = [kmer for kmer in freq_map.keys() if freq_map[kmer] == max_count]
    return sorted(res)

text = str(input())
k,d = map(int,input().split())
print(*ApproximateFrequentWords(text, k, d))
