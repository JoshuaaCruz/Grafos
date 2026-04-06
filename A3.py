import sys
from graph import Grafo

def buscarSubciclo(grafo, v_inicial, arestas):
    ciclo = [v_inicial]
    vertice_atual = v_inicial

    while True:
        v_next = None
       
        for vizinho in grafo.vizinhos(vertice_atual):
            aresta = tuple(sorted((vertice_atual, vizinho)))

            if arestas.get(aresta, 0) > 0:
                arestas[aresta] -= 1
                v_next = vizinho
                break
                #achamos um caminho que existe uma aresta válida para seguir
        
        if v_next is not None:
            ciclo.append(v_next)
            vertice_atual = v_next
            #colocamos na lista e atualizamos o atual
            #se forem iguais é porque encontramos o ciclo
            if vertice_atual == v_inicial:
                break
        else:
            break
    
    i = 0
    while i < len(ciclo):
        v_atual = ciclo[i]

        tem_vizinho = False
        for vizinho in grafo.vizinhos(v_atual):
            if arestas.get(tuple(sorted((v_atual, vizinho))), 0) > 0:
                tem_vizinho = True
                break
                #repassamos e vemos se alguma aresta ficou com "sinal positivo"
        
        if tem_vizinho:
            subciclo = buscarSubciclo(grafo, v_atual, arestas)
            ciclo[i : i + 1] = subciclo #insercao do subciclo 
        else: 
            i += 1
    
    return ciclo

def ciclo_euleriano(grafo):

    for indice in grafo.verticesNames:
        if grafo.grau( indice) % 2 != 0:
            return print("0")

    if not grafo.verticesNames:
        return print("0")
    
    v_inicial = None
    for v in grafo.verticesNames:
        if grafo.grau(v) > 0:
            v_inicial = v
            break

    arestas = {}
    for u in grafo.verticesNames:
        for v in grafo.vizinhos(u):
            aresta = tuple(sorted((u, v)))
            if aresta not in arestas:
                arestas[aresta] = 1
            
    ciclo_final = buscarSubciclo(grafo, v_inicial, arestas)
    
    if any(count > 0 for count in arestas.values()):
        print("0")
    else:
        print("1")
        print(",".join(map(str, ciclo_final)))


if len(sys.argv) < 2:
    print("python3 A2.py <arquivo>")
    sys.exit(1)

arquivo_input = sys.argv[1]

g = Grafo()
g.ler_arquivo(arquivo_input)
ciclo_euleriano(g)

