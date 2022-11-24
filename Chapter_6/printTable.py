tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Caroline', 'Ashar'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colHeights = []
    for i in range(len(list)):
        colHeights.append(len(list[i]))
    newtable = []
    for i in range(max(colHeights)):
        line = []
        for numlist in range(len(list)):
            try:
                line.append(list[numlist][i])
            except:
                pass
        newtable.append(line)

    colwidths = []
    for index in range(len(list)):
        temptablewidth = []
        for element in range(max(colHeights)):  
            try:
                temptablewidth.append(len(list[index][element])) 
            except:
                pass
        colwidths.append(max(temptablewidth))

    for element in range(len(newtable)):
        print('\n')
        for i in range(len(newtable[element])):
                print(newtable[element][i].rjust(colwidths[i]), end =' ') 

#        answer = ' '.join(newtable[element])
#        final.append(answer)
#    for element in range(len(final)):
#        print((final[int(element)]).rjust(len(max(final, key=len))), )

printTable(tableData)
