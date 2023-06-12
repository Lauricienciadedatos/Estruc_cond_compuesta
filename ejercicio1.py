# Introducir los lados de un triángulo 
ladoA= int(input("Ingresa la longitud del lado A "))
ladoB= int(input("Ingresa la longitud del lado B "))
ladoC= int(input("Ingresa la longitud del lado C "))

# visualizar por pantalla que tipo de triángulo es
if ladoA ==  ladoB == ladoC:
    print("El triángulo es equilátero.")

elif ladoA == ladoB  or ladoA == ladoC  or ladoB == ladoC:
    print("El triángulo es Isósceles.")

else:
    print("El triángulo es escaleno.")
  
