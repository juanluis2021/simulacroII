def matriz1():
    filas = int(input("Dame el numero de filas que quieras: "))
    columnas = int(input("Dame el numero de columnas que quieras: "))

    if filas == columnas: 

        matriz = []
        #Por cada elemento en de filas que pidamos 
        for i in range(filas):
            #Construimos un matriz vacia y reservamos la posciones
            matriz.append([] * columnas)
            #Por cada elemento en el rango de columnas
            for k in range(columnas):
                numero = int(input("Fila {}, columna{}: :".format(i + 1, k+1))) #En este caso i y k hacen de indice
                #Guardamos en la poscion de la fila el numero
                print(numero)
                matriz[i].append(numero)
               # print(matriz[i].append(numero))
        print()
        for fila in matriz:
            print("[", end=" ")
            for elemento in fila:
                print(elemento, end=" ")
            print("]")
        print()
    else:
        print("Bruuu, la matriz tiene que ser cuadrada")
matriz1()