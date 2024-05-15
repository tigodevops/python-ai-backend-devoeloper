contato = {"guilherme@gmail.com": {"nome":"Guilherme", "telefone": "3333-2221"}}

contato.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contato)

contato.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contato)