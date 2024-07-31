#ordenar dos numeros ingresados por el usuario de menor a mayor
# nro1=int(input('Ingrese PrimerNro: '))
# nro2 =int(input('Ingrese SegundoNro: '))

# if nro1<nro2:
#     print(nro1, '➡️ ', nro2)
# elif nro1>nro2:
#     print(nro2, ' ->> ', nro1)
# else:
#     print('Son Iguales')

#ordenando 3 numeros
# numero1 = int(input("Ingrese un número: "))
# numero2 = int(input("Ingrese otro número: "))
# numero3 = int(input("Ingrese otro número: "))

# if numero1 > numero2:
#     if numero1 > numero3:
#         if numero2 > numero3:
#             print(f'{numero3}, {numero2}, {numero1}')
#         else:
#             print(f'{numero2}, {numero3}, {numero1}')
#     else:
#         print(f'{numero2}, {numero1}, {numero3}')
# else:
#     if numero2 > numero3:
#         if numero1 > numero3:
#             print(f'{numero3}, {numero1}, {numero2}')
#         else:
#             print(f'{numero1}, {numero3}, {numero2}')
#     else:
#         print(f'{numero1}, {numero2}, {numero3}')

# nro1=int(input('Ingrese PrimerNro: '))
# nro2=int(input('Ingrese SegundoNro: '))
# nro3=int(input('Ingrese TercerNro: '))
# if nro1<nro2 and nro1<nro3:
#     if nro2<nro3:
#         print(nro1, ' ->> ', nro2, '->> ', nro3)
#     else:
#         print(nro1, ' ->> ', nro3, '->> ', nro2)
# elif nro2<nro3 and nro2<nro1:
#     if nro1<nro3:
#         print(nro2, ' ->> ', nro1, '->> ', nro3)
#     else:
#         print(nro2, ' ->> ', nro3, '->> ', nro1)
# else:
#     if nro1<nro2:
#         print(nro3, ' ->> ', nro1, '->> ', nro2)
#     else:
#         print(nro3, ' ->> ', nro2, '->> ', nro1)

lista_numeros= []

while True:
    numero = input("Ingrese un número o 'fin' para terminar: ")
    if numero == 'fin':
        break
    lista_numeros.append(int(numero))

# lista_numeros.sort()
# lista_ordenada=sorted(lista_numeros)

#ordenamiento burbuja
for numPasada in range(len(lista_numeros)-1,0,-1):
    for i in range(numPasada):
        print(i)
        if lista_numeros[i]>lista_numeros[i+1]:
            temp = lista_numeros[i]
            lista_numeros[i] = lista_numeros[i+1]
            lista_numeros[i+1] = temp

print(lista_numeros)