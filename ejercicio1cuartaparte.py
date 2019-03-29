def a_power_b (a,b):
  
  cont=1
  
  for i in range (0,b):
    
    if i>=1000:
      raise(  StopIteration ("Error en el valor"))
    
    cont=cont*a
  
  return cont
contadorpar=0
contadorimpar=0
contador_de_error=0
while True:
  
  try:
  
    x=int(input("Ingrese la base "))
    if x== 0:
      contador_de_error+=1
      print("Nos vemos!")
      break
    
    y=int(input("Ingrese el exponente "))
    ac= a_power_b(x,y)
    print(ac)
    
    if ac%2==0:
     contadorpar+=1
    else:
      contadorimpar+=1
  
  except StopIteration:
    contador_de_error+=1
    print("Es de grande")
    
  except ValueError:
    contador_de_error+=1
    print("No se permiten letras")
  
  
print("la cantidad de pares es",contadorpar )
print("la cantidad de imapares es",contadorimpar)
print("la cantidad de errores es",contador_de_error)      
  