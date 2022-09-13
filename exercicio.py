lista_vazia = list()
def verificarlista ():
    if lista_vazia.__len__() == 0 : 
        print('Lista está vazia', lista_vazia)
    if lista_vazia.__len__() >= tamMax:
        print('Lista está cheia', lista_vazia)
        exit()

def adcionando ():
    elemento = int (input('Elemento a ser adcionado: '))
    lista_vazia.append(elemento)

def obterEModificar(): 
    elemento = int(input('Digite qual posição deseja alterar da lista: '))
    print(lista_vazia[elemento - 1])
    elementoModificado = int(input('Digite o valor que irá substituir: '))
    lista_vazia[elemento - 1] = elementoModificado
    print(lista_vazia)

def inserirElemento():
    posicao = int(input('Digite a posição a qual deseja inserir o elemento: '))
    elemento = int(input('Digito o elemento que será inserido : '))
    lista_vazia.insert(posicao, elemento)
    print(lista_vazia)

def removerElemento():
    print(lista_vazia)
    tamanho = lista_vazia.__len__()
    elemento = int(input('Digite qual valor deseja deletar da lista: '))
    acaoRemover = True
    i = 0
    while i > tamanho or acaoRemover:
        if elemento == lista_vazia[i] :
            del lista_vazia[i]
            print(lista_vazia)
            acaoRemover = False
        else :
            i + 1

tamMax =int(input('Defina o tamanho da lista: '))
verificarlista()
acaoMenu = True
while acaoMenu:
    menu = int(input('Digite o numero da opção que deseja. [1] Adicionar elemento, [2] Modificar elemento da lista, [3] Inserir elemento na lista, [4] Deletar elemento da lista, [5] Sair: '))
    if menu == 1:
         adcionando()
         verificarlista()
         print('Tamanho da lista agora é',lista_vazia.__len__())
    if menu == 2:
        obterEModificar()
    if menu == 3:
        inserirElemento()
        verificarlista()
    if menu == 4:
        removerElemento()
    if menu == 5:
        acaoMenu = False