import random

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

#Probabilidad de que cada tienda este abierta (nodo de azar)
prob_abierto = {
    'APPLE_STORE': 0.9,
    'MACDONALS': 0.8,
    'ZONA_COMIDA': 0.7,
    'MINISO': 0.6,
    'GOMBILL': 0.5,
    'F_GUADALAGARA': 0.9,
    'KIDSANIA': 0.7,
    'PUMA': 0.8,
    'CHARLI': 0.6,
    'ESTACIONAMIENTO': 1.0
    }

#Utilidad de visitar cada tienda (nodo de utilidad)
utilidad = {
    'APPLE_STORE': 10,
    'MACDONALS': 8,
    'ZONA_COMIDA': 6,
    'MINISO': 7,
    'GOMBILL': 5,
    'F_GUADALAGARA': 4,
    'KIDSANIA': 9,
    'PUMA': 6,
    'CHARLI': 5,
    'ESTACIONAMIENTO': 3
    }

def utilidad_esperada(nodo):
    return prob_abierto[nodo] * utilidad[nodo]

#Nodo de decision: elegir la tienda con mayor utilidad esperada
mejor_tienda = max(grafo.keys(), key=lambda n: utilidad_esperada(n))
print("Utilidades esperadaspor tienda:")
for nodo in grafo:
    print(f"{nodo}: {utilidad_esperada(nodo):.2f}")

print("\nDesicion optima (Red de Decision): visitar",mejor_tienda)




















