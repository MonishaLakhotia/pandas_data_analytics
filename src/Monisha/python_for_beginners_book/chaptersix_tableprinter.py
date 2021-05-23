#takes list of strings and displays it in an organized list

table_data = [['apples', 'oranges', 'cherries', 'bananas'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def table(list):
  col_widths = [0] * len(list)
  for i in range(len(list)):
    for x in list[i]:
      if len(x) > col_widths[i]:
        col_widths[i] = len(x)
  print(col_widths)

  for i in range(len(list[0])):
    for x in range(len(list)):
      if x == len(list) - 1:
        print(list[x][i].rjust(col_widths[x], ' '))
      else:
        print(list[x][i].rjust(col_widths[x], ' '), end = ' ')


table(table_data)
