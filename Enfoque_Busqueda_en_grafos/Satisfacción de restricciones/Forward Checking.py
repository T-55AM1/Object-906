def forward_checking(grafo, nodos, colores, asignacion={}, dominios=None, idx=0):
    if dominios is None:
        dominios = {n: list(colores) for n in nodos} # Inicializamos dominios: todos los nodos pueden tener cualquier color

    if idx == len(nodos): # Si todos los nodos están coloreados
        return asignacion

    nodo = nodos[idx]
    for color in dominios[nodo][:]: # Iteramos sobre los colores posibles del nodo actual
        asignacion[nodo] = color

        # Copiamos dominios para esta rama de búsqueda
        nuevos_dominios = {n: list(dominios[n]) for n in nodos}

        # Reducimos dominios de los vecinos
        for vecino in grafo.get(nodo, []):
            if color in nuevos_dominios[vecino]: # Quitamos el color usado al vecino
                nuevos_dominios[vecino].remove(color)

            if not nuevos_dominios[vecino]: # Si algún vecino se queda sin colores → retrocedemos
                break

        else: # Si ningún vecino quedó sin colores, continuamos con el siguiente nodo
            resultado = forward_checking(grafo, nodos, colores, asignacion, nuevos_dominios, idx+1)
            if resultado:
                return resultado

        asignacion.pop(nodo) # Retrocedemos si no funciona

    return None    

# Colores disponibles
colores = ['rojo', 'verde', 'azul']

# Grafo definido
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


# Lista de nodos
nodos = list(grafo.keys())

# Ejecutamos Forward Checking
resultado = forward_checking(grafo, nodos, colores)
print("Asignación de colores encontrada (Forward Checking):", resultado)

