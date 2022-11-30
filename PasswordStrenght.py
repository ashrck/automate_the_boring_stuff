print('password:')
password = 'Gyvt12fcrdxhd'
import re
from signal import valid_signals


def password_strength(password):
    if len(password) > 8:
        find_digit = re.compile(r'\d')
        find_lower_letter = re.compile(r'[a-z]')
        find_upper_letter = re.compile(r'[A-Z]')
        if (len(find_digit.findall(password)) > 0) and (len(find_lower_letter.findall(password)) > 0) and (len(find_upper_letter.findall(password)) > 0) :
            return True
    return False

if password_strength(password) == True:
    print('valid password')
else:
    print('invalid password')

#print(password_strength(password))