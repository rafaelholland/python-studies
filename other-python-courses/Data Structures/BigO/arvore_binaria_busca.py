

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def mostra_no(self):
        print(self.valor)
        

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo_no = No(valor)
        # Se a arvore estiver vazia
        if self.raiz == None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                pai = atual
                #Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo_no
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo_no.valor))
                        return
                #Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo_no
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo_no.valor))
                        return
                    
    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
## Insercao e visualizacao 

arvore = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)
print(arvore.pesquisar(100))
if arvore.pesquisar(84) == None:
    print('Nao encontrado')
else:
    "Elemento localizado"
    