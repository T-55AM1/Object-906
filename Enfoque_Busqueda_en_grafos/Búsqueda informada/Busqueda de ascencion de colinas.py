def hill_climbing(grafo, inicio, objetivo, heuristica):
    nodo = inicio #empezamos por el nodo inicial
    camino = [nodo] #guardamos el cambio recorrido

    while nodo != objetivo:#mientras no llegemos al objetivo
        vecinos = grafo.get(nodo, [])#obtenemos los vecinos del nodo actual
        if not vecinos: #Si no hay vecinos
            return camino, "Atascado en el maximo local"#nos excusamos


        mejor_vecino = min(vecinos, key = lambda v: heuristica.get(v[0], float("inf"))) #Selecionamos el mejor vecino solo por tener menor Heuristica
        nodo = mejor_vecino[0]#Avanzamos al mejor vecino
        camino.append(nodo)#lo agregamos al camino
        
        if nodo == objetivo: #Si alcanzamos el objetivo
            return camino, "objetivo alcanzado"# Lo decimos
grafo = {
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

camino, estado = hill_climbing(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("Camino encontrado (Hill Climbing):", camino, "-", estado)
