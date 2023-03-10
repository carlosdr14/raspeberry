import socket
import pymongo

class CheckInternet():
    def __init__(self):
        self.status = None
        self.message = None
  
    
    def is_connected(self):
        try:
            # intenta conectarse a google para verificar la conexión a Internet
            socket.create_connection(("www.google.com", 80))
            self.status = True
            self.message = "Conexión a Internet establecida"
        except OSError:
            self.status = False
            self.message = "No se pudo establecer una conexión a Internet"
        return (self.status, self.message)
    
    def mongo_connect(self):
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Nadia"]
            print("Connected to MongoDB")
            
       
       
        


check_internet = CheckInternet()
status, message = check_internet.is_connected()
print(status)
print(message)
