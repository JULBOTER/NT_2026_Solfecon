import pandas as pd
#tabla producto
from utils import simulacion
from notebook.limpieza import limpiar_datospro
#tabla linea
from utils import simulacion_lineas
from notebook.Limpiezalineas import limpiar_datos

#tabla productos
simulacionespro=simulacion.simular_producto(10)
simulaciones_ordenadaspro=pd.DataFrame(simulacionespro)
simulaciones_limpiaspro=limpiar_datospro(simulaciones_ordenadaspro)
print(simulaciones_limpiaspro)

#tabla lineas
simulaciones = simulacion_lineas.LineaProducto(10)  # Generar 1000 simulaciones
simulaciones_ordenadas=pd.DataFrame(simulaciones)
simulaciones_limpias=limpiar_datos(simulaciones_ordenadas)
print(simulaciones_limpias) 


