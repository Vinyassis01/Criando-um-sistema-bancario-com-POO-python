from abc import ABC,classmethod,abstractmethod

class Cliente():
    def __init__ (self,nome):
        self.nome=nome
   
class Banco():
    def __init__ (self):
        super().__init__()
        self.cliente=Cliente()
        self.contas=[]
        self.saldo=0
        self.transacao=[]

    def criar_conta (self):
        return self.contas.append()

class Depositar():
    def __init__ (self,valor,saldo):
        super().__init__ (self.saldo)
        self.valor =valor
        self.saldo = saldo
        self.transacao.append("deposito")
        return saldo+=valor

class Sacar():
    def __init__ (valor,self,saldo):
        super().__init__(self.saldo)
        self.valor =valor
        self.saldo = saldo
        self.transacao.append("saque")
        return saldo-=valor
       
class Historico :
    def __init__(self):
        super().__init__(self.transacao)
        
    def historico():
        if Banco.depositar:
            Banco.transacao.append("deposito")
        if Banco.sacar:
            Banco.transacao.append("saque")

class Transacao:
    def __init__ (self):
        super().__init__ ()

    def transacao ():
        @property
        @abstractmethod
        def valor(self):
            return self.valor
        
        @classmethod
        @abstractmethod
        def registrar(self, contas):
            return self.contas.append()
        
class Pessoa_fisica:
    def __init__ (self):
        super().__init__ (self.cliente)

    def cliente(self):
       pass

class Extrato ():
    def __init__(self):
        super().__init__(self.transacao)    

    def extrato(self):
        return self.transacao
            

