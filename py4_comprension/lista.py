
A=[4,5,6,1,2,6,7,22,63,1]
B=[2,5,8,5,1,2,5,8,9,1]

n=len(A)//2
C=[((A[i+1]**2)*B[2*i])+B[n+i] for i in range(n)]
print(f'Nueva lista: {C}')