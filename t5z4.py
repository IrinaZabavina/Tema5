a = str(input())
def x(a):
  b = ""
  for i in a:
    if i.isupper() == True:
      b=b+i
  print(b)
x(a)