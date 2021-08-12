import matplotlib.pyplot as plt

lista =[]
numero = 17

while numero != 1: 

  lista.append(numero)
  if  numero % 2 == 0:
        numero=numero // 2
        
  else: 
        numero= numero *3 +1
        

print("la lista de numero es :",lista)
plt.plot(lista)
plt.ylabel('sala')
plt.show()