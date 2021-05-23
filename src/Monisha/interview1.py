def get_message(i):
  if i % 2 == 0 and i % 3 == 0:
    return 'WeeWoo'
  elif i % 2 == 0:
    return 'Wee'
  elif i % 3 == 0:
    return 'Woo'
  else:
    return None

for i in range(1, 10):
  message = get_message(i)
  if message is not None:
    print(message)

x = print('Hello world')

print(x)