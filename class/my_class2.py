class RemoteControl:
    
    # caracteristicas = Atributo
    def __init__(self, television, comodo):
        self.television = television
        self.comodo = comodo
        
    # acoes = metodo
    def avancar_canal(self):
        print('Canal avancado.')
    
    def voltar_canal(self):
        print('Voltar o canal.')
    
    def escolher_canal(self, canal):
        print(f' Alterado para o canal: {canal}')
        
controle_sala = RemoteControl('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.television)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = RemoteControl('lg', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.television)
controle_quarto.voltar_canal()