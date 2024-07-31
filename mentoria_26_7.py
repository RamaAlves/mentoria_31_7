# # Ejercicio 3
# Vamos a crear un programa en python donde vamos a declarar un diccionario 
# para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido 
# y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
# Extra crear una lista con el total de la compras.


# precio_frutas = {"manzana": 3200, "pera": 4090, "uva": 5010, "sandia": 7340, "anana": 5990, "mandarina": 3000}
# lista_de_compras = {}
# print(">>> Bienvenido a la Frutería mas frutosa de la fruta vida <<<")
# print("Presione enter para continuar")
# ingreso = input()
# while ingreso == "":
#     print(" >>> MENU <<< ")
#     print("manzana")
#     print("uva")
#     print("sandia")
#     print("pera")
#     print("anana")
#     print("mandarina")
#     fruta= input(" Que fruta quieres comprar: \n")
#     fruta_elegida = fruta.lower()
#     if fruta_elegida in precio_frutas:
#         cantidad = int(input('introducza la cantidad de frutas: '))
#         total = precio_frutas[fruta_elegida] * cantidad
#         print(f'Fruta: {fruta_elegida}\tCantidad: {cantidad}\nEl total a pagar es: ${total}')
#         if fruta_elegida in lista_de_compras:
#             lista_de_compras[fruta_elegida]+=total
#         else:
#             lista_de_compras[fruta_elegida]=total
#     else:
#         print("Error!\n no se encontro la fruta seleccionada.")
#     print("Presione enter para continuar\nPresione 0 para salir!")
#     ingreso = input()
# print('Usted compró: ',lista_de_compras)
# total_compra=0
# for item in lista_de_compras:
#     total_compra+=lista_de_compras[item]
# print('El total de su compra fue de: $',total_compra)


#ABM fruteria
 
precio_frutas = {"manzana": 3200, "pera": 4090, "uva": 5010, "sandia": 7340, "anana": 5990, "mandarina": 3000}
lista_de_compras = {}
print(">>> Bienvenido a la Frutería mas frutosa de la fruta vida <<<")
print("Presione enter para continuar")
ingreso = input()
while ingreso == "":
    #Menu
    print("1. Alta") #agregar frutas al diccionario
    print("2. Baja") #eliminar fruta del diccionario
    print("3. Modificación") #altualizar el precio de una fruta en el diccionario
    print("4. Mostrar") #mostrar las frutas en el diccionario
    print("5. Comprar") #permite comprar frutas
    print("0. Salir")
    
    ingreso = input()
    
    #Alta
    if ingreso == '1':
        print('Elegiste ALTA')
        frutaNueva=str(input('Cual es la fruta nueva? '))
        if frutaNueva in precio_frutas:
            print ('Existe, vaya a otra opcion')
        else:
            precioNuevo=float(input('Ingrese precio: '))
            precio_frutas[frutaNueva]=precioNuevo
    
    #Baja
    elif ingreso == '2':
        print('Elegiste BAJA')
        frutaBaja=str(input('Cual es la fruta a eliminar? '))
        if frutaBaja in precio_frutas:
            del precio_frutas[frutaBaja]
            print(precio_frutas)
        else:
            print ('No Existe, vaya a otra opcion')
    
    #Modificación
    elif ingreso == '3':
        nombre_fruta = input('ingrese nombre de fruta: ')
        if nombre_fruta in precio_frutas:
            precio_fruta = int(input("ingrese el precio de la fruta: "))
            precio_frutas[nombre_fruta] = precio_fruta
            print(precio_frutas)
        else:
            print("no se encuentra la fruta")    
    
    #Mostrar
    elif ingreso == '4':
        print(precio_frutas)
    
    #Comprar
    elif ingreso == "5":
        fruta= input(" Que fruta quieres comprar: \n")
        fruta_elegida = fruta.lower()
        if fruta_elegida in precio_frutas:
            cantidad = int(input('introducza la cantidad de frutas: '))
            total = precio_frutas[fruta_elegida] * cantidad
            print(f'Fruta: {fruta_elegida}\tCantidad: {cantidad}\nEl total a pagar es: ${total}')
            if fruta_elegida in lista_de_compras:
                lista_de_compras[fruta_elegida]+=total
            else:
                lista_de_compras[fruta_elegida]=total
        else:
            print("Error!\n no se encontro la fruta seleccionada.")
    elif ingreso=="0":
        break
    
    # Volver a ejecutar el programa o salir
    print("Presione enter para continuar")
    print("Ingrese 0 para salir")
    ingreso = input()

#Mostrar lista de elementos comprados
if len(lista_de_compras)>0:
    print('Usted compró: ',lista_de_compras)
    total_compra=0
    for item in lista_de_compras:
        total_compra+=lista_de_compras[item]
    print('El total de su compra fue de: $',total_compra)

#Despedida
print("Gracias vuelvas prontos! ")