def listtostring(listname):
    if len(listname) > 1:
        seperator = ', '
        listname[-1] = 'and ' + listname [-1]
        return seperator.join(listname)
    
spam = ['apples', 'bananas', 'tofu', 'cats']
print(listtostring(spam))


#ALTERNATE THIS WORKS FOR SINGLE VALUES
def comma_separator(sequence):
    if not sequence:
        return ''
    if len(sequence) == 1:
        return sequence[0]
    return '{}, and {}'.format(', '.join(sequence[:-1]), sequence[-1])

#note: I have no idea how to do .format and .join

test = ['apples', 'bananas', 'tofu', 'cats']
testtest = ['apple']
print(comma_separator(test))
print(comma_separator(testtest))