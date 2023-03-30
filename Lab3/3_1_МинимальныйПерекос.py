text = input()

def word(Genome):
    countC = 0
    countG = 0
    d ={}
    i = 0
    for j in range(len(Genome)):
        if Genome[j] == "C":
            countC +=1
        if Genome[j] == "G":
            countG +=1 
    for j in range(i,len(Genome)):
        if Genome[j] == "C":
            countC -=1
        if Genome[j] == "G":
            countG -=1 
        m = countC-countG
        d.update({i+1:m})
        
        i+=1
    
    max_value = min(d.values())
    d1 = {k: v for k, v in d.items() if v == max_value}
    return " ".join(sorted( list(map(str,d1.keys() ) ) ) )
   

print (word(text))
