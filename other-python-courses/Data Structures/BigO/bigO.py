from logging import captureWarnings
import time
import numpy as np




# BigO(n) Desempenho relativo a quantidade de elementos
def sum1(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


# Big0(3)
def sum2(n):
    return ((n ( n + 1)) / 2)

# BigO(1000) || O(n)
def list1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

# BigO(1)
def list2():
    return range(1000)


#Constante - Contem somente 1 passo;
# O(1)
lista = [1,2,3,4,5]
def constant(n):
    print(n[0])
    
# Linear - Possui O(n) Depende do valor de N
def linear(n):
    for i in n:
        print(i)

# Quadratica(O(n^2)) - polynomial | Possui 2 loops portanto eleva a complexidade a 2
# Muito utilizado para ler matrizes
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)

# Combinação de varios parametros do BigO, o correto é separar a função em varias etapas e calcular separadamente
def combination(n):
    
    # Somatoria da complexidade: O(1) + O(5) + O(N) + O(N) + O(3)
    #                            O(9) + O(2n) -> O(n)
    #                            
    
    #BigO(1)
    print(n[0])
    
    #BigO(5)
    for i in range(5):
        print('teste', i)
        
    #BigO(n)
    for i in n:
        print(i)
        
    #BigO(n)
    for i in n:
        print(i)
        
    
    # BigO(3))
    print('python')
    print('python')
    print('python')
    

# Vetores nao ordenados

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    # BigO(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '- ' , self.valores[i])
                
    #BigO(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade:
            print('Capacidade maxima atingida')
        else: 
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                print(i)
                return i
            return -1
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1
            
        
vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

vetor.imprime()

vetor.pesquisar(1)

vetor.excluir(3)
vetor.imprime()