from collections import OrderedDict
import sys
import os
import operator

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from graph import Grafo

def kruskal(grafo):
    A = set()
    S = dict()
    for v in grafo.verticesNames:
        S[v] = {v}

    EOrdenado = get_arestas(grafo)
    EOrdenado = OrderedDict(sorted(EOrdenado.items(), key=operator.itemgetter(1)))
    soma = 0
    for aresta, peso in EOrdenado.items():
        v = aresta[0]
        u = aresta[1]
        if S[v] != S[u]:
            A = A.union({(v, u)})
            soma += peso
            x = S[v].union(S[u])
            for y in x:
                S[y] = x
    return (A, soma)


def get_arestas(grafo):
    E = dict()
    for v in grafo.verticesNames:
        for u in grafo.verticesNames:
            if v == u:
                continue
            if grafo.haAresta(v, u):
                if ((u, v) in E) or ((v, u) in E):
                    continue
                peso = grafo.peso(v, u)
                E[(v, u)] = peso
    return E


if len(sys.argv) < 2:
    print("Uso: python3 A2_3.py <arquivo>")
    sys.exit(1)

g = Grafo()
g.ler_arquivo(sys.argv[1])
arvore, peso = kruskal(g)
print(peso)
arvore = list(arvore)
for i in range(len(arvore) - 1):
    v = arvore[i][0]
    u = arvore[i][1]
    print(str(v) + "-" + str(u), end=", ")
print(str(arvore[len(arvore) - 1][0]) + "-" + str(arvore[len(arvore) - 1][1]))
