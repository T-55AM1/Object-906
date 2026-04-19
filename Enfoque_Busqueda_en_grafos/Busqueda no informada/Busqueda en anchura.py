
from collections import deque # deque es una cola que sale de collections o colecciones


def bfs(grafo, inicio, objetivo): #def bfs en una funcion de busqueda en anchura
                                  #y tenemos: (diccionario con conecciones, nodo inicial, nodo que buscamos)
    cola = deque([(inicio,[inicio])]) #creamos una cola con el nodo inicial
                                  #[inicio] es el camino recorrido
    visitados = set() #evitamos ciclos y no repetimos nodos
    while cola: #mientras haya nodos por explorar (traduccion)
        nodo, camino = cola.popleft() #sacamos el primer nodo de la cola
                                  #nodo: es el actual
                                  #camino: como llegamos aqui
        if nodo == objetivo: #si el nodo es igual al objetivo regresamos al camino
            return camino

        if nodo not in visitados: #vemos si ya lo visitamos
            visitados.add(nodo)   #si no lo marcamos

        for vecino in grafo[nodo]: #recorremos los vecinos del nodo actual
            cola.appened((vecino, camino + [Vecino])) #agregamos a la cola: el vecino y
                                                  # el nuevo camino

    return None #si no encuentra nada no hay solucion


        
