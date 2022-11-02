x=int(input("Введите число\n"))
print("Ваше число",x)
a=x%2
print(a)
if a!=0:
  print("Плохо")
if x in range(2,6) and a==0:
  print("Неплохо")
if x in range(6,21) and a==0:
  print("Так себе")  
if x>20 and a==0:
  print("Отлично")  