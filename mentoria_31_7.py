# '''Crear un sistema que dado un número genere una sucesión de fibonacci con esa cantidad 
# de números en la sucesion, por ejemplo: 3 -> 0,1,1 o 5 -> 0,1,1,2,3'''

# numero = int(input("Ingrese un número: "))
# lista_fibonacci = [0, 1]

# if numero == 0:
#     print("La sucesion debe contener al menos un número")
# elif numero == 1:
#     print(lista_fibonacci[0])
# elif numero == 2:
#     for i in range(len(lista_fibonacci)):
#         if i == (len(lista_fibonacci) -1):
#             print(f'{lista_fibonacci[i]}', end='')
#         else:
#             print(f'{lista_fibonacci[i]}, ', end='')
# else:
#     for i in range(2, numero):
#         numero_nuevo = lista_fibonacci[i - 1] + lista_fibonacci[i - 2]
#         lista_fibonacci.append(numero_nuevo)

#     #seccion repetida
#     for i in range(len(lista_fibonacci)):
#         if i == (len(lista_fibonacci) -1):
#             print(f'{lista_fibonacci[i]}', end='')
#         else:
#             print(f'{lista_fibonacci[i]}, ', end='')

# Actividades extra: como optimizarias este codigo?


# def fibo(n):
#     fibo_list = [0,1]
#     if n == 0:
#         return []
#     elif n == 1:
#         return fibo_list[n-1]
#     else:
#         for i in range(1,n-1):
#             siguiente = fibo_list[i-1] + fibo_list[i]
#             fibo_list.append(siguiente)
#     return fibo_list

# print(fibo(0))
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))

# def fibonacci(n):
#     x = [0,1]
#     if n<=0:
#         return[]
#     elif n==1:
#         return[0]
#     elif n==2:
#         return[0,1]
#     else:
#         for i in range(n-2):
#             x.append(x[-1]+x[-2])
#     return x

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))