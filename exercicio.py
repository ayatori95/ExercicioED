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



tamMax =int(input('Defina o tamanho da lista: '))
verificarlista()
adcionando()
print('Tamanho da lista agora é',lista_vazia.__len__())

execucao = True
while execucao :
    resposta = input('Deseja Adcionar um elemento? s/n ')
    if resposta == 's' : 
        adcionando()
        verificarlista()
        print('Tamanho da lista agora é',lista_vazia.__len__())
    if resposta == 'n' : execucao = False

obterEModificar()
inserirElemento()