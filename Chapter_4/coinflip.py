import random
numberOfStreaks = 0
HT = [] 
for experimentNumber in range(100000000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    headtail = ['H','T']
    if len(HT) < 100: 
        HT.append(headtail[random.randint(0,1)])

        if len(HT) == 100:
            for i in range(len(HT)): 
                if (HT[i:i+6] == ['H'] * 6) or (HT[i:i+6] == ['T'] * 6):
                    numberOfStreaks += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))