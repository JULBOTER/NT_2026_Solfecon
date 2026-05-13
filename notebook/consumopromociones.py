#Rutina para consumir APIS en python
import requests

#def consumir_servicio_backendpromociones():
 #   url="http://localhost:8080/promocion"
   # respuesta=requests.get(url)
   # respuesta.raise_for_status()
    #datos=respuesta.json()
    #return datos
    
    #print(datos)
    
#consumir_servicio_backendpromociones()

import requests
import pandas as pd

# 1. Configuración de Pandas para ver todos los datos en la terminal
pd.set_option('display.max_rows', None)      # Muestra todas las promociones
pd.set_option('display.max_columns', None)   # Muestra todas las columnas
pd.set_option('display.width', 1000)         # Evita saltos de línea

def consumir_servicio_backendpromociones():
    url = "http://localhost:8080/promocion"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # 2. Convertimos a DataFrame para mejor manipulación
        df = pd.DataFrame(datos)
        
        # 3. Limpieza: Eliminamos columnas de relación si existen (similar a mProducto)
        # Esto es útil si tu backend de Spring Boot devuelve objetos anidados
        columnas_a_eliminar = ['mProducto', 'mLinea'] 
        for col in columnas_a_eliminar:
            if col in df.columns:
                df = df.drop(columns=[col])
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el backend de promociones: {e}")
        return pd.DataFrame()

# --- Ejecución ---

df_promociones = consumir_servicio_backendpromociones()

if not df_promociones.empty:
    print("--- Listado Completo de Promociones ---")
    # Al imprimir el DF sin .head(), verás todas las filas gracias al set_option
    print(df_promociones)
    
    print("\n--- Información de la Tabla ---")
    print(df_promociones.info())
else:
    print("No se pudieron cargar las promociones.")