import random

print("\n     PROGRAMA QUE GENERA NUMERO ALEATORIO  ENTRE 1-120\n")

Num_Aleatorio=random.randint(1,121)
print("El numero escogido es: ",Num_Aleatorio,)

if (Num_Aleatorio < 10 ):
 print('\nEl numero es menor de 10')
elif (Num_Aleatorio <50):
 print('\nEl numero esta entre 10-50')
elif (Num_Aleatorio <100):
 print('\nEl numero esta entre 50-100')
else:
 print('\nEl numero es mayor que 100')