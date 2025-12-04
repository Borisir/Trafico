from .carro import Carro

class Redondel:
    def __init__(self, num_carros=15): # Aumenté un poco el número para ver mejor el efecto
        self.vehiculos = []
        separacion = 360 / num_carros
        
        for i in range(num_carros):
            # Velocidad max 2.5 para que sea fluido
            carro = Carro(i, velocidad_max=2.5, angulo_inicial=i * separacion)
            self.vehiculos.append(carro)

    def siguiente_paso(self):
        num = len(self.vehiculos)
        # Importante: Primero calculamos todo, luego movemos (para evitar condiciones de carrera en lógica)
        # Pero para una simulación simple, iterar directo funciona bien.
        
        for i in range(num):
            carro_actual = self.vehiculos[i]
            # Identificamos al carro de enfrente
            carro_enfrente = self.vehiculos[(i + 1) % num]
            
            carro_actual.actualizar(carro_enfrente)

    def obtener_estado(self):
        return [
            {
                "id": c.id, 
                "angulo": c.angulo, 
                "velocidad": c.velocidad,
                "frenado": c.frenado_manual,
                "alerta": c.velocidad < 0.2 and not c.frenado_manual # Flag para pintar en frontend
            } 
            for c in self.vehiculos
        ]

    def frenar_carro(self, id_carro):
        for c in self.vehiculos:
            if c.id == int(id_carro):
                c.forzar_frenado()