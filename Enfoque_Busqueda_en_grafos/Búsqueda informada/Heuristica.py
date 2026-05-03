import heapq #importamos heapq para manejar la cola de prioridad
def greedy_best_first(grafo, inicio, objetivo,heuristica): #Definimos la funcion greegy con grafo 
    cola = [(heuristica[inicio], inicio, [inicio])]#Cola con tupla: (h(n)), nodo acutual, camino recorrido
    visitados = set()#Conjunto para marcar nodos visitados

    while cola:#Mientras haya elementos en la cola
        h, nodo, camino = heapq.heappop(cola)#Extraemos el nodo con menor heuristica h(n)

        if nodo == objetivo:#Si llegamos al objetivo
            return camino#Regresamos el camino recorrido 
        
        if nodo not in visitados:#Si el nodo no ha sido visitado
            visitados.add(nodo)#Lo marcamos como visitado

            for vecino, _ in grafo.get(nodo, []):#Recorremos vecinos del nodo actual (ignoramos pesos)

                heapq.heappush(cola, (heuristica.get(vecino, float("inf")), vecino, camino + [vecino]))#Insertamos en la cola el vecino con su heuristica h(n) y el camino extendido

    return None   #None si no se encuentra nada         

grafo = {# el grafo
    'APPLE_STORE': [('MACDONALS', 5)],
    'MACDONALS': [('ZONA_COMIDA', 3), ('F_GUADALAGARA', 4)],
    'ZONA_COMIDA': [('GOMBILL', 2), ('MINISO', 3)],
    'MINISO': [('KIDSANIA', 1), ('PUMA', 6), ('CHARLI', 5)],
    'GOMBILL': [('ESTACIONAMIENTO', 8)],
}

heuristica = {#Heuristica definida para el objetivo 
'APPLE_STORE':7,
'MACDONALS':6,
'ZONA_COMIDA':4,
'MINISO':5,
'GOMBILL':0,
'F_GUADALAGARA':9,
'KIDSANIA':10,
'PUMA':8,
'CHARLI':7,
'ESTACIONAMIENTO':0
}
print("Camino enconrrado (Greedy):", greedy_best_first(grafo, 'APPLE_STORE', 'GOMBILL', heuristica)) #Mostramos el camino encontrado
