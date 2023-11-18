import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def crear_matriz_M1(grafo):
    n = len(grafo)
    M1 = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i != j and grafo[i][j] != 0:
                M1[i][j] = 1
    return M1

def encontrar_caminos_hamiltonianos(M1, Mr, nodo_inicial, nodo_actual, camino_actual, caminos):
    if len(camino_actual) == len(Mr):
        caminos.append(camino_actual)
        return
    
    for siguiente_nodo in range(len(Mr)):
        if M1[nodo_actual][siguiente_nodo] and Mr[nodo_inicial][siguiente_nodo]:
            if str(siguiente_nodo) not in camino_actual:
                encontrar_caminos_hamiltonianos(M1, Mr, nodo_inicial, siguiente_nodo, camino_actual + str(siguiente_nodo), caminos)

def kaufmann_malgranger(grafo):
    n = len(grafo)
    M1 = crear_matriz_M1(grafo)
    r = 1
    Mr = M1.copy()

    matrices_intermedias = [Mr.copy()]  # Almacenar matrices intermedias para visualización

    while r < n - 1:
        Mr = np.dot(Mr, M1)
        matrices_intermedias.append(Mr.copy())
        r += 1

    caminos_hamiltonianos = {}
    for i in range(n):
        caminos = []
        for j in range(n):
            if Mr[i][j] != 0:
                encontrar_caminos_hamiltonianos(M1, Mr, i, j, str(i), caminos)
        caminos_hamiltonianos[f"Nodo {i}"] = caminos

    return caminos_hamiltonianos

# Ejemplo de matriz de adyacencia del grafo semi-hamiltoniano
grafo = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

caminos = kaufmann_malgranger(grafo)

# Visualización del grafo
G = nx.from_numpy_array(np.array(grafo))
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Grafo original')
plt.show()

# Mostrar caminos hamiltonianos por nodo
for nodo, caminos_nodo in caminos.items():
    print(f"{nodo}: {' '.join(caminos_nodo)}")