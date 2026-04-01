#  [Representa¸c˜ao] (2,0pts) Crie um tipo estruturado de dados ou uma classe que represente um grafo n˜ao-dirigido
# e ponderado G(V, E, w), no qual V ´e o conjunto de v´ertices, E ´e o conjunto de arestas e w : E → R ´e a fun¸c˜ao que
# mapeia o peso de cada aresta {u, v} ∈ E. As opera¸c˜oes/m´etodos contemplados para o grafo dever˜ao ser:
# • qtdVertices(): retornr a quantidade de v´ertices;
# • qtdArestas(): retorna a quantidade de arestas;
# • grau(v): retorna o grau do v´ertice v;
# • rotulo(v): retorna o r´otulo do v´ertice v;
# • vizinhos(v): retorna os vizinhos do v´ertice v;
# • haAresta(u, v): se {u, v} ∈ E, retorna verdadeiro; se n˜ao existir, retorna falso;
# • peso(u, v): se {u, v} ∈ E, retorna o peso da aresta {u, v}; se n˜ao existir, retorna um valor infinito positivo1
# ;
# • ler(arquivo)2
# : deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento.

from collections import defaultdict

class Grafo:
    def __init__(self, arquivo=None):
        self.verticesNames = {} # índice → rótulo
        self.osVizinhos = defaultdict(dict) # índice → {vizinho: peso}
        self.numArestas = 0

        if arquivo:
            self.ler_arquivo(arquivo)

    def ler_arquivo(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            
            lendo_vertices = False
            lendo_arestas = False

            for linha in linhas:
                linha = linha.strip()
                if not linha: continue 

                if "*vertices" in linha.lower():
                    lendo_vertices = True
                    lendo_arestas = False
                    continue
                elif "*edges" in linha.lower() or "*arcs" in linha.lower():
                    lendo_vertices = False
                    lendo_arestas = True
                    continue

                partes = linha.split()

                if lendo_vertices:
                    if len(partes) >= 2:
                        indice = int(partes[0])
                        rotulo = " ".join(partes[1:]).replace('"', '')
                        self.verticesNames[indice] = rotulo

                elif lendo_arestas:
                    if len(partes) >= 2:
                        u, v = int(partes[0]), int(partes[1])
                        peso = float(partes[2]) if len(partes) > 2 else 1.0
                        
                        self.osVizinhos[u][v] = peso
                        self.osVizinhos[v][u] = peso
                        self.numArestas += 1

    def qtdVertices(self):
        return len(self.verticesNames)

    def qtdArestas(self):
        return self.numArestas
    
    def grau(self, v):
        return len(self.osVizinhos[v])
    
    def rotulo(self, v):
        return self.verticesNames.get(v, None) #retorna o rotulo/nome de um vertice especifico

    def vizinhos(self, v):
        return list(self.osVizinhos[v].keys())

    def haAresta(self, u, v):
        return v in self.osVizinhos[u]

    def peso(self, u, v):
        return self.osVizinhos[u].get(v, float('inf'))