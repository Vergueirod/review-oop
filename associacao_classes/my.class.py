from typing import Type

############################
# Interruptor
############################


class Interruptor:
    
    
    def __init__(self, comodo: str):
        self.__comodo = comodo
        
        
    def acender(self):
        print(f"Acendendo {self.__comodo}")
        
        
    def apagar(self):
        print(f"Apagando {self.__comodo}")
 
 
############################
# Pessoa
############################     


class Pessoa:
    
    
    def acenderLuzes(self, interruptor: Type[Interruptor] ):
        interruptor.acender()
    
    
    def apagarLuzes(self, interruptor: Type[Interruptor] ):
        interruptor.apagar()
    
    
    def dormir(self):
        print("Fui dormir...")
        
        
diego = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()
diego.acenderLuzes(interruptor_quarto)