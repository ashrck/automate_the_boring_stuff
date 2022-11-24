#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = str(pyperclip.paste())

lines = text.split('\r\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i] # loop through all indexes in the "lines" list
    print(lines)
text = '\n'.join(lines)

pyperclip.copy(text)


