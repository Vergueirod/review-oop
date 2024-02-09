class Client:
    
    # atributes
    def __init__(self, name, cpf, interesse):
        self.name = name
        self.cpf = cpf
        self.interesse = interesse
        
    def client_buy(self, interesse):
        if interesse == 'comprar':
            print('é seu!')
            
        elif interesse == 'nao quero':
            print('volte outro dia')
    
user1 = Client('Diego', '422.605.548-90', 'comprar')
print(user1.name, user1.cpf, user1.interesse)
interesse_client = user1.client_buy(user1.interesse)
        
        
user2 = Client('Nathalia', '422.605.548-90', 'nao quero')
print(user2.name, user2.cpf, user2.interesse)
interesse_client = user2.client_buy(user2.interesse)