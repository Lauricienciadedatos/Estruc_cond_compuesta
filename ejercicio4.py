# Ingresar un número del 1 al 7 e indicar el día de la semana correspondiente.

numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1: 
 print("El número", numero, "corresponde al día lunes.")
   
elif numero == 2:
 print("El número", numero, "corresponde al día martes.")

elif numero == 3:
 print("El número", numero, "corresponde al día miércoles.")

elif numero == 4:
    print("El número", numero, "corresponde al día jueves.")

elif numero == 5:
    print("El número", numero, "corresponde al día viernes.")

elif numero == 6:
    print("El número", numero, "corresponde al día sábado.")

elif numero == 7:
    print("El número", numero, "corresponde al día domingo.")

else:
    print("Número inválido. Debe ingresar un número del 1 al 7.")




