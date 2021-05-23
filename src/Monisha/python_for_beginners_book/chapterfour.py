#List + list indexing
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print('Hello, ' + spam[0])
print(spam[-1])
print(spam[1:4])
print(spam[2:])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][:3])

#Len
print(len(spam))

#changing value at index
spam[1] = 'new value'
print(spam)

#list concatenation and list replication
print([1, 2, 3] + ['A', 'B', 'C'])
print([1, 2, 3] * 3)

spam = [0, 1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

print()
#del statement
del spam[3]
print(spam)
del spam[3]
print(spam)

print()
#Working with lists
catnames = []

while True:
  print('Enter name of cat ' + str(len(catnames) + 1) + ' (Or enter nothing to stop):')
  name = input()
  if name == '':
    break
  catnames = catnames + [name]

print('The cat names are:')
for name in catnames:
  print(' ' + name) #space is so they indent when they list out

#in and not in operator
print('howdy' in ['hello', 'hi', 'howdy', 'hola'])
print('cat' not in spam)

mypets = ['Ashely', 'Mary', 'Cassandra']
print('Enter a pet name:')
name = input()
if name not in mypets:
  print('I do not have a pet named ' + name)
else:
  print(name + ' is my pet')

#multiple assignment
cat = ['fat', 'black', 'mean']
size, color, disposition = cat #do this instead of manually assigned each index to a variable

print(disposition) #prints variable size (which stores 'fat')

#listname.index()
print(cat.index('mean')) #returns index for value in list cat

#listname.append()
spam.append('append')
print(spam)

#listname.insert()
spam.insert(1, 'insert')
print(spam)

#listname.remove()
spam.remove('insert')
print(spam)

#listname.sort()
sorttest = ['Ashley', 'Graham', 'Junessa', 'Estelle', 'Jodi']
sorttest.sort()
print(sorttest)
sorttest.sort(reverse = True)
print(sorttest)