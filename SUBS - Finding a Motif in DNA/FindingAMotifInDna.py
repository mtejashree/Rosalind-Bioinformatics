def FindingAMotifInDna(s,t):
    n = len(s)
    m = len(t)
    for i in range(0,n):
        if s[i:i+m] == t:
            print(i+1)
