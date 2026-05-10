import random

def online_search(grafo, inicio, objetivo, heuristica, max_iter=20):
    nodo = inicio
    camino = [inicio]
    visitados = set([nodo]) #Estados descubiertos

    for _ in range(max_iter):
        if nodo == objetivo:
            return camino, "objetivo alcanzado"

        vecinos = grafo.get(nodo,[])
        if not vecinos:
            return camino, "Atascado sin vecinos"

        vecinos_nuevos = [v for v in vecinos if v[0] not in visitados]#Simulamos descubrimientos: elegimos un vecino no visitado si existe
        if vecinos_nuevos:
            siguiente = min(vecinos_nuevos, key=lambda v: heuristica.get(v[0], float("inf")))
        else:
            siguiente = random.choice(vecinos)#Si ya se visitaron todos, elegimos uno aleatorio

            nodo = siguiente[0]
            camino.append(nodo)
            visitados.add(nodo)

    return camino, "Iteraciones maximas alcanzadas"   


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
camino, estado = online_search(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("Camino encontrado (Busqueda Online):", camino, "-", estado)
