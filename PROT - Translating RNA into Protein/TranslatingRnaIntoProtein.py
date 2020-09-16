f = open('rosalind_prot.txt', 'r')
rna = f.read()
f.close()
d = len(rna)
n = d/3
m = int(n)
j = 0
protein = ["" for x in range(m)] # to create an empty string array
for i in range(0,d-2,3):
    codon1 = rna[i:i+3]
    if codon1 in ['UUU', 'UUC']:
        protein[j] = 'F'
    elif codon1 in ['UUA','UUG','CUU','CUC','CUA','CUG']:
        protein[j] = 'L'
    elif codon1 in ['UCU','UCC','UCA','UCG','AGU','AGC']:
        protein[j] = 'S'
    elif codon1 in ['UAU','UAC']:
        protein[j] = 'Y'
    elif codon1 in ['UAA','UAG','UGA']:
        protein[j] = 'stop'
    elif codon1 in ['UGU','UGC']:
        protein[j] = 'C'
    elif codon1 in ['UGG']:
        protein[j] = 'W'
    elif codon1 in ['CCU','CCC','CCA','CCG']:
        protein[j] = 'P'
    elif codon1 in ['CAU','CAC']:
        protein[j] = 'H'
    elif codon1 in ['CAA','CAG']:
        protein[j] = 'Q'
    elif codon1 in ['CGU','CGC','CGA','CGG','AGA','AGG']:
        protein[j] = 'R'
    elif codon1 in ['AUU','AUC','AUA']:
        protein[j] = 'I'
    elif codon1 in ['AUG']:
        protein[j] = 'M'
    elif codon1 in ['ACU','ACC','ACA','ACG']:
        protein[j] = 'T'
    elif codon1 in ['AAU','AAC']:
        protein[j] = 'N'
    elif codon1 in ['AAA','AAG']:
        protein[j] = 'K'
    elif codon1 in ['GUU','GUC','GUA','GUG']:
        protein[j] = 'V'
    elif codon1 in ['GCU','GCC','GCA','GCG']:
        protein[j] = 'A'
    elif codon1 in ['GAU','GAC']:
        protein[j] = 'D'
    elif codon1 in ['GAA','GAG']:
        protein[j] = 'E'
    elif codon1 in ['GGU','GGC','GGA','GGG']:
        protein[j] = 'G'
    j = j+1

protein1 = ''.join(protein)
print(protein1)

    
        
    
    
    
    
