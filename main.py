import networkx as nx
import numpy as np
print("Ingrese la cantidad de vertices del Grafo #1: ")
n = int(input())
print("Ingrese la cantidad de aristas del Grafo #2: ")
m = int(input())
if (m != n):
    print("Los grafos no son isomorfos")
else:
    #por medio de la lectura de las matrices de adyacencia se dice si son isomorfos o no sin usar funciones de networkx
    print("Ingrese la matriz de adyacencia del Grafo #1: ")
    matriz1 = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = int(input(f"Ingrese el elemento en la fila {i+1}, columna {j+1}: "))
            fila.append(elemento)
        matriz1.append(fila)
    print("Ingrese la matriz de adyacencia del Grafo #2: ")
    matriz2 = []
    for i in range(m):
        fila = []
        for j in range(m):
            elemento = int(input(f"Ingrese el elemento en la fila {i+1}, columna {j+1}: "))
            fila.append(elemento)
        matriz2.append(fila)
    #se crea el grafo 1
    G1 = nx.Graph()
    for i in range(n):
        G1.add_node(i)
    for i in range(n):
        for j in range(n):
            if (matriz1[i][j] == 1):
                G1.add_edge(i, j)
    #se crea el grafo 2
    G2 = nx.Graph()
    for i in range(n):
        G2.add_node(i)
    for i in range(n):
        for j in range(n):
            if (matriz2[i][j] == 1):

                G2.add_edge(i, j)

   
    #se eleva al cuadrado la matriz de adyacencia del grafo 1
    #np es una libreria que permite trabajar con matrices
    matriz1 = np.array(matriz1)
    #dot es una funcion que permite multiplicar matrices
    matriz1 = np.dot(matriz1, matriz1)
    
    #se eleva al cuadrado la matriz de adyacencia del grafo 2
    matriz2 = np.array(matriz2)
    matriz2 = np.dot(matriz2, matriz2)
    #se crea un vector con los datos de la diagonal principal de la matriz 1
    vector1 = []
    for i in range(n):
        vector1.append(matriz1[i][i])
    #se crea un vector con los datos de la diagonal principal de la matriz 2
    vector2 = []
    for i in range(n):
        vector2.append(matriz2[i][i])
    #se ordenan los vectores de mayor a menor
    vector1.sort(reverse=True)
    vector2.sort(reverse=True)
    #se verifica si son iguales
    if (vector1 == vector2):
        print("Los grafos son isomorfos")
    else:
        print("Los grafos no son isomorfos")

    


    


