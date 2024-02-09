class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        
    def correr(self):
        print('Estou correndo.')
        
    def beber(self, bebida, idade):
        if bebida == 'cerveja' and idade >= 18:
            self.__apesentar_document()
            print('Estou bebendo.')
        else:
            print('Posso beber qualquer coisa sem alcool, logo estou bebendo.')
                
    def __apesentar_document(self):
        print(self.__cpf)
        
diego = Pessoa('Diego', 27, '234fggh')
diego.beber('cerveja', diego.idade)

nathalia = Pessoa('Nathalia', 17, 'frg123h')
nathalia.beber('refri', nathalia.idade)