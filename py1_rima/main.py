print('Hola mundo')

archivo = open('palabras500.csv' , encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

def rima(terminacion_de_la_palabra):
  ctda_terminacion=len(terminacion_de_la_palabra)  
  for i in lineas:    
    if len(i)>ctda_terminacion:      
      if i[-ctda_terminacion-1:]==terminacion_de_la_palabra+'\n':
        print(i)
        palabra = i
        print(palabra)                 
     

rima('e')



 