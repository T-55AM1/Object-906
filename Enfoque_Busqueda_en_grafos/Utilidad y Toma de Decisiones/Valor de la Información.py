import random

grafo = {
    'APPLE_STORE': ['MACDONALS'],
    'MACDONALS': ['ZONA_COMIDA','F_GUADALAJARA'],
    'ZONA_COMIDA': ['GOMBILL','MINISO'],
    'MINISO': ['KIDSANIA','PUMA','CHARLI'],
    'GOMBILL': ['ESTACIONAMIENTO'],
    'F_GUADALAJARA': [],
    'KIDSANIA': [],
    'PUMA': [],
    'CHARLI': [],
    'ESTACIONAMIENTO': []
}

# Probabilidades de apertura
prob_abierto = {
    'APPLE_STORE': 0.9,
    'MACDONALS': 0.8,
    'ZONA_COMIDA': 0.7,
    'MINISO': 0.6,
    'GOMBILL': 0.5,
    'F_GUADALAJARA': 0.9,
    'KIDSANIA': 0.7,
    'PUMA': 0.8,
    'CHARLI': 0.6,
    'ESTACIONAMIENTO': 1.0
}

# Utilidades
utilidad = {
    'APPLE_STORE': 10,
    'MACDONALS': 8,
    'ZONA_COMIDA': 6,
    'MINISO': 7,
    'GOMBILL': 5,
    'F_GUADALAJARA': 4,
    'KIDSANIA': 9,
    'PUMA': 6,
    'CHARLI': 5,
    'ESTACIONAMIENTO': 3
}

def utilidad_esperada(nodo):
    return prob_abierto[nodo] * utilidad[nodo]

#Utilidad esperada sin informacion (mejor decision global)
EU_sin_info = max(utilidad_esperada(n) for n in grafo)

def valor_informacion(nodo):
    #Con informacion perfecta: si esta abierto, elegimosese nodo; si esta cerrado, elegimos el mejor de los demas
    EU_con_info = (prob_abierto[nodo] * utilidad[nodo] + (1 - prob_abierto[nodo]) * max(utilidad_esperada(m) for m in grafo if m !=nodo))
    return EU_con_info - EU_sin_info

#Calcular VOI para cada nodo
print("Valor de la Informacion por tienda:")
for nodo in grafo:
    print(f"{nodo}: {valor_informacion(nodo):.2f}")













