def a_power_b(a, b):
  
  contador=1
  for i in range(0, b):
   contador=contador*a
  
  return contador


x=int(input("ingrese el numero bro"))
y=int(input("ingrese el segundo numero"))


que= a_power_b(x,y)
print(que)