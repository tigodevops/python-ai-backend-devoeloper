## Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável com (strings e número)

#Exemplos 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-5555"},
    "diego@gmail.com": {"nome": "Diego", "telefone": "5558-5551"},
    "hhrr@gmail.com": {"nome": "Henry", "telefone": "1238-5285"},
    "john@gmail.com": {"nome": "John", "telefone": "4563-1234"},

}

telefone = contatos["john@gmail.com"]["telefone"]

print(telefone)