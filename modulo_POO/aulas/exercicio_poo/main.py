"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente tem conta (agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança ou ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter método sacar abstrato (abrastração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticaçãoo do banco (descrita acima)
"""
from modulo_POO.aulas.exercicio_poo.contas import Conta
from modulo_POO.aulas.exercicio_poo.clientes import Cliente
from modulo_POO.aulas.exercicio_poo.banco import Banco

banco = Banco()
kilder = Cliente(nome='Kilder Colvalan', idade=29)
kilder.contacorrente(agencia=1017, conta=81652, saldo=0)
banco.inserir_cliente(kilder)
banco.inserir_conta(kilder.conta)
if banco.autenticar(kilder):
    kilder.conta.depositar(10)
    kilder.conta.sacar(150)
