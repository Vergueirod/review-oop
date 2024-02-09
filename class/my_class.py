# PascalCase or camelCase
class MyClass:
    
    def __init__(self, att): # atributos # esse é o construtor
        self.meu_atributo = 'Ola mundo'
        self.meu_atributo2 = att
    
    def my_method(self): # self or cls
        print(" I'm in the method! ")
        
    def my_method2(self, num, mult):
        return num * mult
        
        
#object = MyClass() # instanciando
#object.my_method()
#result = object.my_method2(3, 2) # acessando o metodo de desejo
#print(result)

#att = object.meu_atributo
#print(att)

object = MyClass('meu atributo')
print(object.meu_atributo2)