#2. [Buscas] (2,0pts) Crie um programa que receba um arquivo de grafo e o ´ındice do v´ertice s como argumentos3. O
#programa deve fazer uma busca em largura4 a partir de s e dever´a imprimir a sa´ıda na tela, onde cada linha dever´a
#conter o n´ıvel seguido de “:” e a listagem de v´ertices encontrados naquele n´ıvel. O exemplo abaixo trata de uma
#sa´ıda, na qual a busca se iniciou pelo v´ertice s no n´ıvel 0, depois prosseguiu nos v´ertices 3, 4 e 5 para o pr´oximo
#n´ıvel. No n´ıvel seguinte, a busca encontrou os v´ertices 1, 2, 6 e 7.

import sys
from graph import Grafo
from collections import deque

def bfs(grafo, vi):
    #visitados = {vi}
    distancia = {vi: 0}

    fila = deque([vi])

    while fila:
        vertice = fila.popleft()
        for vizinho in grafo.osVizinhos[vertice]:
            if vizinho not in distancia:
                #visitados.add(vizinho)
                distancia[vizinho] = distancia[vertice] + 1
                fila.append(vizinho)

    return distancia

if len(sys.argv) < 3:
    print("python3 A1_2.py <arquivo> <vertice_inicial>")
    sys.exit(1)

arquivo_input = sys.argv[1]
vertice_inicial = int(sys.argv[2])

g = Grafo()
g.ler_arquivo(arquivo_input)

distancia = bfs(g, vertice_inicial)

niveis = {}
for vertice, d in distancia.items():
    if d not in niveis:
        niveis[d] = []
    niveis[d].append(vertice)

for nivel in sorted(niveis.keys()):
    lista_vertices = niveis[nivel]
    lista_vertices.sort()
    string_vertices = ", ".join(map(str, lista_vertices))
    print(f"{nivel}: {string_vertices}")