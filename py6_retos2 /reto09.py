import random
print("  \nSUMA DE NUMEROS EN UN INTERVALO\n")

Num_Inicial=random.randint(0,2**10)
Num_Final=random.randint(0,2**10)
Intervalo=random.randint(0,10)
Suma=0

if Num_Final <= Num_Inicial:
  Num_Final+=Num_Inicial

else:
  print("Numero inicial: ",Num_Inicial,"\nNunmero Final: ",Num_Final,"\nIntervalo: ",Intervalo,"\n")

for i in range(Num_Inicial,Num_Final,Intervalo):
  print("•",i)
  Suma+=i

print("\nSuma: ",Suma)

