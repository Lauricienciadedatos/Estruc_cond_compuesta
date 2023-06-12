# Simulación de pago ingresando el importe y forma de pago:

Importe= float(input("Ingrese el importe a pagar: "))
Forma_pago= input("Ingrese forma de pago elegida:  ", "Contado" ,  "Tarjeta", "Débito")

# Contado (1): se aplica un descuento del 10% al importe 
# Tarjeta (2): se aplica un interés de 10%, 
# Débito (3): se aplica un descuento del 5%

Descuento_contado= (Importe * 0.1)
Interés_tarjeta= Descuento_contado
Descuento_débito= (Importe * 0.05)

Importe_Total_Contado= Importe - (Importe * 0.1)
Importe_Total_Tarjeta= Importe + (Importe * 0.1)
Importe_Total_Débito= Importe - (Importe * 0.05)

# Mostrar resultados

if Forma_pago: Contado
print("Importe: " Importe)
print("Descuento:$ " Descuento_contado)
print("Importe total:$ " Importe_Total_Contado)

elif Forma_pago: Tarjeta
   print("Importe:$  " Importe)
   print("Descuento:$ " Interés_tarjeta)
   print("Importe total:$ " Importe_Total_Tarjeta)

elif Forma_pago: Débito
   print("Importe:$ " Importe)
   print("Descuento:$ " Descuento_débito)
   print("Importe total:$ " Importe_Total_Débito)

else:
print("Forma de pago inválida")