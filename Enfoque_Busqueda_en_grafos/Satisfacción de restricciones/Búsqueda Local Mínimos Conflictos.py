import random

def contar_conflictos(nodo, color, asignacion, grafo):
    #Cuenta cuantos vecinos tienen el mismo color
    conflictos =  0
    for vecino in grafo.get(nodo, []):
        if asignacion.get(vecino) == color:
            conflictos += 1
    return conflictos

def min_conflicts(grafo, nodos, colores, max_iter=100):
    #Inicializacion aleatoria
    asignacion = {n: random.choice(colores) for n in nodos}

    for _  in range(max_iter):
        #Detectamos nodos en conflicto
        conflictos = [n for n in nodos if any(asignacion.get(v) == asignacion[n] for v in grafo.get(n, []))]
        if not conflictos:
            return asignacion #Solucion encontrada

        #Elegimos un nodo conflictivo al azar
        nodo = random.choice(conflictos)

        #Elegimos el color que minimisa conflictos
        mejor_color = min(colores, key=lambda c: contar_conflictos(nodo, c, asignacion, grafo))
        asignacion[nodo] = mejor_color
    return None #Sin solucion



grafo = {
    'APPLE_STORE': ['MACDONALS'],
    'MACDONALS': ['ZONA_COMIDA','F_GUADALAGARA'],
    'ZONA_COMIDA': ['GOMBILL','MINISO'],
    'MINISO': ['KIDSANIA','PUMA','CHARLI'],
    'GOMBILL': ['ESTACIONAMIENTO'],
    'F_GUADALAGARA': [],
    'KIDSANIA': [],
    'PUMA': [],
    'CHARLI': [],
    'ESTACIONAMIENTO': []
}
colores = ['rojo', 'verde', 'azul']

#ejecutamos Min-conflicts
nodos = list(grafo.keys())
resultado = min_conflicts(grafo, nodos, colores)
print("asignacion de colores encontrada (Min-Conflicts):", resultado)
