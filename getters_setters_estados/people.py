class Pessoa: # substantivo
    
    def __init__(self, name: str, idade: int) -> None:
        self.name = name # substantivo
        self.idade = idade # substantivo
        
    def dirigir(self, veiculo: str) -> None: # verbos
        print('Dirigindo um(a) {}'.format(veiculo))
        
    def cantar(self) -> None: # verbos
        print('LaLaLa')
        
    def apresentar_idade(self) -> int: # verbos
        return self.idade