arquivo = open("I:/dio-git-e-github/python-ai-backend-developer/05 - Manipulação de arquivos/teste.txt", 'w'

)

print(arquivo.write("Escrevendo um texto."))
print(arquivo.writelines(["\n", "escrevendo", "\n", "novo", "\n","texto", "\n",  "teste"]))

arquivo.close()