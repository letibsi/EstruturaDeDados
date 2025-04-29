#Aula 15/04/2025

#Passo 1: Criando uma lista vazia para armazenar os IDs das naves alienigenas
naves_alienigenas = []

#Passo 2: Adicionando IDs de novas naves alienigenas
naves_alienigenas.append("NaveAlfa-01")
naves_alienigenas.append("NaveBeta-05")
naves_alienigenas.append("NaveGama-12")
print(f"Naves alienígenas detectadas: {naves_alienigenas}")

#Passo 3: Acessando o ID da primeira nave detectada
primeira_nave = naves_alienigenas[0]
print(f"Primeira nave alienígena detectada: {primeira_nave}")

#Passo 4: Modificando o ID de uma nave (correção)
naves_alienigenas[1] = "NaveBeta-06"
print(f"Naves alienígenas atualizadas: {naves_alienigenas}")

#Passo 5: Removendo uma nave que deixou a órbita
naves_alienigenas.remove("NaveAlfa-01")
print(f"Naves restantes: {naves_alienigenas}")

#Passo 6: Verificando quantas naves ainda estão presentes
total_naves = len(naves_alienigenas)
print(f"Número total de naves na órbita: {total_naves}")

from collections import deque

#Passo 1: Criando uma fila vazia par as taredas da expedição
fila_de_tarefas = deque()

#Passo 2: Adicionando tarefas à fila (enqueue)
fila_de_tarefas.append("Verificar painéis solares")
fila_de_tarefas.append("Realizar experimento de gravidade")
fila_de_tarefas.append("Comunicar com a base terrestre")
print(f"Fila de tarefas da expedição: {fila_de_tarefas}")

#Passo 3: Executando a próxima tarefa na fila(dequeue)
proxima_tarefa = fila_de_tarefas.popleft()
print(f"Próxima tarefa na fila: {proxima_tarefa}")
print(f"Fila de tarefas restantes: {fila_de_tarefas}")

#Passo 4: Verificando o tamanho da fila
total_tarefas_restantes = len(fila_de_tarefas)
#print(f"Número de tarefas restantes na fila: {total_tarefas_restantes}")
print("Número de tarefas restantes na fila: ", total_tarefas_restantes)

#Passo 5: Verificando se a fila está vazia
if not fila_de_tarefas:
    print("Todas as tarefas foram concluídas.")
else:
    print("Ainda há tarefas pendentes.")

fila_de_atendimento_alienigena = deque()

fila_de_atendimento_alienigena.append("Zorg")
fila_de_atendimento_alienigena.append("Gleepglorp")
fila_de_atendimento_alienigena.append("Floopy")

print(f"Fila de atendimento alienígena: {fila_de_atendimento_alienigena}")

proximo_alienigena = fila_de_atendimento_alienigena.popleft()
print(f"Atendendo o alienigena: {proximo_alienigena}")
print(f"Fila de atendimento alienígena restante: {fila_de_atendimento_alienigena}")
