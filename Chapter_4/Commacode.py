spam = ['apples', 'bananas', 'tofu', 'cats', 'bee', 'tea']

#print(spam[:-1])

def comma(list):
    for i in range(len(list)):
        if i != (len(list)-1) and i != (len(list)-2):
            print(list[(i)] + ', ', end='')
        if i == (len(list)-2):
            print(list[i] + ' ', end='')
        if i == (len(list)-1):
            print('and ' + list[(i)] + '.' )

def commaQ(list):
    answer = ''
    for i in range(len(list)):
        if i != (len(list)-1) and i != (len(list)-2):
            #print(list[(i)] + ', ', end='')
            answer = answer + list[i] + ', ' 
        if i == (len(list)-2):
           # print(list[i] + ' ', end='')
           answer = answer + list[i] + ' ' 
        if i == (len(list)-1):
            #print('and ' + list[(i)] + '.' )
            answer = answer + 'and ' + list[i] 
    print(answer)
 

#print (str(list[(i-1)]) + 'and '+ str(list[-1]))
commaQ(spam)

# def split(list):
#     for i in range(len(list)):
#         print (i)

#split(spam)


