
año = int(input('\n____PROGRAMA QUE DICE SI UN AÑO ES BISIESTO O NO_____\n\nIngrese un año: '))

def mul4(año):
  mult=año%4 
  return(mult)

def term00(año):
  term=año%100
  return(term)

def mult400(año):
  mul400=año%400
  return (mul400)   

def msjAñoB():
  mjs_1=('Si es un año Bisiesto')
  return(mjs_1)

def msjAñoNoB():
  mjs_2=('No es un año Bisiesto')  
  return(mjs_2)



if mul4(año)==0 and term00(año)==0 and mult400(año)==0:
  print(msjAñoB())
elif mul4(año)==0 and term00(año)==0:
  print(msjAñoNoB())
elif mul4(año)==0:
  print(msjAñoB())
else:
  print(msjAñoNoB())    




