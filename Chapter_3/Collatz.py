def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number /= 2 
            print (int(number))
            if number == 1:
                break

        if (number % 2 != 0):
            number *= 3 
            number += 1
            print (int(number))
            if number == 1:
                break
    return number

print ('Choose a number:')
try:
    chosen_number = int(input())
    collatz(chosen_number)
except:
    print ('not a number')