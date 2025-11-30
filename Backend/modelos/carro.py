class Carro:
    def __init__(self, id, velocidad, trayecto, distancia_permitida):
        self.id = id
        self.velocidad = velocidad
        self.trayecto = trayecto  
        self.distancia_permitida = distancia_permitida
        self.colisionado = False  

    def frenar(self):
        self.velocidad = 0
        print(f"El carro {self.id} ha frenado.")

    def identificar_colision(self, distancia_objeto_cercano):
        if distancia_objeto_cercano < self.distancia_permitida:
            self.colisionado = True
            self.frenar()
            print(f"¡ALERTA! El carro {self.id} ha colisionado.")
            return True
        return False