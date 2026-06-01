from collections import deque
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graph import Grafo

def buscaEdmondsKarp(G, s, t, cf):

    C = {v: False for v in cf.keys()}
    A = {}  
    
    if s not in C or t not in C:
        return None

    C[s] = True
    Q = deque([s])
    
    while len(Q) > 0:
        u = Q.popleft()  
        
        for v in cf[u]:
            if C[v] == False and cf[u][v] > 0:
                C[v] = True     
                A[v] = u        
                if v == t:
                    p = [t]     
                    w = t       
                    while w != s:
                        w = A[w]      
                        p.insert(0, w)
                    return p    
                Q.append(v)
    return None


def edmonds_karp_completo(G, s, t):
    cf = {}
    
    todos_vertices = set(G.osVizinhos.keys())
    for u in G.osVizinhos:
        todos_vertices.update(G.osVizinhos[u].keys())
        
    for v in todos_vertices:
        cf[v] = {}

    for u in G.osVizinhos:
        for v in G.osVizinhos[u]:
            cf[u][v] = G.osVizinhos[u][v]

    for u in list(cf.keys()):
        for v in list(cf[u].keys()):
            if u not in cf[v]:
                cf[v][u] = 0

    fluxo_maximo = 0

    while True:
        p = buscaEdmondsKarp(G, s, t, cf)
        
        if not p:
            break

        gargalo = float('inf')
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i+1]
            gargalo = min(gargalo, cf[u][v])
        
        for i in range(len(p) - 1):
            u = p[i]
            v = p[i+1]
            cf[u][v] -= gargalo  
            cf[v][u] += gargalo  
            
        fluxo_maximo += gargalo

    return fluxo_maximo

g = Grafo()
g.ler_arquivo(sys.argv[1])

chaves_vertices = sorted(g.verticesNames.keys())

s = chaves_vertices[0]
t = chaves_vertices[-1]

valor_fluxo = edmonds_karp_completo(g, s, t)
print(valor_fluxo)
