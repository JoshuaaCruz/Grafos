from collections import deque
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from graph import Grafo


def buscaProfundidade(grafo):
    conhecidos = set()
    ordem = deque()
    tempo = [0]
    T = {}
    F = {}
    for v in grafo.verticesNames.keys():
        if v not in conhecidos:
            buscaProfundidadeOT(grafo, v, conhecidos, T, F, ordem, tempo)
    return  ordem

def buscaProfundidadeOT(grafo, v, conhecidos, T, F, ordem, tempo):
    conhecidos.add(v)
    tempo[0] += 1
    T[v] = tempo[0]
    for u in grafo.osVizinhos[v]:
        if u not in conhecidos:
            buscaProfundidadeOT(grafo, u, conhecidos, T, F, ordem, tempo)
    tempo[0] += 1
    F[v] = tempo[0]
    ordem.appendleft(v)

if len(sys.argv) < 2:
    print("Uso: python3 A2_2.py <arquivo>")
    sys.exit(1)

def ordenacaoTopologica(grafo):
    ordem = buscaProfundidade(grafo)
    return ordem 

g = Grafo()
g.ler_arquivo(sys.argv[1])

ordem = ordenacaoTopologica(g)
resultado = " , ".join([g.verticesNames[v] for v in ordem])
print("Ordem Topológica:", resultado)
