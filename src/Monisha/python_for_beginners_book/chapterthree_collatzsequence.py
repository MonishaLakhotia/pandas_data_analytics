print('Enter number:')

def collats(number):
  if number % 2 == 0: #if number is even, return this value
    return number // 2
  elif number % 2 == 1: #if number is odd, return 3*number
    return 3 * number + 1

#allow user to enter number until they hit 1
while True:
  try:
    number = int(input())
  
    print(collats(number)) #prints return value for collats

    if collats(number) == 1:
      break
  except ValueError: #if non integer entered
    print('You must enter an integer.')