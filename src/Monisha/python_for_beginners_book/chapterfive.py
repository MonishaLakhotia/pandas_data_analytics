#Dictionaries
mycat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}

print(mycat['size'])

#Birthdays Example
"""
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name + '. ' \
            "\nDo you want to add their birthday to the database? \
            \n(type yes or no.)" )
        answer = input()
        if answer == 'yes':
            print('What is their birthday?')
            birthday = input()
            birthdays[name] = birthday
            print('Birthday database updated')
        else:
            print('Birthday database not updated')
            break
"""
#unblock out the above when you copy this to your version

#keys(), values(), items()
spam = {'color': 'red', 'age': 42}

print(spam.values())

print()

for v in spam.values():
    print(v)

print()

for k in spam.keys():
    print(k)

print()

for i in spam.items():
    print(i)

#list()

print(list(spam.keys())) #returns list of dict_keys datatype

for k, v in spam.items():
    print('Keys: ' + k + ' Values: ' + str(v))

#in or not in

print('color' in spam.keys())

print('color' not in spam.items())

print(42 in spam)

#get()
picnicitems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicitems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicitems.get('bananas', 0)) + ' bananas.')


#setdefault()
newdict = {'name': 'Pooka', 'age': 5}
newdict.setdefault('color', 'black') #use print to make this print the value at color
newdict.setdefault('color', 'white') #should return 'black' when printed because doesn't overwrite


message = 'It was a bright cold dat in April, and the clocks were stricking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
#i think i'll be able to use this for the fantasy game example

#Nested Dictionaries
all_guests = {'Alice' : {'apples': 5, 'pretzels': 12},
'Bob' : {'ham sandwiches': 3, 'apples': 2},
'Carol' : {'cups': 3, 'apple pie': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
        return num_brought

print('Number of things being brought:')
print(' - Apples  ' + str(total_brought(all_guests, 'apples')))
print(' - Cups  ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes  ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches  ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies  ' + str(total_brought(all_guests, 'apple pies')))

#I don't know why this one isn't working