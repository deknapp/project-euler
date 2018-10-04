shortcut_list = [3, 5, 6, 9, 10, 12, 15]
solution = 993 + 995 + 996 + 999
for i in range(0, 1000//15): 
  solution += sum([15*i + elem  for elem in shortcut_list])
print solution 
