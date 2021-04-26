import random

def LLenar_lista(A,B):
  n=len(A)//2
  C=[]
  for i in range(n):
    a= (A[i+1])**2
    b= a*B[2*i]
    f=b+B[n+i]
    C.append(f)
  return C

A=[0,1,5,9,7,6,8,2]
B=[4,9,3,5,8,7,5,1]

print(f'Nueva lista C:\n{LLenar_lista(A,B)}')