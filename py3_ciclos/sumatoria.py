

def sumatoria_1(A,B,C):
  n = len(A)
  print(f'Cantidad de datos de las listas: {n}')
  print(f'Lista 1: {A}')
  print(f'Lista 2: {B}')
  print(f'Lista 3: {C}')
  sumatoria=0
  for i in range(n):
    a=A[i]*B[i]
    b=a+C[i]
    sumatoria +=b
  resultado= sumatoria+n**2  
  return resultado

A=[1,1,5,6,8]
B=[0,2,2,6,7]
C=[1,2,0,2,5]  

print(f'\nSumatoria = {sumatoria_1(A,B,C)}')