
import time

class Cliente:
    def __init__(self, nombre, correo, edad, pais):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.pais = pais
    
    def __str__(self):
        return f"Se ha creado el cliente {self.nombre}"

    def comprar(self):
        articulo = input("¿Que articulo desea comprar? ")
        tienda = input("¿Donde lo desea comprar? ")
        print("")
        time.sleep(0.5)
        print("Realizando transacción...\n")
        time.sleep(0.5)
        print(f"El cliente {self.nombre} ha comprado {articulo} en {tienda}")

    def confirmar(self):
        print("")
        confirmacion = input("Desea confirmar la compra? S/N: ").capitalize()
        time.sleep(0.5)
        print("")
        if confirmacion == "S":
            print("Compra confirmada con éxito.")
        elif confirmacion == "N":
            print("Compra cancelada con éxito.")
        else:
            print("Esa opción no existe.")

cliente1 = Cliente("Franco", "frankovalli123@gmail.com", 17, "Argentina")
time.sleep(0.5)
print(cliente1)
cliente1.comprar()
cliente1.confirmar()