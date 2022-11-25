class Pilha():
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0

    def size(self):
         return len(self.dados)

# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha.dados)
acaoMenu = True
while acaoMenu:
    menu = int(input('Digite o numero da opção que deseja. [1] Adicionar elemento, [2] Deletar elemento da lista, [3] Ler o topo da pilha, [4] Indicar se a pilha está vazia, [5] Retornar tamanho da pilha, [6] Sair: '))
    if menu == 1:
         top = int (input('Elemento a ser adcionado: '))
        # Insere elementos na pilha.
         pilha.empilha(top)
         print("Insere o valor {0} no topo da pilha: {1}".format(top, pilha.dados))
    if menu == 2:
        if not pilha.vazia():
         pilha.desempilha()
         print("Removendo elemento que está no topo da pilha: ", pilha.dados)
        else:
         print("Pilha está vazia.")
    if menu == 3:
        try:
         print(pilha.dados[-1])
        except IndexError:
         print('Ocorreu um erro, é possível que a lista esteja vazia.')
    if menu == 4:
        if pilha.vazia():
            print("Pilha está vazia")
        if not pilha.vazia():
            print("Pilha não está vazia")
    if menu == 5:
        print(pilha.size())
    if menu == 6:
        acaoMenu = False


