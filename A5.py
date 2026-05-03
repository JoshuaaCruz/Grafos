import sys

from graph import Grafo


def floyd_warshall(grafo):
    matriz_fw = [matriz_adjacencias(grafo)]
    vertices_ordenados = sorted(list(grafo.verticesNames.keys()))

    for k in range(1, grafo.qtdVertices() + 1):
        k_index = k - 1
        matriz_fw.append([])
        for u in vertices_ordenados:
            matriz_fw[k].append([])
            for v in vertices_ordenados:
                matriz_fw[k][u - 1].append(min(
                    matriz_fw[k - 1][u - 1][v - 1], matriz_fw[k - 1][u - 1][k_index] + matriz_fw[k - 1][k_index][v - 1]
                ))

    return matriz_fw[grafo.qtdVertices()]

def floyd_warshall_op(grafo):
    matriz_fw = matriz_adjacencias(grafo)
    vertices_ordenados = sorted(list(grafo.verticesNames.keys()))

    for k in range(1, grafo.qtdVertices() + 1):
        k_index = k - 1
        for u in vertices_ordenados:
            for v in vertices_ordenados:
                matriz_fw[u - 1][v - 1] = (min(
                    matriz_fw[u - 1][v - 1], matriz_fw[u - 1][k_index] + matriz_fw[k_index][v - 1]
                ))

    return matriz_fw



def matriz_adjacencias(grafo):
    vertices_ordenados = sorted(list(grafo.verticesNames.keys()))
    matriz_ad = []
    for u in vertices_ordenados:
        matriz_ad.append([])
        for v in vertices_ordenados:
            if u == v:
                matriz_ad[u - 1].append(0)
            else:
                matriz_ad[u - 1].append(grafo.peso(u, v))
    return matriz_ad


grafo = Grafo()
grafo.ler_arquivo(sys.argv[1])
matriz = floyd_warshall_op(grafo)
contador = 1
for i in matriz:
    print(f"{contador}:", end="")
    for n in range(0, len(i) - 1):
        print(f"{i[n]},", end="")
    print(f"{i[len(i) - 1]}\n", end="")
    contador += 1


