def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo.get(nodo, []): #vemos si hay vecinos del mismo color
        if asignacion.get(vecino) == color:
            return False
    return True

def backtracking_coloreo(grafo, nodos, colores, asignacion={}, idx=0):
    if idx == len(nodos): #Si coloreamos todos los nodos
        return asignacion

    nodo = nodos[idx]
    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            resultado = backtracking_coloreo(grafo, nodos, colores, asignacion, idx+1)
            if resultado:
                return resultado
            asignacion.pop(nodo) #Retrosede si no funciona
    return None
 

colores = ['rojo', 'verde', 'azul']

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
nodos = list(grafo.keys())
resultado = backtracking_coloreo(grafo, nodos, colores)
print("Asignacion de colores encontrada (Backtracking):", resultado)
