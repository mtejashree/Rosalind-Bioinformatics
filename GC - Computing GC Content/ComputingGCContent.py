f = open('rosalind_gc.txt','r')
dna = f.readlines()
f.close()
dna_strands = {}
for line in dna:
    if line[0] == '>':
        dna_name = line[1:].rstrip()
        dna_strands[dna_name] = ''
    else:
        dna_strands[dna_name] = line.rstrip()
dna_ans = 0
gc_ans = 0
for dna1 in dna_strands:
    gc_temp = dna_strands[dna1].count('G') + dna_strands[dna1].count('C')
    gc_temp = (gc_temp*100)/len(dna_strands[dna1])
    if gc_temp > gc_ans:
        gc_ans = gc_temp
        dna_ans = dna1
print(dna_ans)
print(gc_ans)
        
        
    
    
    
