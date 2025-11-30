from .carro import Carro

class Redondel:
    def __init__(self):
        self.vehiculos = [] 

    def agregar_vehiculo(self, carro: Carro):
        self.vehiculos.append(carro)

    def permitir_circulacion(self):
        
        # 1. VERIFICACIÓN
        hay_accidente = False
        for carro in self.vehiculos:
            if carro.colisionado:
                hay_accidente = True
                break 

        # 2. ACCIÓN
        if hay_accidente:
            print("!!! ACCIDENTE DETECTADO EN EL REDONDEL !!!")
            print("Ordenando a todos los vehículos que se detengan...")
            
            for carro in self.vehiculos:
                if carro.velocidad > 0:
                    carro.frenar()
                    
        else:
            print(f"--- Circulando {len(self.vehiculos)} vehículos normalmente ---")
            for carro in self.vehiculos:
                print(f"Carro {carro.id} avanzando por {carro.trayecto} a {carro.velocidad} km/h")