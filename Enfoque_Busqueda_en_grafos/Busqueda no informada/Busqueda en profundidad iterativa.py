def dls(grafo, inicio, objetivo, limite):  # Función auxiliar: DFS con límite de profundidad
    pila = [(inicio, [inicio], 0)]         # Pila con tupla: (nodo actual, camino recorrido, profundidad actual)
    visitados = set()                      # Conjunto para marcar nodos visitados

    while pila:                            # Mientras haya elementos en la pila
        nodo, camino, profundidad = pila.pop()  # Sacamos el último elemento

        if nodo == objetivo:               # Si encontramos el objetivo
            return camino                  # Regresamos el camino

        if profundidad < limite:           # Solo expandimos si no hemos alcanzado el límite
            if nodo not in visitados:      # Si el nodo no ha sido visitado
                visitados.add(nodo)        # Lo marcamos como visitado

                for vecino in grafo.get(nodo, []):  # Recorremos vecinos del nodo actual
                    pila.append((vecino, camino + [vecino], profundidad + 1))  # Agregamos vecino con profundidad +1

    return None                            # Si no se encuentra el objetivo dentro del límite

def ids(grafo, inicio, objetivo, max_limite):  # Función principal: Iterative Deepening Search
    for limite in range(max_limite + 1):       # Iteramos desde límite 0 hasta max_limite
        resultado = dls(grafo, inicio, objetivo, limite)  # Ejecutamos DLS con el límite actual
        if resultado is not None:              # Si encontramos solución
            return resultado, limite           # Regresamos el camino y el límite en que se encontró
    return None, None                          # Si no se encuentra solución en ningún límite
grafo = {
    'APPLE_STORE': ['MACDONALS'],
    'MACDONALS': ['ZONA_COMIDA', 'F_GUADALAGARA'],
    'ZONA_COMIDA': ['GOMBILL', 'MINISO'],
    'MINISO': ['KIDSANIA','PUMA','CHARLI'],
    'GOMBILL': ['ESTACIONAMIENTO'],
}
camino, limite_encontrado = ids(grafo, 'APPLE_STORE', 'GOMBILL', 5)# Ejecutamos IDS desde APPLE_STORE hasta GOMBILL con límite máximo 5
print("Camino encontrado:", camino, "en límite:", limite_encontrado)
