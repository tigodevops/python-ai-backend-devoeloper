class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def verificar_saldo(self):
        return self.saldo

    def mensagem_personalizada(self):
        saldo = self.verificar_saldo()

        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo < 50:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        else:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo_e_mensagem(self):
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("Digite seu nome: ")
nome_plano = input("Digite o nome do plano: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar saldo e mensagem:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo_e_mensagem()
print(mensagem_usuario)
