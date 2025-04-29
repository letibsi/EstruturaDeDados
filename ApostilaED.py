#Listas - armazena mais de um valor (ordenadas, mutáveis e heterogêneas) >>> Atribuídas com uso de colchetes [].
x = [10, 5, 11, 0, 3]
x

# Listas vazias podem ser criadas usando-se uma das duas sintaxes a seguir:
# x = []
# x = list()

#Como a lista é mutável, os valores nela armazenados podem ser alterados e novos valores podem ser adicionados.
L = [1, 4.5, 'abc', 3 + 4j, [1, 2, 3, 4]]
L[2] = 5
L[4] = 5
L
[1, 4.5, 5, (3+4j), 5]

#Para a adição de novos valores pode-se usar o método append(valor) ou o operador "+",que no caso das listas, executa concatenação.
A = [1, 2, 3]; B = [4, 5, 6]
C = A + B
C
[1, 2, 3, 4, 5, 6]
C += [7] # equivale a C = C + [7]
C
[1, 2, 3, 4, 5, 6, 7]
C.append('abc')
C
[1, 2, 3, 4, 5, 6, 7, 'abc']

#A heterogeneidade permite que a lista armazene tipos variados, incluindo também outras listas:

#7.1 Listas 61
L = [ 1, 4.5, 'abc', 3 + 4j, [1, 2, 3, 4]]
L
[1, 4.5, 'abc', (3+4j), [1, 2, 3, 4]]
L[4]
[1, 2, 3, 4]
L[4][0]
1

#append() Adiciona elementos a lista:
x = [1, 2, 3]
x.append (4)
x
[1, 2, 3, 4]

#clear() Esvazia a lista:
x = [1, 2, 3]
x.clear ()
x
[]

#count() Retorna quantas ocorrências há do argumento passado:
x = [1, 2, 3, 3, 3, 3, 4]
x.count (3)
4

#index() Retorna o índice da primeira ocorrência do argumento passado:
x = [1, 2, 3, 3, 3, 3, 4]
x.index (3)
2

#insert() Insere na posição especificada um elemento:
x = ['a,' 'c', 'd']
x.insert (1, 'b')
x
['a', 'b', 'c', 'd']

#pop() Remove e retorna o elemento da posição especificada:
x = ['a', 'b', 'c', 'd']
x.pop (1)
'b'
x
['a', 'c', 'd']

#remove() Remove o elemento especificado:
x = ['a', 'b', 'c']
x.remove('c')
x
['a', 'b']

#reverse() Inverte a ordem dos elementos:
x = [5, 4, 3, 2, 1]
x. reverse ()
x
[1, 2, 3, 4, 5]

#sort() Ordena:
x = [10, 3, 3, 10, 10, 6, 6, 4, 8, 7]
x.sort ()
x
[3, 3, 4, 6, 6, 7, 8, 10, 10, 10]

#7.1.2 Laço for - Os conjuntos finitos de valores usados na estrutura de repetição for para iterar uma variável, também é uma lista.
  
#Neste caso, a lista x é usada como a lista de valores no qual i será iterado. Assim, serão impressos os valores 10, 5, 11, 0 e 3.
#No entanto, fora da iteração for, o operador in retorna verdadeiro se o i está presente em x, ou falso caso contrário.

i = 10
i in x
True
i = 100
i in x
False

#Quando uma lista é criada a partir de um laço for, é possível reescrever o procedimento de forma mais compacta.
A=[3, 4, 5, 10]
soma1 = list ()
for i in A:
  soma1 += [i+1] #soma1. append (i+1)

soma1
[4, 5, 6, 11]

#Neste exemplo, uma nova lista soma1 é criada a partir de A somando-se 1 a cada elemento.

#A sintaxe da forma compacta pode ser expressa da seguinte forma:
#NovaLista = [ Elemento for Variavel in VelhaLista if Condicao ]
#No Exemplo anterior, seria:

A=[3, 4, 5, 10]
soma1 = [i+1 for i in A]
soma1
[4, 5, 6, 11]

#7.1.3 Fatiamento - É possível acessar partes da lista por meio de fatiamentos. Para isso, há três parâmetros, separados por dois pontos:

#Índices negativos continuam válidos, bem como o passo negativo, que indicará que o fatiamento será de trás para frente. O parâmetro de início é de onde o fatiamento irá
#começar, o de fim-1 é onde o fatiamento irá parar e o passo é de quantos em quantos elementos serão pegos. Exemplo:
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
X [0:2:1]
[1, 2]
X [0:4:1]
[1, 2, 3, 4]
X [0:4:2]
[1, 3]
#Nesse exemplo, primeiro é selecionado do elemento 0 até o elemento 1, de 1 em 1, depois selecionado do 0 até o 3 de 1 em 1 e, por fim, de 0 até o 3 de 2 em 2.


X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
X[::-1]
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
X[4::-1]
[5, 4, 3, 2, 1] 
#Esse exemplo mostra o passo negativo, que indica que o fatiamento percorre a lista no sentido inverso. Primeiro, toda a lista foi selecionada, porém com o passo -1, e, por fim, a lista foi selecionada a partir do elemento 4 e contada de 1 em direção ao elemento 0.

#É possível também omitir os parâmetros. Por padrão, o início vale 0, o fim vale o índice do último elemento + 1 (tamanho da lista) e o passo vale 1.
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
X[:2:1]
[1, 2]
X[:4]
[1, 2, 3, 4]
X[::2]
[1, 3, 5, 7, 9]
X[:] # equivale a X
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#Nesse exemplo, X foi fatiado primeiro de 0 a 2, com passo 1, depois em 0 a 4, também com passo 1, em seguida a lista toda, com passo 2 e, por fim, a lista toda.

#7.2 Tuplas - As tuplas são similares as listas, pois são ordenadas e heterogêneas. No entanto, diferentemente das listas, as tuplas são imutáveis. Este fato faz com que as tuplas sejam mais compactas e eficazes em termos de memória e eficiência.
  
#A sua atribuição é feita por meio de parênteses:
#x = ('a', 1, 2)
#type(x)
#<class 'tuple'>
#x
#('a', 1, 2)

#As tuplas são imutáveis, no entanto, como são heterogêneas, se em uma tupla houver listas, os item das listas podem ser alterados normalmente, pois, apesar da tupla, as listas são mutáveis:
#x = ([0, 1, 2], 2, 2)
#x[1]
#2
#x[1] = 2
#Traceback (most recent call last):
#File "<pyshell #12>", line 1, in <module >
#x[1] = 2
#TypeError : 'tuple' object does not support item assignment
#x[0]
#[0, 1, 2]
#x[0][0] = 'mudei'
#x
#(['mudei', 1, 2], 2, 2)





