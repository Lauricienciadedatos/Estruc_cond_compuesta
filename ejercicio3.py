# Leer tres números.
número1= int(input("Ingrese el primer número "))
número2= int(input("Ingrese el segundo número "))
número3= int(input("Ingrese el tercer número "))

# Mostrar cuál es el número mayor y determinar si es par o impar.

mayor= max(número1, número2, número3)

print("El número mayor es:",mayor)
if mayor % 2 == 0:
    print("El número mayor es par.")
else:
    print("El número mayor es impar.")    