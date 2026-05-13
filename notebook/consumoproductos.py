#Rutina para consumir APIS en python
#import requests

#def consumir_servicio_backendproductos():
 #   url="http://localhost:8080/producto"
  #  respuesta=requests.get(url)
    #respuesta.raise_for_status()
  #  datos=respuesta.json()
    #return datos
    
    #print(datos)
    
#consumir_servicio_backendproductos()


import requests
import pandas as pd

# 1. Configuración de visualización para ver el catálogo completo
pd.set_option('display.max_rows', None)      # Muestra todos los productos
pd.set_option('display.max_columns', None)   # Muestra todas las columnas (precio, stock, etc.)
pd.set_option('display.width', 1000)         # Maximiza el ancho para que no se amontone la info
pd.set_option('display.colheader_justify', 'center') # Centra los títulos de las columnas

def consumir_servicio_backendproductos():
    url = "http://localhost:8080/producto"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # 2. Convertimos a DataFrame
        df = pd.DataFrame(datos)
        
        # 3. Limpieza de columnas de relación
        # En productos solemos quitar las relaciones anidadas para que el print sea legible
        columnas_relacionales = ['mLinea', 'mPromocion', 'mCategorias']
        for col in columnas_relacionales:
            if col in df.columns:
                df = df.drop(columns=[col])
                
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el backend de productos: {e}")
        return pd.DataFrame()

# --- Ejecución ---

df_productos = consumir_servicio_backendproductos()

if not df_productos.empty:
    print("--- Catálogo Completo de Productos ---")
    # Imprimimos el DataFrame completo
    print(df_productos)
    
    print("\n--- Resumen Técnico ---")
    print(df_productos.info())
else:
    print("No se encontraron productos disponibles.")