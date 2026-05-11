import random

# Grafo de tiendas
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

# Recompensas (utilidad)
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

def value_iteration(grafo, prob_abierto, utilidad, gamma=0.9, max_iter=100):
    V = {s: 0 for s in grafo} #Inicializamos valores
    for _ in range(max_iter):
        nuevo_V = {}
        for s in grafo:
            #Recompensa inmediata si la tienda esta abierta
            recompensa = prob_abierto[s] * utilidad[s]
            #Valor esperado de moverse a vecinos
            if grafo[s]:
                vecinos_valor = max(V[v] for v in grafo[s])
            else:
                vecinos_valor = 0
            nuevo_V[s] = recompensa + gamma * vecinos_valor
        V = nuevo_V
    return V

valores = value_iteration(grafo, prob_abierto, utilidad)
print("Valores optimos por tienda (Value Iteration):")
for nodo, v in valores.items():
    print(f"{nodo}: {v:.2f}")
            
























