# contexto que uma classe cria (contexto geral)
# contexto que um objeto possui (contexto declarado)
# o contexto da classe é passado para os objetos, MAS o contexto do objeto fica somente armazenados neles

class MinhaClasse:
    
    # estatico = 'vergueiro' # variavel de classe
    
    def __init__(self, estado):
        self.estado = estado # Atributo
        #self.estatico = 'vergueiro' # estado

    def print_estatico(self):
        print(self.estatico)
    
    @classmethod    
    def mudar_estatico(cls):
        cls.estatico = 'Programador'

        
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj1.print_estatico()
obj2.print_estatico()




'''
obj2 = MinhaClasse(False)

# obj1.estatico = 'Programador'
MinhaClasse.estatico = 'Programador'
obj1.estatico = 'Diego'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
'''
