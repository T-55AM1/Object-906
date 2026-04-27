def dls(grafo, inicio, objetivo, limite):  # Definimos la función DLS con grafo, nodo inicial, objetivo y límite de profundidad
    pila = [(inicio, [inicio], 0)]         # Pila con tupla: (nodo actual, camino recorrido, profundidad actual)
    visitados = set()                      # Conjunto para marcar nodos visitados y evitar ciclos

    while pila:                            # Mientras haya elementos en la pila
        nodo, camino, profundidad = pila.pop()  # Sacamos el último elemento (LIFO)

        if nodo == objetivo:               # Si el nodo actual es el objetivo
            return camino                  # Regresamos el camino recorrido

        if profundidad < limite:           # Solo expandimos si no hemos alcanzado el límite
            if nodo not in visitados:      # Si el nodo no ha sido visitado
                visitados.add(nodo)        # Lo marcamos como visitado

                for vecino in grafo.get(nodo, []):  # Recorremos vecinos del nodo actual
                    pila.append((vecino, camino + [vecino], profundidad + 1))  # Agregamos vecino con profundidad +1

    return None                            # Si no se encuentra el objetivo dentro del límite, regresamos None
grafo = {
    'APPLE_STORE': ['MACDONALS'],
    'MACDONALS': ['ZONA_COMIDA', 'F_GUADALAGARA'],
    'ZONA_COMIDA': ['GOMBILL', 'MINISO'],
    'MINISO': ['KIDSANIA','PUMA','CHARLI'],
    'GOMBILL': ['ESTACIONAMIENTO'],
}
print("Camino encontrado:", dls(grafo, 'APPLE_STORE', 'GOMBILL', 2))# Ejecutamos DLS desde APPLE_STORE hasta GOMBILL con límite de profundidad 2

