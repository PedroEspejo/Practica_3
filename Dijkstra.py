import sys

# Función para encontrar el nodo no visitado con la distancia mínima
def nodo_no_visitado_con_distancia_minima(distancias, visitados):
    min_distancia = sys.maxsize
    min_nodo = None
    for nodo in distancias:
        if distancias[nodo] < min_distancia and not visitados[nodo]:
            min_distancia = distancias[nodo]
            min_nodo = nodo
    return min_nodo

# Función para mostrar el camino más corto
def mostrar_camino_mas_corto(distancias, padres, nodo_destino):
    camino = []
    while nodo_destino is not None:
        camino.insert(0, nodo_destino)
        nodo_destino = padres[nodo_destino]
    return camino

# Función principal de Dijkstra
def dijkstra(grafo, nodo_inicio, nodo_destino):
    distancias = {nodo: sys.maxsize for nodo in grafo}
    padres = {nodo: None for nodo in grafo}
    visitados = {nodo: False for nodo in grafo}
    distancias[nodo_inicio] = 0

    for _ in grafo:
        nodo_actual = nodo_no_visitado_con_distancia_minima(distancias, visitados)
        if nodo_actual is None:
            break
        visitados[nodo_actual] = True

        for vecino, peso in grafo[nodo_actual].items():
            if not visitados[vecino]:
                distancia_alternativa = distancias[nodo_actual] + peso
                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    padres[vecino] = nodo_actual

        # Muestra el progreso en la consola
        print(f"Nodo actual: {nodo_actual}")
        print("Distancias:", distancias)
        print("Padres:", padres)
        print()

    camino_mas_corto = mostrar_camino_mas_corto(distancias, padres, nodo_destino)
    return camino_mas_corto

# Grafo de ejemplo (representado como un diccionario de diccionarios)
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

nodo_inicio = 'A'
nodo_destino = 'D'

print("Ejecutando el algoritmo de Dijkstra paso a paso:\n")
camino_mas_corto = dijkstra(grafo, nodo_inicio, nodo_destino)
print("\nCamino más corto:", camino_mas_corto)
