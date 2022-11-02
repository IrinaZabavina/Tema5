x=int(input("Введите число\n"))
print("Ваше число",x)
a=x%3
b=x%5
if a==0 and b==0:
  print("Fizz Buzz")
else:  
    if a==0:
      print("Fizz")
    if b==0:
      print("Buzz")
if a!=0 and b!=0:
   print(x)