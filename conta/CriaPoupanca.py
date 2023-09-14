from conta.ContaPoupanca import ContaPoupanca
from conta.conta import Conta


class CriarPoupanca:
    if __name__ == '__main__':
        conta = Conta("21.342-7")
        conta2 = ContaPoupanca(conta)
        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())
        conta2.render_juros(0.01)
        print(conta.get_saldo())
