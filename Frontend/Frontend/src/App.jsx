import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [carros, setCarros] = useState([])

  useEffect(() => {
    const intervalo = setInterval(() => {
      fetch('http://localhost:5000/api/estado')
        .then(res => res.json())
        .then(data => setCarros(data))
        .catch(err => console.error("Error backend:", err))
    }, 100) // 10 FPS
    return () => clearInterval(intervalo)
  }, [])

  const manejarFrenado = (id) => {
    fetch(`http://localhost:5000/api/frenar/${id}`, { method: 'POST' })
  }

  const reiniciarSimulacion = () => {
    fetch(`http://localhost:5000/api/reiniciar`, { method: 'POST' })
  }

  return (
    <div>
      <h1>Simulación de Tráfico</h1>
      
      <div className="contenedor-principal">
        
        {/* IZQUIERDA: Panel de Control */}
        <div className="panel-control">
          <button className="btn-reiniciar" onClick={reiniciarSimulacion}>
            Reiniciar Todo
          </button>
          
          <table className="tabla-carros">
            <thead>
              <tr>
                <th>Auto ID</th>
                <th>Velocidad</th>
                <th>Acción</th>
              </tr>
            </thead>
            <tbody>
              {carros.map(carro => (
                <tr key={carro.id} style={{ 
                    backgroundColor: carro.frenado ? '#ffcccc' : (carro.alerta ? '#fff4e5' : 'transparent') 
                  }}>
                  <td><strong>{carro.id}</strong></td>
                  <td>{carro.velocidad.toFixed(1)} km/h</td>
                  <td>
                    <button 
                      className="btn-frenar"
                      onClick={() => manejarFrenado(carro.id)}
                      disabled={carro.frenado} // Deshabilitar si ya está frenado manualmente
                    >
                      {carro.frenado ? 'Detenido' : 'Frenar'}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* DERECHA: Simulación Visual */}
        <div className="panel-simulacion">
          <div className="carretera">
            {carros.map((carro) => (
              <div
                key={carro.id}
                style={{
                  position: 'absolute',
                  width: '40px',
                  height: '20px',
                  // Colores: Rojo (Manual), Naranja (Alerta/Frenando auto), Azul (Normal)
                  backgroundColor: carro.frenado ? '#ff4444' : (carro.alerta ? 'orange' : '#2196F3'),
                  top: '50%',
                  left: '50%',
                  // La transformación matemática para posicionarlos en círculo
                  transform: `translate(-50%, -50%) rotate(${carro.angulo}deg) translate(160px) rotate(90deg)`,
                  borderRadius: '4px',
                  color: 'white',
                  fontSize: '10px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: '0 0 2px black',
                  transition: 'transform 0.1s linear, background-color 0.2s'
                }}
              >
                {carro.id}
              </div>
            ))}
          </div>

        </div>

      </div>
    </div>
  )
}

export default App