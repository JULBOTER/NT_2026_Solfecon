#Rutina para consumir APIS en python
import requests

def consumir_servicio_backendpromociones():
  url="http://localhost:8080/promocion"
  respuesta=requests.get(url)
  respuesta.raise_for_status()
  datos=respuesta.json()
  print(datos)
  return datos
    


