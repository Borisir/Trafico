import math

class Carro:
    def __init__(self, id, velocidad_max, angulo_inicial):
        self.id = id
        self.velocidad_max = velocidad_max
        self.velocidad = velocidad_max
        self.angulo = angulo_inicial
        
        # Estado
        self.frenado_manual = False
        self.ciclos_frenado_restantes = 0 # Contador para volver a acelerar
        
        # Física
        self.aceleracion = 0.1       # Aceleración suave para recuperar marcha
        self.frenado_suave = 0.2     # Frenado sutil (lo que pediste)
        self.frenado_fuerte = 1.0    # Frenado de emergencia para no chocar
        
        # Distancias (en grados del redondel)
        self.distancia_seguridad = 25.0  # Distancia donde empieza a soltar el acelerador
        self.distancia_critica = 8.0     # Distancia donde frena fuerte

    def actualizar(self, carro_enfrente):
        # 1. Calcular distancia con el de enfrente
        if carro_enfrente:
            # Fórmula para distancia circular positiva
            distancia = (carro_enfrente.angulo - self.angulo) % 360
            # Corrección: si están muy cerca pero el cálculo dio la vuelta (360), ajustamos
            if distancia == 0: distancia = 0.1 
        else:
            distancia = 999 

        # ---------------- LÓGICA DE CONTROL ----------------

        # CASO A: El usuario frenó este carro manualmente
        if self.frenado_manual:
            self.velocidad = 0
            self.ciclos_frenado_restantes -= 1
            
            # Si se acabó el tiempo de espera, soltamos el freno
            if self.ciclos_frenado_restantes <= 0:
                self.frenado_manual = False
                print(f"Carro {self.id} reanudando marcha...")

        # CASO B: Conducción automática
        else:
            # 1. Si estamos demasiado cerca (Emergencia) -> Evitar choque a toda costa
            if distancia < self.distancia_critica:
                self.velocidad = max(0, self.velocidad - self.frenado_fuerte)
            
            # 2. Si estamos entrando en zona de precaución -> Frenado sutil
            elif distancia < self.distancia_seguridad:
                # Factor proporcional: cuanto más cerca, más frena, pero empieza suave
                factor = (self.distancia_seguridad - distancia) / self.distancia_seguridad
                frenado_actual = self.frenado_suave + (factor * 0.5)
                
                # Ajustamos velocidad para igualar al de enfrente (evita el efecto elástico excesivo)
                velocidad_objetivo = carro_enfrente.velocidad if carro_enfrente else 0
                
                if self.velocidad > velocidad_objetivo:
                    self.velocidad -= frenado_actual
                
                # Nunca retroceder
                self.velocidad = max(0, self.velocidad)

            # 3. Si hay espacio libre -> Acelerar
            else:
                if self.velocidad < self.velocidad_max:
                    self.velocidad += self.aceleracion

        # ---------------- MOVIMIENTO ----------------
        self.angulo = (self.angulo + self.velocidad) % 360

    def forzar_frenado(self):
        self.frenado_manual = True
        # El carro se detendrá por 30 ciclos de simulación (aprox 3 segundos si vas a 10FPS)
        self.ciclos_frenado_restantes = 2
        self.velocidad = 0