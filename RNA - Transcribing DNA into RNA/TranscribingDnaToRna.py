f = open('rosalind_rna.txt','r')
dna = f.read()
d = len(dna)
rna = list(dna)
for i in range(1,d):
    if dna[i] == 'T' :
        rna[i] = 'U'
rna1 = ''.join(rna)
print(rna1)

   
