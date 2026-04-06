import sys
from graph import Grafo

def imprimir_saida(grafo, s, distances, ancestors):
    # Ordenar os vértices para garantir a saída na ordem crescente (1, 2, 3...)
    vertices_ordenados = sorted(list(grafo.verticesNames.keys()))
    
    for v in vertices_ordenados:
        # Se a distância for infinita, o vértice é inalcançável
        if distances[v] == float('inf'):
            continue
            
        caminho = []
        atual = v
        
        # Reconstrói o caminho de trás para frente
        while atual is not None:
            caminho.append(atual)
            if atual == s:
                break
            atual = ancestors[atual]
            
        # Inverte a lista para ficar na ordem (Origem -> Destino)
        caminho.reverse()
        
        # Formatar a saída
        caminho_str = ",".join(map(str, caminho))
        
        # Formatar a distância (remover casas decimais se for um número inteiro)
        d = distances[v]
        d_str = str(int(d)) if d == int(d) else str(d)
        
        print(f"{v}: {caminho_str}; d={d_str}")

def bellmanFord(grafo,s):
    distances = {}
    ancestors = {}
    for vertice in grafo.verticesNames.keys():
        distances[vertice] = float('inf')
        ancestors[vertice] = None

    distances[s] = 0

    for i in range(1, grafo.qtdVertices() ): #se range fosse inclusivo seria len - 1
        for u in grafo.verticesNames.keys():
            for v in grafo.vizinhos(u):
                if distances[v] > distances[u] + grafo.peso(u,v):
                    distances[v] = distances[u] + grafo.peso(u,v)
                    ancestors[v] = u

    for u in grafo.verticesNames.keys():
            for v in grafo.vizinhos(u):
                if distances[v] > distances[u] + grafo.peso(u,v):
                    return (False, None, None)
                
    return (True, distances, ancestors)


if len(sys.argv) < 3:
    print("python3 A4.py <arquivo> <vertice_s>")
    sys.exit(1)

arquivo_input = sys.argv[1]
vertice_s = int(sys.argv[2])

g = Grafo()
g.ler_arquivo(arquivo_input)
bellmanFord(g,vertice_s)

ciclosPosit, distancias, ancestors = bellmanFord(g,vertice_s)

if ciclosPosit:
    imprimir_saida(g, vertice_s, distancias, ancestors)
else:
    print("Ciclo negativo")