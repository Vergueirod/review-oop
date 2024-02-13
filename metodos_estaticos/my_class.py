class MinhaClasse:
    
    def __init__(self, estado):
        self.estado = estado
        
    @staticmethod   # utilizar como especificador
    def metodo_estatico():
        #print(self.estado)
        print("Estou no meu metodo estatico")
        
obj = MinhaClasse(True)
obj.metodo_estatico()
#MinhaClasse.metodo_estatico()