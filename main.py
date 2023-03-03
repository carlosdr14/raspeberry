import distancia
import led
import humedad


class Menu():
    def humedad(self):
        humedad.humedad()
    
    def distancia(self):
        distancia.distancia()
    
    def led(self):
        led.led()

    def menu(self):
        print("1. Humedad")
        print("2. Distancia")
        print("3. Led")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            self.humedad()
        elif opcion == 2:
            self.distancia()
        elif opcion == 3:
            self.led()
        elif opcion == 4:
            exit()
        else:
            print("Opcion invalida")
            self.menu()

if __name__ == "__main__":
    menu = Menu()
    menu.menu()