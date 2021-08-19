print("\n PROGRESION GEOMETRICA (Tablero de agedrez)\n")

Cant_Casillas_tablero=8*8
Casilla=1
Gran_de_trigo=1

print("||   Casilla    ||   Granos de Trigo   ||\n----------------------------------------")

for i in range(1,Cant_Casillas_tablero+1,1):
  print("||      ",Casilla,"              ",Gran_de_trigo)
  Casilla+=1
  Gran_de_trigo*=2