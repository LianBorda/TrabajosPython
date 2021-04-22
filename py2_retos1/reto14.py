
n=-10
def cuadrado(n):
  y=n**2
  return(y)

def fin():
  msj=('Programa finalizado')
  return(msj)

while n<11:
  if n>=0:
    print(f'  {n}^2 = {cuadrado(n)}')
    n=n+1
  else:
    print(f' {n}^2 = {cuadrado(n)}')
    n=n+1

print(fin())