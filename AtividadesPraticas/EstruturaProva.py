#LISTA
#Criando lista vazia.
biblioteca_musicas = []

#Adicionando a música ao final da lista biblioteca.
biblioteca_musicas.append("Take me to church")
biblioteca_musicas.append("We hug now")
biblioteca_musicas.append("Hometown Glory")

#Imprimindo o catálogo para ver a ordem das músicas.
print(biblioteca_musicas)

#Buscando a música pelo índice fornecido.
buscar_musica = biblioteca_musicas[0]
print(buscar_musica)

#Removendo uma música pelo índice.
biblioteca_musicas.pop(2)

#Iprimindo após a remoção.
print(biblioteca_musicas)

#Verificando se uma música está na biblioteca.
verificar_musica = "Take me to church" in biblioteca_musicas
print(verificar_musica)


#FILA
from collections import deque

#Criando uma fila vazia
fila_de_atendimentos = deque()

#Adicionando pacientes à fila (enqueue)
fila_de_atendimentos.append("Théo - Check-up")
fila_de_atendimentos.append("Bela - Vacinação")
fila_de_atendimentos.append("Tico - Exame de rotina")
print(f"Fila de atendimentos do dia: {fila_de_atendimentos}")

#Atendendo o próximo paciente na fila (dequeue)
proximo_atendimento = fila_de_atendimentos.popleft()
print(f"Próximo paciente a ser atendido: {proximo_atendimento}")
print(f"Fila de atendimentos restantes: {fila_de_atendimentos}")

#Verificando o tamanho da fila
total_atendimentos_restantes = len(fila_de_atendimentos)
print("Número de atendimentos restantes na fila: ", total_atendimentos_restantes)

#Verificando se a fila está vazia
if not fila_de_atendimentos:
    print("Todos os pacientes foram atendidos.")
else:
    print("Ainda há pacientes aguardando atendimento.")


#PILHAS

#Criando uma pilha(lista vazia)
pilha_de_livros = []

#Empilhando livros (inserindo no final da lista)
pilha_de_livros.append("Nasce uma estrela")
pilha_de_livros.append("Bruxas da noite")
pilha_de_livros.append("Lady killers")

#Visualizando a pilha
print("Pilha de livros:", pilha_de_livros)

#Desempilhando o livro do topo
livro_utilizado = pilha_de_livros.pop()
print("Livro utilizado pelo Sábio:", livro_utilizado)

#Verificando se a pilha está vazia
print("A pilha está vazia?", len(pilha_de_livros) == 0)

#Visualizando os livros restantes
print("Livros restantes na pilha:", pilha_de_livros)

#Desempilhando os livros restantes, um por um
livro_utilizado = pilha_de_livros.pop()
print("Livro utilizado pelo Sábio:", livro_utilizado)

livro_utilizado = pilha_de_livros.pop()
print("Livro utilizado pelo Sábio:", livro_utilizado)

#Verificando a pilha ao final
print("A pilha está vazia ao final?", len(pilha_de_livros) == 0)



