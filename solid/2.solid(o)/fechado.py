# Principio aberto / fechado

class Circo:

    
    def apresentar(self, tipo: int) -> None:
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:    
            self.apresentar_palhaco()
    
        
    def apresentar_malabarista(self):
        print("Malabarista apresentando seu show")
    
    
    def apresentar_palhaco(self):
        print("Palhaco apresentando seu show")
        

circo = Circo()
circo.apresentar(1)