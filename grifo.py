class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]

    def inserir_aresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def remover_aresta(self, u, v):
        self.grafo[u][v] = 0
        self.grafo[v][u] = 0

    def imprimir_grafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.grafo[i][j], end=" ")
            print()

    def busca_profundidade(self, vertice):
        pilha = []
        visitados = []
        pilha.append(vertice)
        while pilha:
            vertice = pilha.pop()
            if vertice not in visitados:
                visitados.append(vertice)
                for i in range(self.vertices):
                    if self.grafo[vertice][i] == 1:
                        pilha.append(i)
        return visitados

    def busca_largura(self, vertice):
        fila = []
        visitados = []
        fila.append(vertice)
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.append(vertice)
                for i in range(self.vertices):
                    if self.grafo[vertice][i] == 1:
                        fila.append(i)
        return visitados

    def inserir_vertice(self, vertice):
        self.vertices += 1
        for i in range(self.vertices):
            self.grafo[i].append(0)
        self.grafo.append([0] * self.vertices)

    def remover_vertice(self, vertice):
        self.vertices -= 1
        self.grafo.pop(vertice)
        for i in range(self.vertices):
            self.grafo[i].pop(vertice)

def leitor_arquivo():
        arquivo = open('grafo.txt', 'r')
        linhas = arquivo.readlines()
        arquivo.close()
        vertices = int(linhas[0])
        arestas = int(linhas[1])
        grafo = Grafo(vertices)
        for i in range(2, arestas + 2):
            linha = linhas[i].split()
            grafo.inserir_aresta(int(linha[0]), int(linha[1]))
        return grafo

# Menu de opções.
def menu():
    def opcao():
        opcao = int(input('Digite o numero da opção que deseja. [1] Inserir vértice, [2] Inserir aresta, [3] Remover vértice, [4] Remover aresta, [5] Imprimir grafo, [6] Busca em profundidade, [7] Busca em largura, [8] Sair: '))
        return opcao
    grafo = leitor_arquivo()
    acaoMenu = True
    
    while acaoMenu: 
        decisao = opcao()
        if decisao == 1:
            vertice = int(input('Digite o numero do vértice que deseja inserir: '))
            grafo.inserir_vertice(vertice)
            print('Vértice inserido com sucesso.')
        if decisao == 2:
            u = int(input('Digite o numero do primeiro vértice: '))
            v = int(input('Digite o numero do segundo vértice: '))
            grafo.inserir_aresta(u, v)
            print('Aresta inserida com sucesso.')
        if decisao == 3:
            vertice = int(input('Digite o numero do vértice que deseja remover: '))
            grafo.remover_vertice(vertice)
            print('Vértice removido com sucesso.')
        if decisao == 4:
            u = int(input('Digite o numero do primeiro vértice: '))
            v = int(input('Digite o numero do segundo vértice: '))
            grafo.remover_aresta(u, v)
            print('Aresta removida com sucesso.')
        if decisao == 5:
            grafo.imprimir_grafo()
        if decisao == 6:
            vertice = int(input('Digite o numero do vértice que deseja iniciar a busca: '))
            print(grafo.busca_profundidade(vertice))
        if decisao == 7:
            vertice = int(input('Digite o numero do vértice que deseja iniciar a busca: '))
            print(grafo.busca_largura(vertice))
        if decisao == 8:
            acaoMenu = False

menu()