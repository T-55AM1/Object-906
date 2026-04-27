from collections import deque  # Importamos deque para manejar colas eficientes

def bidirectional_search(grafo, inicio, objetivo):  # Definimos la función con grafo, nodo inicial y objetivo
    if inicio == objetivo:  # Caso trivial: si inicio y objetivo son iguales
        return [inicio]     # Regresamos directamente el nodo

    # Inicializamos dos colas: una desde el inicio y otra desde el objetivo
    cola_inicio = deque([(inicio, [inicio])])       # Cola que guarda (nodo, camino desde inicio)
    cola_objetivo = deque([(objetivo, [objetivo])]) # Cola que guarda (nodo, camino desde objetivo)

    # Diccionarios para registrar caminos visitados desde cada lado
    visitados_inicio = {inicio: [inicio]}           # Camino desde inicio
    visitados_objetivo = {objetivo: [objetivo]}     # Camino desde objetivo

    while cola_inicio and cola_objetivo:            # Mientras ambas colas tengan elementos
        # --- Expansión desde el lado del inicio ---
        nodo_i, camino_i = cola_inicio.popleft()    # Sacamos el primer nodo de la cola de inicio
        for vecino in grafo.get(nodo_i, []):        # Recorremos vecinos del nodo actual
            if vecino not in visitados_inicio:      # Si el vecino no ha sido visitado desde inicio
                visitados_inicio[vecino] = camino_i + [vecino]  # Guardamos el camino hasta ese vecino
                cola_inicio.append((vecino, camino_i + [vecino]))  # Lo agregamos a la cola
                if vecino in visitados_objetivo:    # Si este vecino ya fue visitado desde el objetivo
                    # Unimos el camino desde inicio y el camino desde objetivo (invertido)
                    return visitados_inicio[vecino] + visitados_objetivo[vecino][::-1][1:]

        # --- Expansión desde el lado del objetivo ---
        nodo_o, camino_o = cola_objetivo.popleft()  # Sacamos el primer nodo de la cola de objetivo
        for vecino in grafo.get(nodo_o, []):        # Recorremos vecinos del nodo actual
            if vecino not in visitados_objetivo:    # Si el vecino no ha sido visitado desde objetivo
                visitados_objetivo[vecino] = camino_o + [vecino]  # Guardamos el camino hasta ese vecino
                cola_objetivo.append((vecino, camino_o + [vecino]))  # Lo agregamos a la cola
                if vecino in visitados_inicio:      # Si este vecino ya fue visitado desde el inicio
                    # Unimos el camino desde inicio y el camino desde objetivo (invertido)
                    return visitados_inicio[vecino] + visitados_objetivo[vecino][::-1][1:]

    return None  # Si no hay conexión entre inicio y objetivo, regresamos None


grafo = {
    'APPLE_STORE': ['MACDONALS'],                # APPLE_STORE conecta con MACDONALS
    'MACDONALS': ['ZONA_COMIDA', 'F_GUADALAGARA'], # MACDONALS conecta con ZONA_COMIDA y F_GUADALAGARA
    'ZONA_COMIDA': ['GOMBILL', 'MINISO'],        # ZONA_COMIDA conecta con GOMBILL y MINISO
    'MINISO': ['KIDSANIA','PUMA','CHARLI'],      # MINISO conecta con KIDSANIA, PUMA y CHARLI
    'GOMBILL': ['ESTACIONAMIENTO'],              # GOMBILL conecta con ESTACIONAMIENTO
}
print("Camino encontrado:", bidirectional_search(grafo, 'APPLE_STORE', 'GOMBILL'))# Ejecutamos búsqueda bidireccional desde APPLE_STORE hasta GOMBILL
