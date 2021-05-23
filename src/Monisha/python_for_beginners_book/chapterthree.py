#Defining functions
def hello():
  print('Howdy!')
  print('Howdy!!!')
  print('Hello there.')
  print()

hello()
hello()
hello()

#Parameters
def hello(name):
  print('Hello ' + name)

hello('Alice')
hello('Bob')

import random

#Return Statement
def getanswer(answernumber):
  if answernumber == 1:
    return 'It is certain'
  elif answernumber == 2:
    return 'It is decidedly so'
  elif answernumber == 3:
    return 'Yes'
  elif answernumber == 4:
    return 'Reply hazy try again later'
  elif answernumber == 5: 
    return 'Ask again later'
  elif answernumber == 6:
    return 'Concentrate and ask again later'
  elif answernumber == 7:
    return 'My reply is no'
  elif answernumber == 8:
    return 'Outlook not so good'
  elif answernumber == 9:
    return 'I\'m over typing this.'
  
r = random.randint(1, 9)
fortune = getanswer(r)
print(fortune)

#Shortened version of bottom
print(getanswer(random.randint(1,9)))

#keyword arguments
print('Hello', end='')#no space
print('World')

print('Hello', end=' ')
print('World')

print('cats', 'dogs', 'mice', sep=',')#no space after comma

print('cats', 'dogs', 'mice', sep=', ')

#global statement
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

print()
#Try/Except statement
def spam(divideby):
  try:
   return 42/divideby
  except ZeroDivisionError:
    print('Error: Invalid Argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

print()
#alternate version of above
def spam(divideby):
  return 42/divideby

try:
  print(spam(2))
  print(spam(12))
  print(spam(0))
  print(spam(1))#this one will be skipped because the one before this has an error and code will go straight to except
except ZeroDivisionError:
  print('Error: Invalid Argument')