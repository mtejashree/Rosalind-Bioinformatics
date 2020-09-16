f = open('rosalind_hamm.txt','r')
dna1 = f.readline()
dna2 = f.readline()
f.close()
total = 0
n = len(dna1)
d1 = list(dna1)
d2 = list(dna2)
for i in range(1,n):
    if d1[i] != d2[i]:
        total = total+1
print(total)
