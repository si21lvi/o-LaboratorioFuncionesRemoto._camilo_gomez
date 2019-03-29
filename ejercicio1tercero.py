def a_power_b (a,b):
  cont=1
  
  for i in range (0,b):
    
    if i>=1000:
      raise(  StopIteration ("Error en el valor"))
    
    cont=cont*a
  
  return cont
 
while True:
  
  try:
  
    x=int(input("Ingrese la base "))
    
    if x== 0:
      print("Nos vemos!")
      break
    
    y=int(input("Ingrese el exponente "))
    ac= a_power_b(x,y)
    print(ac)
  
  except StopIteration:
     print("Es demasiado grande")
    
  except ValueError:
      print("No se permiten letras")
  
  except:
      print("Error no conocido")
