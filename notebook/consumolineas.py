#Rutina para consumir APIS en python
#import requests

#def consumir_servicio_backendlineas():
   # url="http://localhost:8080/linea"
    #respuesta=requests.get(url)
    #respuesta.raise_for_status()
   # datos=respuesta.json()
    #return datos
    
    #print(datos)
    
import requests
import pandas as pd

# 1. Configuración de Pandas para mostrar todas las filas y columnas en la terminal
pd.set_option('display.max_rows', None)      # Muestra todas las filas sin importar cuántas sean
pd.set_option('display.max_columns', None)   # Muestra todas las columnas
pd.set_option('display.width', 1000)         # Evita saltos de línea molestos si la tabla es ancha

def consumir_servicio_backendlineas():
    url = "http://localhost:8080/linea"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # 2. Convertimos la lista de diccionarios a un DataFrame
        df = pd.DataFrame(datos)
        
        # 3. Limpieza de columnas innecesarias (como mProducto)
        if 'mProducto' in df.columns:
            df = df.drop(columns=['mProducto'])
            
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el backend: {e}")
        return pd.DataFrame() # Devuelve un DataFrame vacío en caso de error

# --- Ejecución del código ---

# Obtenemos el DataFrame
df_lineas = consumir_servicio_backendlineas()

# Verificamos si el DataFrame tiene datos antes de imprimir
if not df_lineas.empty:
    print("--- Listado Completo de Líneas (12 registros) ---")
    # Al imprimir el df directamente, usará la configuración de set_option de arriba
    print(df_lineas)
    
    print("\n--- Estructura del DataFrame ---")
    print(df_lineas.info())
else:
    print("No se encontraron datos para mostrar.")
