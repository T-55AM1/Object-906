import heapq  # Importamos heapq para manejar cola de prioridad (min-heap)

def a_star(grafo, inicio, objetivo, heuristica):  # Definimos la función A* con grafo, inicio, objetivo y heurística
    cola = [(heuristica[inicio], inicio, [inicio])]  # Cola con tupla: (f(n), nodo actual, camino recorrido)
    costos = {inicio: 0}                            # Diccionario para guardar el costo acumulado g(n)

    while cola:                                     # Mientras haya elementos en la cola
        f, nodo, camino = heapq.heappop(cola)       # Sacamos el nodo con menor f(n)

        if nodo == objetivo:                        # Si llegamos al objetivo
            return camino, costos[nodo]             # Regresamos el camino y el costo acumulado

        for vecino, peso in grafo.get(nodo, []):    # Recorremos vecinos del nodo actual
            nuevo_costo = costos[nodo] + peso       # Calculamos g(n) acumulado
            if vecino not in costos or nuevo_costo < costos[vecino]:  # Si es mejor camino
                costos[vecino] = nuevo_costo
                f_vecino = nuevo_costo + heuristica.get(vecino, 0)    # f(n) = g(n) + h(n)
                heapq.heappush(cola, (f_vecino, vecino, camino + [vecino]))  # Agregamos a la cola

    return None, float("inf")                       # Si no se encuentra solución

# Grafo con pesos (tu grafo corregido)
grafo = {
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)],
    'F_GUADALAGARA': [],
    'KIDSANIA': [],
    'PUMA': [],
    'CHARLI': [],
    'ESTACIONAMIENTO': []
}

# Heurística definida para el objetivo GOMBILL
heuristica = {
    'APPLE_STORE': 7,
    'MACDONALS': 6,
    'ZONA_COMIDA': 4,
    'MINISO': 5,
    'GOMBILL': 0,
    'F_GUADALAGARA': 9,
    'KIDSANIA': 10,
    'PUMA': 8,
    'CHARLI': 7,
    'ESTACIONAMIENTO': 0
}

# Ejecutamos A* desde APPLE_STORE hasta GOMBILL
camino, costo = a_star(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("Camino encontrado (A*):", camino, "con costo:", costo)
