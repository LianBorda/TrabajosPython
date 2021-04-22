
nombre = input('\n               Índice de masa corporal\n\nIngrese su nombre: ')

estatura= float(input('Ingrese su estatura en m: '))
peso= int(input('Ingrese su peso en Kg: '))

def IMC(x,y):
  IMC=x/(y**2)
  print(f'\n{nombre}')
  print(f'Su IMC es: {IMC}\n\n')
  print(Tabla())
  return IMC

def Tabla():
  x=('            IMC                   NIVEL DE PESO\n      Por debajo de 18.5	Bajo peso\n        18.5 – 24.9	        Normal\n        25.0 – 29.9	        Sobrepeso\n        30.0 o más	        Obeso')
  return x

IMC(peso,estatura)

