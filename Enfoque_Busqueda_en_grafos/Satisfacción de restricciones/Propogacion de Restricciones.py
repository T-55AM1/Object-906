
from collections import deque

def ac3(grafo, dominios):#creamos una cola con todos los arcos (nodo, vecino)
    cola = deque([(nodo, vecino) for nodo in grafo for vecino in grafo[nodo]])

    while cola:
        nodo, vecino = cola.popleft()
        if revisar_arco(nodo, vecino, dominios):
            if not dominios[nodo]:
                return False #Si algun nodo se queda sin vaores no hay solucion

            for otro in grafo:#Si hubo cambios, volvemos a revisar los vecinos del nodo
                if nodo in grafo[otro] and otro != vecino:
                    cola.append((otro, nodo))
    return True

def revisar_arco(nodo, vecino, dominios):
    cambiado = False
    for valor in dominios[nodo][:]:
        #Si no hay ningun vecino que sea distinto, eliminamos el valor
        if all(valor == v for v in dominios[vecino]):
            dominios[nodo].remove(valor)
            cambiado = True
    return cambiado

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

# Colores disponibles
colores = ['rojo', 'verde', 'azul']

#iniciamos dominios
dominios = {n: list(colores) for n in grafo}
#Ejecutamos  ac3
resultado = ac3(grafo, dominios)
print("¿Es consistente el grafo?:", resultado)
print("Dominios reducidos despues de ac3:", dominios)








