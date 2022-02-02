class Banco:
    def __init__(self):
        self.agencias = [1017]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            print(f'Cliente {cliente} não encontrado no banco de dados da instituição.')
            return False

        if cliente.conta not in self.contas:
            print(f'Conta {cliente.conta} não encontrada no banco de dados da instituição.')
            return False

        if cliente.conta.agencia not in self.agencias:
            print(f'Agência {cliente.conta.agencia} não pertence ao banco de dados da instituição.')
            return False

        return True
