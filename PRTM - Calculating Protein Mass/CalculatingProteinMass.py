def CalculatingProteinMass(protein):
    weight = 0
    n = len(protein)
    for i in range(0,n):
        if protein[i] == 'A':
            weight = weight + 71.03711
        elif protein[i] == 'C':
            weight = weight + 103.00919
        elif protein[i] == 'D':
            weight = weight + 115.02694
        elif protein[i] == 'E':
            weight = weight + 129.04259
        elif protein[i] == 'F':
            weight = weight + 147.06841
        elif protein[i] == 'G':
            weight = weight + 57.02146
        elif protein[i] == 'H':
            weight = weight + 137.05891
        elif protein[i] == 'I':
            weight = weight + 113.08406
        elif protein[i] == 'K':
            weight = weight + 128.09496
        elif protein[i] == 'L':
            weight = weight + 113.08406
        elif protein[i] == 'M':
            weight = weight + 131.04049
        elif protein[i] == 'N':
            weight = weight + 114.04293
        elif protein[i] == 'P':
            weight = weight + 97.05276
        elif protein[i] == 'Q':
            weight = weight + 128.05858
        elif protein[i] == 'R':
            weight = weight + 156.10111
        elif protein[i] == 'S':
            weight = weight + 87.03203
        elif protein[i] == 'T':
            weight = weight + 101.04768
        elif protein[i] == 'V':
            weight = weight + 99.06841
        elif protein[i] == 'W':
            weight = weight + 186.07931
        elif protein[i] == 'Y':
            weight = weight + 163.06333
    print(round(weight,3))
