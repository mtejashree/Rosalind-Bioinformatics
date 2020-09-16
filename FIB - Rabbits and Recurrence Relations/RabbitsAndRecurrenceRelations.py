def RabbitsAndRecurrenceRelations(n,k):
    mature = 0
    newmature = 0
    small = 1
    for i in range(1,n):
        newmature = small
        small = mature*k
        mature = mature + newmature
    total = mature + small
    print(total)

