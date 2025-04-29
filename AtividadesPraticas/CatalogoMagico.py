#Biblioteca Mágica (Listas)

#Criando um alista vazia.
catalogo_magico = []

#Adicionando o livro ao final da lista catalogo.
catalogo_magico.append("O Feitiço da Lua Crescente")
catalogo_magico.append("A Jornada do Unicórnio Perdido")
catalogo_magico.append("Segredos da Floresta Encantada")

#Imprimindo o catálogo para ver as ordem dos livros.
print(catalogo_magico)

#Buscando livro pelo índice fornecido.
buscar_livro = catalogo_magico[1]
print(buscar_livro)

#Removendo um livro do índice.
catalogo_magico.pop(2)

#Imprimindo catálogo após a remoção.
print(catalogo_magico)

#Verificando se o livro está no catálogo.
verificar_livro = "Segredos da Floresta Encantada" in catalogo_magico
print(verificar_livro)
