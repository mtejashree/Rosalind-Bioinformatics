f = open('rosalind_revc.txt', 'r')
dna = f.read()
dna1 = dna[::-1]
d = len(dna1)
dna2 = list(dna1)
for i in range(1,d):
    if dna1[i] == 'T':
        dna2[i] = 'A'
    elif dna1[i] == 'A':
        dna2[i] = 'T'
    elif dna1[i] == 'G':
        dna2[i] = 'C'
    elif dna1[i] == 'C':
        dna2[i] = 'G'
dna3 = ''.join(dna2)
print(dna3)

