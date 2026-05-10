import random
def generar_camino(grafo, inicio, objetivo):
    nodo = inicio
    camino = [nodo]
    while nodo != objetivo and grafo.get(nodo):
        nodo = random.choice(grafo[nodo])[0]
        camino.append(nodo)
        if nodo not in grafo:
            break
        return camino
def fitness(camino, heuristica, objetivo):
    #Aqui vamos a evaluar el camino segun heuristica del ultimo nodo
    if camino[-1] == objetivo:
        return 0 #mejor posible
    return heuristica.get(camino[-1], float("inf"))

def crossover(camino1, camino2):#Combinamos 2 caminos en un punto aleatorio
    punto = min(len(camino1), len(camino2)) // 2
    return camino1[:punto] + camino2[punto:]

def mutacion(camino, grafo):#Cambiamos aleatoriamente un nodo por otro vecino
    if len(camino) > 1:
        idx = random.randint(1, len(camino)-1)
        nodo = camino[idx-1]
        if grafo.get(nodo):
            nuevo = random.choice(grafo[nodo])[0]
            camino[idx] = nuevo
    return camino

def algoritmo_genetico(grafo, inicio, objetivo, heuristica, poblacion_size=6, generaciones=10):
    #Generamos poblacion inicial
    poblacion = [generar_camino(grafo, inicio, objetivo) for _ in range(poblacion_size)]

    for _ in range(generaciones): #evaluamos fitness
        poblacion = sorted(poblacion, key=lambda c: fitness(c, heuristica, objetivo))
        if poblacion[0][-1] == objetivo:
            return poblacion[0], "Objetivo alcanzado"

        #seleccion de tomar los mejores
        nueva_poblacion = poblacion[:poblacion_size//2]

        #cruce y mutacion para jenerar nuevos individuos
        while len(nueva_poblacion) < poblacion_size:
            padres = random.sample(poblacion[:3], 2)
            hijo = crossover(padres[0], padres[1])
            hijo = mutacion(hijo, grafo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion
    return poblacion[0], "Generaciones maximas alcanzadas"
                        
grafo = {
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)]
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
camino, estado = algoritmo_genetico(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)
print("camino encontrado (Algoritmo genetico):",camino, "-", estado)
