from collections import deque
import sys
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graph import Grafo

def hopcroft_karp(grafo):
    # Ordenação dos vértices + separação. Existência do Y por mera formalidade.
    vertices = sorted(grafo.verticesNames)
    X = vertices[0:(len(vertices) // 2)]
    Y = vertices[(len(vertices) // 2):]

    # Definição das demais estruturas.
    D = dict()
    for v in vertices:
        D[v] = float("inf")

    mate = dict()
    for v in vertices:
        mate[v] = None

    m = 0

    # Início da lógica. As instruções da apostila foram seguidas a risca.
    while BFS(grafo, X, Y, mate, D):
        for x in X:
            if mate[x] is None:
                if DFS(grafo, mate, x, D):
                    m += 1
    return m, mate

# Implementação BFS de acordo com a apostila
def BFS(grafo, X, Y, mate, D):
    infinity = float("inf")
    Q = deque()
    for x in X:
        if mate[x] is None:
            D[x] = 0
            Q.append(x)
        else:
            D[x] = infinity

    D[None] = infinity

    while len(Q) != 0:
        x = Q.popleft()
        if D[x] < D[None]:
            vizinhos = grafo.vizinhos(x)
            for y in vizinhos:
                if D[mate[y]] == infinity:
                    D[mate[y]] = D[x] + 1
                    Q.append(mate[y])

    return D[None] != infinity

# Implementação DFS de acordo com a apostila
def DFS(grafo, mate, x, D):
    if x is not None:
        vizinhos = grafo.vizinhos(x)
        for y in vizinhos:
            if D[mate[y]] == D[x] + 1:
                if DFS(grafo, mate, mate[y], D):
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = float("inf")
        return False
    return True

g = Grafo()
g.ler_arquivo(sys.argv[1])
m, mate = hopcroft_karp(g)
keys = list(mate.keys())
lastKey = keys[len(keys) - 1]
keys = keys[0:len(keys) - 1]
print(m)
for i in keys:
    if mate[i] is None:
        continue
    print(str(i) + "-" + str(mate[i]), end=", ")
print(str(lastKey) + "-" + str(mate[lastKey]))