#Boolean - T/F
spam = True
print(spam)

#Comparison Operators
print(48 == 42) #equal to
print(48 != 42) #notequalto
print(48 < 42) #less than
print(48 > 42) #greater than
print(2 >= 2) #greater than or equal to
print(2 <= 8) #less than or equal to 

print()
print()

#with strings
print('hello' == 'hello')
print('hello' != 'Hello')

#with variables
eggs = 5
print(eggs == 5)
print(eggs >= 8)

print()
print()

#Boolean Operators
print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not not not not True)

print()
print()

#Boolean and Comparison Operators Mixed
print((4 < 5) and (5 < 6))
print((4 == 5) or (1 ==2))

#multiple Boolean
print((2 + 2 == 4) and not (2 + 2 ==5))
print(True and not False)
print((2 + 2 == 4) and not (2 + 2 == 4))

print()
print()

#blocks of code
#if name == 'Mary':
  #print('Hello Mary')
  #if password == 'swordfish':
    #print('Access Granted.')
  #else:
    #print('Wrong Password.')
  
#if vs while statement
spam = 0
if spam < 5:
  print('Hello world!')
  spam = spam + 1

print()
spam = 0
while spam < 5:
  print('Hello world!')
  spam = spam + 1

#name = ''
#while name != 'your name':
  #print('Please type your name.')
  #name = input()
#print('Thank you!')

print()
print()

#break statement
#while True:
  #print('Please type your name.')
  #name = input()
  #if name == 'your name':
    #break
#print('Thank you!')

print()
print()

#continue statement
#while True:
  #print('Who are you?')
  #name = input()
  #if name != 'Joe':
    #continue
  #print('Hello, Joe. What is the password? (It is a fish.)')
  #password = input()
  #if password == 'swordfish':
    #break
#print('Access granted.')

print()
print()

#for loop and range()
print('My name is')
for i in range (5):
  print('Jimmy Five Times (' + str(i) + ')')

print()
total = 0
for num in range(101):
  total = total + num
print(total)

#Jimmy statement as while
print('My name is')
i = 0
while i < 5:
  print('Jimmy Five Times(' + str(i) + ')')
  i = i + 1
#note this is less concise than for + range()

##9 quiz question
print('Type a number between 1 and 5:')
spam = input()
if int(spam) == 1:
  print('Hello')
elif int(spam) == 2:
  print('Howdy')
else:
  print('Greetings!')

print()
##10 quiz question
#for loop
for i in range(1, 11):
  print(i)

#while loop
i = 1
while i <= 10:
  print(i)
  i = i + 1