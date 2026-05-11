import itertools

def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo.get(nodo, []):
        if asignacion.get(vecino) == color:
            return False
    return True

def backtracking_coloreo(grafo, nodos, colores, asignacion={}, idx=0):
    if idx == len(nodos):
        return asignacion
    nodo = nodos[idx]
    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            resultado = backtracking_coloreo(grafo, nodos, colores, asignacion, idx+1)
            if resultado:
                return resultado
            asignacion.pop(nodo)
    return None

def cutset_conditioning(grafo, nodo, colores, cutset):
    #Probamos todas las combinaciones de colores para el cutset
    for combination in itertools.product(colores, repeat=len(cutset)):
        asignacion = {cutset[i]: combination[i] for i in range(len(cutset))}
        #Resolver el resto del grafo con backtracking
        resto = [n for n in nodos if n not in cutset]
        resultado = backtracking_coloreo(grafo, resto, colores, asignacion)
        if resultado:
            return resultado
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
nodos = list(grafo.keys())
cutset = ['MINISO'] #nODO ELEGIDO COMO CORTE

resultado = cutset_conditioning(grafo, nodos, colores, cutset)
print("Asignacion de colores encontrada (Cutset Conditioning):", resultado)





