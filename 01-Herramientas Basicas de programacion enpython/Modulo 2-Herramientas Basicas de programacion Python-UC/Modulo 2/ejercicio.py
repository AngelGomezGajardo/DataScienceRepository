def suma(x):
  l = len(x)
  if l == 0:
    return 0
  else:
    last = x.pop()
    print(last, x)
    return suma(x) + last

print(suma([7, 4, 23]))
print ('=' * 15)
print(suma([1,2,3,4,5]))