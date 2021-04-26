

def sumatoria_1(A,B,C):
  n = len(A)
  sumatoria=0
  for i in range(n):
    a=A[i]*B[i]
    b=a+C[i]
    sumatoria +=b
  resultado= sumatoria+n**2  
  return resultado

A=[1,1]
B=[0,2]
C=[1,2]  
