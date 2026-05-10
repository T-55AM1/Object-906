def local_beam_search(grafo, inicio, objetivo, heuristica, k=2, max_iter=20):

    estados = [(inicio, [inicio])]#Iniciamos el haz con el nodo inicial

    for _ in range(max_iter):

        for nodo, camino in estados:#Si alguno de los estados llega al objetivo, lo devolvemos
            if nodo == objetivo:
                return camino, "objetivo alcamzado"

        sucesores = [] #Generamos todos los sucesores de los estados actuales
        for nodo, camino in estados:
            for vecino, _ in grafo.get(nodo, []):
                nuevo_camino = camino + [vecino]
                sucesores.append((vecino, nuevo_camino))
        if not sucesores:
            return estados[0][1],"Sin sucesores,busqueda detenida"
        
        estados = sorted(sucesores, key=lambda x: heuristica.get(x[0], float("inf")))[:k]
        # aqui arriba seleccionamos a los mejores k sucesores segun la heuristica
    return estados[0][1], "Iteraciones maximas alcanzadas"
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
grafo = {
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)]
}
camino, estado = local_beam_search(grafo, 'APPLE_STORE','GOMBILL', heuristica, k=2)
print("Camino encontrado (Local Beam Search):", camino, "-", estado)
