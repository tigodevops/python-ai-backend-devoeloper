## Interpolação de váriaveis ##

# Utilizando a % - menos recomendada hoje em dia.

nome = "Thiago"
idade = 33
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou iniciando no curso de %s ." % (nome, idade, profissao, linguagem))

## Metodo format 

print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou iniciando no curso de {}." .format(nome, idade, profissao, linguagem))

## Forma dois do format

print("Olá, me chamo {1}. Eu tenho {3} anos de idade, trabalho como {2} e estou iniciando no curso de {0}." .format(linguagem, nome, profissao, idade))

## Forma trê do format

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou iniciando no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

## Forma do "f" string ##

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou iniciando no curso de {linguagem}")

## Diminuindo casas decimais usando f string 

PI = 3.14159

print(f"Valor de PI {PI}")

#Sem espaço no final
print(f"Valor de PI: {PI:.2f}")

# incluindo espaço no final - nesse caso 10 é quantidade de espaço
print(f"Valor de PI: {PI:10.2f}")