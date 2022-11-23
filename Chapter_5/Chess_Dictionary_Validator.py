from itertools import count

position1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

boardletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

blackwhite = ['b','w']

#for i in range(8):
#    for l in range(len(boardletters))
#        possiblepositions.append(boardletters[l])

def valid(position):
    if ('bking' not in position.values()) or ('wking' not in position.values()):
        print('missing king')
        return False
    #for i in range(8):
        #for l in range(len(boardletters)):
            #if ((str(i+1) + str(boardletters[l])) not in position.keys()):
               # print(str(i+1) + str(boardletters[l]))
                #print('invalid board position')
    for i in position.keys():
        if (int(i[0]) > 8) or (int(i[0]) < 1):
            print('position not valid')
            return False
        if (i[1] >= 'h') and (i[1] <= 'a'):
            print('position not valid')
            return False 
    for i in position.values():
        if (i[0] != 'w') and (i[0] != 'b'):
            return(False)
    totalpieces = list(position.values())
    print(list(position.values()))
#    for i in position.values():
#        totalpieces.append(i)
    if (totalpieces.count('bpawn') > 8) or (totalpieces.count('wpawn') > 8):
        print('position not valid')




 #   if (totalpieces.count('bking') > 1) or (totalpieces.count('wking') > 1):
 #       print('position not valid')
 #   if (totalpieces.count('brook') > 2) or (totalpieces.count('wrook') > 2):
 #       print('position not valid')
 #   if (totalpieces.count('bknight') > 2) or (totalpieces.count('wknight') > 2):
 #       print('position not valid')
 #   if (totalpieces.count('bbishop') > 2) or (totalpieces.count('wbishop') > 2):
 #       print('position not valid')




    #for i in range(len(location)):
     ##   if (location[i] not in :
    return True


valid(position1)