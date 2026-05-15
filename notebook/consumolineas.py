#Rutina para consumir APIS en python
import requests

def consumir_servicio_backendlineas():
 url="http://localhost:8080/linea"
 respuesta=requests.get(url)
 respuesta.raise_for_status()
 datos=respuesta.json()
 print(datos)
 return datos
    
    