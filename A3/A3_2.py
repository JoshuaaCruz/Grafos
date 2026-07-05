from collections import deque
from graph import Grafo
from sys import argv

def hopcroft_karp(grafo):
    # Divisão dos vértices em dois conjuntos U e V
    todos_vertices = list(grafo.verticesNames.keys())
    metade = grafo.qtdVertices() // 2
    U = todos_vertices[:metade]
    V = todos_vertices[metade:]

    emparelhamento = {}
    dist = {}

    # método BFS para encontrar caminho aumentante
    def bfs():
        queue = deque()
        for u in U:
            dist[u] = 0 if u not in emparelhamento else float('inf')
            if dist[u] == 0:
                queue.append(u)

        dist[None] = float('inf')

        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in grafo.vizinhos(u):
                    pair_u = emparelhamento.get(v)
                    if dist.get(pair_u, float('inf')) == float('inf'):
                        dist[pair_u] = dist[u] + 1
                        queue.append(pair_u)

        return dist[None] != float('inf')

    # função DFS para tentar expandir o emparelhamento
    def dfs(u):
        if u is None:
            return True
        for v in grafo.vizinhos(u):
            pair_u = emparelhamento.get(v)
            if dist.get(pair_u, float('inf')) == dist[u] + 1 and dfs(pair_u):
                emparelhamento[v] = u
                emparelhamento[u] = v
                return True
        dist[u] = float('inf')
        return False

    n_emparelhamento = 0
    while bfs():
        for u in U:
            if u not in emparelhamento and dfs(u):
                n_emparelhamento += 1

    # obtendo as arestas do emparelhamento
    arestas_emparelhadas = [f"{u}-{emparelhamento[u]}" for u in U if u in emparelhamento]

    return n_emparelhamento, arestas_emparelhadas

def ex_2():
    arquivo = argv[1]
    grafo = Grafo(arquivo)
    n_emparelhamento, arestas = hopcroft_karp(grafo)

    # exibindo o resultado
    print(n_emparelhamento)
    print(", ".join(arestas))

ex_2()