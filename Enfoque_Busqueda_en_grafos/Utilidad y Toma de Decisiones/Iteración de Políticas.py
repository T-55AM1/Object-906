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

def policy_iteration(grafo, prob_abierto, utilidad, gamma=0.9, max_iter=100):
    #Inicializamos politica aleatoria (cada estado elige un vecino al azar si existe)
    policy = {s: (grafo[s][0] if grafo[s] else None) for s in grafo}
    V = {s: 0 for s in grafo}

    for _ in range(max_iter):
        #1. Evaluacion de la politica
        for s in grafo:
            recompensa = prob_abierto[s]* utilidad[s]
            if policy[s]:
                V[s] = recompensa

        #2. Mejora de la politica
                stable = True
                for s in grafo:
                    if grafo[s]:
                        #Elegimos la accion que maximisa el valor esperado
                        mejor_vecino = max(grafo[s], key=lambda v: V[v])
                        if mejor_vecino != policy[s]:
                            policy[s] = mejor_vecino
                            stable = False
                if stable:
                    break

            return policy, V

        policy, valores = policy_iteration(grafo, prob_abierto, utilidad)


        print("Valores optimos por tienda (Policy Iteration):")
        for nodo, v in valores.items():
            print(f"{nodo}: {v:.2f}")

        print("\nPolitica optima (que vecino elegir en cada tienda):")
        for nodo, accion in policy.items():
            print(f"{nodo} -> {accion}")





            











                






