def tabu_search(grafo, inicio, objetivo, heuristica, max_iter=20, tabu_size=5):
    nodo = inicio
    camino =[nodo]
    tabu_list = set([nodo])#Lista tabu inicial con el nodo de partida

    for _ in range(max_iter):#Limitamos el numero de iteraciones
        if nodo == objetivo:
            return camino, "Objetivo alcanzado"
        
        vecinos = grafo.get(nodo, [])
        if not vecinos:
            return camino, "Atascado sin vecinos"

        vecinos_validos = [v for v in vecinos if v[0] not in tabu_list]#Filtramos vecinos que no esten el la lista tabu
        if not vecinos_validos:
            return camino, "Atascado por lista tabu"
        
        mejor_vecino = min(vecinos_validos, key=lambda v: heuristica.get(v[0], float("inf")))
        nodo = mejor_vecino[0]
        camino.append(nodo)

        tabu_list.add(nodo)#Actualizamos la lista tabu
        if len(tabu_list) > tabu_size: #Si exede el tamaño, eliminamos el mas antiguo
            tabu_list.pop()

    return camino, "Iteracciones maximas alcanzadas"

grafo = {#el grafo
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)],
}

# Heurística 
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

camino, estado = tabu_search(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)#Ejecutamos el tabu search
print("Camino encontrado (Tabu Search):", camino, "-", estado)
