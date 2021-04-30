
A=['Avion', 'Casa', 'Programacion', 'Aplicada', 'Juiciosa','Natural', 'Perro', 'Matematicas', 'Historia','Para', 'Avanza','Lucha', 'Revoluciona']
n=len(A)

p=[A[i] for i in range(n) if A[i].endswith('a')==True]
print(p)