import random

messages = ['It is certain', 
'It is decidedly so', 
'Yes definitely', 
'Reply hazy try again later', 
'Ask again later', 
'Concentrate and ask again', 
'My reply is no', 
'Outlook not so good',
'Fucking Christ this is long']

while True:
  print('What is your question? (enter to exit)')
  answer = input()
  if answer == '':
    break
  else:
    print(messages[random.randint(0, len(messages) - 1)])

messages.append('hi you suck')
x = 1