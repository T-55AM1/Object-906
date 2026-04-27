import heapq #importa una estructura de cola de prioridad

def costo_uniforme(grafo, inicio, objetivo): #(diccionario de instrucciones, nodo de inicio, nodo al que queremos llegar)
    cola = [(0, inicio, [inicio])] #cola con: (costo=0, nodo inicial, camino)
    visitados = set() #evitamos repetir ciclos y visitar nodos ya visitados
    
    while cola:
        costo, nodo, camino = heapq.heappop(cola) #saca el nodo con menor costo
        if nodo == objetivo:
            return camino, costo #si llega regresa camino y costo total
        
        if nodo not in visitados: #añade un nodo si el nodo no a sido visitado
            visitados.add(nodo)
            
            for vecino, peso in grafo.get(nodo, []):
                heapq.heappush(cola, (costo + peso, vecino, camino + [vecino])) #(la cola, (costo acumulado, vecino, camino + [vecino]))
    return None, float("inf")
#grafo en cuestion
grafo = {
    'APPLE_STORE': [('MACDONALS',5)],
    'MACDONALS': [('ZONA_COMIDA',3), ('F_GUADALAGARA',4)],
    'ZONA_COMIDA': [('GOMBILL',2), ('MINISO',3)],
    'MINISO': [('KIDSANIA',1),('PUMA',6),('CHARLI',5)],
    'GOMBILL': ['ESTACIONAMIENTO',8]
}
camino, costo = costo_uniforme(grafo, 'APPLE_STORE','GOMBILL')
print("Camino encontrado:", camino, "con costo:", costo)
