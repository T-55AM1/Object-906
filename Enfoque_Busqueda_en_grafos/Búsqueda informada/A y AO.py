import heapq#para la cola

def a_star(grafo, inicio, objetivo, heuristica):
    cola = [(heuristica[inicio], inicio, [inicio])]#(f(n), nodo, camino)
    costos = {inicio: 0}#g(n) acumulado

    while cola:
        f, nodo, camino = heapq.heappop(cola)# Nodo con menor f(n)

        if nodo == objetivo:
            return camino, costos[nodo]#Camino y costo acumulado

        for vecino, peso in grafo.get(nodo, []):
            nuevo_costo = costos[nodo] + peso
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                f_vecino = nuevo_costo + heuristica.get(vecino, 0)
                heapq.heappush(cola,(f_vecino, vecino, camino + [vecino]))
    return None, float("inf")
# Grafo con pesos
grafo = {
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)],
}

# Heurística para GOMBILL
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
}

camino, costo = a_star(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("Camino encontrado (A*):", camino, "con costo:", costo)

grafo_and_or = {
    'APPLE_STORE': [('MACDONALS', 'OR')],  # corregido guion bajo
    'MACDONALS': [('ZONA_COMIDA', 'AND'), ('F_GUADALAGARA', 'AND')],
    'ZONA_COMIDA': [('GOMBILL', 'OR'), ('MINISO', 'OR')],
    'MINISO': [('KIDSANIA', 'AND'), ('PUMA', 'AND'), ('CHARLI', 'AND')],
    'GOMBILL': [('ESTACIONAMIENTO', 'OR')]
}
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

def ao_star(grafo, nodo,heuristica):
    if not grafo.get(nodo):
        return [nodo]
    mejor_camino = None
    mejor_costo = float("inF")

    for hijo, tipo in grafo[nodo]:
        if tipo == 'OR':
            camino = ao_star(grafo, hijo, heuristica)
            costo = heuristica[hijo]
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_camino = [nodo] + camino
        elif tipo == 'AND':
            camino = ao_star(grafo, hijo, heuristica)
            costo = heuristica[hijo]
            if mejor_camino is None:
                mejor_camino = [nodo] + camino
                mejor_costo = costo
            else:
                mejor_camino += camino
                mejor_costo += costo

    return mejor_camino
print("Camino encontrado (A0*):", ao_star(grafo_and_or, 'APPLE_STORE', heuristica))
