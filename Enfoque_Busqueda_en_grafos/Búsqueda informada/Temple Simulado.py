import math, random

def simulated_annealing(grafo, inicio, objetivo, heuristica, temp_inicial=100, enfriamiento=0.9, max_iter=50):
    nodo = inicio
    camino = [nodo]
    temp = temp_inicial

    for _ in range(max_iter):
        if nodo == objetivo:
            return camino, "Objetivo alcanzado"

        vecinos = grafo.get(nodo, [])
        if not vecinos:
            return camino, "Atascado si vecinos"

        vecino, _ = random.choice(vecinos)
        h_actual = heuristica.get(nodo, float("inf"))
        h_vecino = heuristica.get(vecino, float("inf"))

        delta = h_vecino - h_actual

        if delta < 0 or ramdom.ramdom() < math.exp(-delta / temp):
            nodo = vecino
            camino.append(nodo)

            temp *= enfriamiento

            return camino, "Iteraciones maximas alcanzadas"
    

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

camino, estado = simulated_annealing(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("Camino encontrado: ",camino, "-", estado)
