f = open('rosalind_dna.txt','r')
dna = f.read()
f.close()
A = dna.count("A")
C = dna.count("C")
G = dna.count("G")
T = dna.count("T")
print(A,C,G,T)

