import json
from jsonHandler import JSONHandler

class LISTA(JSONHandler):
    def __init__(self):
        self.lista = []
        
    def agregar(self, elemento):
        self.lista.append(elemento)
        
    def modificar(self, elemento_viejo, elemento_nuevo):
        indice = self.lista.index(elemento_viejo)
        self.lista[indice] = elemento_nuevo
        
    def eliminar(self, elemento):
        self.lista.remove(elemento)
        
    def buscar(self, elemento):
        return elemento in self.lista

   
    

    

    
