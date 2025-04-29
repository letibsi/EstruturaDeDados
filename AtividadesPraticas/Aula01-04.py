#AULA 01/04

#Fazer um algoritmo que leia as notas de 10 alunos de uma classe e ao final infome a média desses alunos.

media_alunos = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
media = sum(media_alunos) / len(media_alunos)
print("A média da classe é:", media)

#Crie um vetor de inteiros ( int ) de 10 posições. Preencha-o com os valores 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 e 100 . Use um for para exibir os valores deste vetor

vetor = int
vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for valor in vetor:
  print(valor)

#Crie uma matriz de caracteres ( char ) de 16 posições (4x4). Preencha-a com os valores a , b , c , d , e , f , g , h , i , j ,
#k , l , m , n , o e p . Use dois for para exibir os valores desta matriz.

matriz = ["a","b","c","d"
          "e", "f", "g", "h"
          "i", "j", "k", "l"
          "m","n", "o", "p"
          ]
for linha in matriz:
  for caractere in linha:
    print(caractere, end = '')
    print()
