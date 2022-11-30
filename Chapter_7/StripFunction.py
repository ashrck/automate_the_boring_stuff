sample_text = ' ashar needs help'
import re
print(sample_text)

def strip(text, strip_var = ' '):
    if strip_var == ' ':
        finding_begins_whitespace = re.compile(r'^ ')
        new_text = finding_begins_whitespace.sub(r'', text)
        finding_ends_whitespace = re.compile(r' $')
        new_text = finding_ends_whitespace.sub(r'', new_text)
        return new_text
    else:
        find_strip_var = re.compile(strip_var)
        new_text = find_strip_var.sub(r'', text)
        return new_text 

print(strip(sample_text))