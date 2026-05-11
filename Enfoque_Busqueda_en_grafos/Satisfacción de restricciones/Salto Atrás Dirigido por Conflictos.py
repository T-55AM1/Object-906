def es_valido(nodo, color, asignacion, grafo):
    
    #verifica que ningun grafo tenga el mismo color
    for vecino in grafo.get(nodo, []):
        if asignacion.get(vecino) == color:
            return False
    return True

def conflict_directed_backjumping(grafo, nodos, colores, asignacion={}, idx=0):
    #Si todos los nodos estan coloreados
    if idx == len(nodos):
        return asignacion

    nodo = nodos[idx]
    #Guardamos las variables que causan conflicto 
    conflictos = set()

    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            resultado = conflict_directed_backjumping(grafo, nodos, colores, asignacion, idx+1)
            if resultado:
                return resultado
            asignacion.pop(nodo)
        else:
            #guardamos el conflicto con este nodo
            conflictos.add(nodo)

    if conflictos:#Si hubo conflictos, retrocedemos directamente al nodo conflictivo
        return None

    return None

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

#Ejecutamos conflict_directed_backjumping
nodos = list(grafo.keys())
resultado = conflict_directed_backjumping(grafo, nodos, colores)
print("Asignacion de colores encontrada (conflict_directed_backjumping):", resultado)

    
