
palabra= input('        PALÍNDROMOS        \nIngrese una palabra: ')

print(f'\nLa palabra tiene {len(palabra)} caracteres')
print(palabra[::-1])

if palabra==palabra[::-1]:
  print(f'La palabra {palabra} Si es un palíndromo')
else:
  print(f'La palabra {palabra} No es un palíndromo')