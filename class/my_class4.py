n = 'Diego'
c = '4234'

class ClientBank:
    
    def __init__(self, name, cpf, account, password, bank):
        
        self.name = name
        self.cpf = cpf
        self.account = account
        self.password = password
        self.bank = bank
        
    def auth_client(self, name, cpf):
        
        if name == n and cpf == c:
            print(f'Olá {name}, seja bem vindo(a)')
        else:
            print('Acesso negado.')


client1 = ClientBank('Diego', '4234', '123', '321', 'BTG')
#autentication = client1.auth_client(client1.name, client1.cpf)
print(f"User {client1.name} use the bank: {client1.bank}")

