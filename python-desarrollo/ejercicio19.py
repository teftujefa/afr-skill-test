class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= monto

    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Ana", 100)
cuenta.depositar(50)
cuenta.retirar(200)
print(cuenta.obtener_saldo())