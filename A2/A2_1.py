from collections import deque
import sys
from graph import Grafo

def buscaProfundidade(grafo):
    conhecidos = set()
    ordem = deque()

    for v in grafo.verticesNames.keys():
        if v not in conhecidos:
            visita(grafo, v, conhecidos, ordem )
    return  ordem #ordem que a 2° busca profundidade irá operar sobre

def buscaProfundidade2(grafo, ordem):
    conhecidos = set()
    componentesFortConectados = []
    
    for v in ordem:
        if v not in conhecidos:
            umComponente = deque()
            visita(grafo, v, conhecidos, umComponente) #acha os componentes dessa busca em prof
            componentesFortConectados.append(sorted(umComponente)) #adiciona os grupos de componentes (fortemente conectados) na lista
    return componentesFortConectados
        
def visita(grafo, v, conhecidos, ordem):
    conhecidos.add(v)
    for u in grafo.osVizinhos[v]:
        if u not in conhecidos:
            visita(grafo, u, conhecidos, ordem)
    ordem.appendleft(v)

def transposto(grafo):
    grafoT = Grafo()
    grafoT.verticesNames = grafo.verticesNames.copy()
    for v in grafo.osVizinhos:
        for u, peso in grafo.osVizinhos[v].items():
            grafoT.osVizinhos[u][v] = peso
    grafoT.numArestas = grafo.numArestas
    grafoT.direcionado = grafo.direcionado
    return grafoT

def ks (oGrafo):

    ordem = buscaProfundidade(oGrafo)

    grafoT = transposto(oGrafo)

    ancestrais2 = buscaProfundidade2(grafoT, ordem)

    return ancestrais2

if len(sys.argv) < 2:
    print("Uso: python3 A2_1.py <arquivo>")
    sys.exit(1)

g = Grafo()
g.ler_arquivo(sys.argv[1])

for comp in ks(g):
    print(",".join(map(str, comp)))
