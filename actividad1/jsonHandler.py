import json

class JSONHandler():
    def __init__(self, file_name):
        self.file_name = file_name
    
    def save(self, lista):
        
        with open(self.file_name, 'w') as f:
            json.dump(lista, f)
            
    def open(self):
        with open(self.file_name, 'r') as f:
            lista = json.load(f)
        return lista

    def to_list(self):
         with open(self.file_name, "r") as json_file:
            data = json.load(json_file)
            lista = list(data)
            return lista
    
    