import pandas as pd
from utils import simulacion_lineas
from notebook.Limpiezalineas import limpiar_datos


simulaciones = simulacion_lineas.LineaProducto(10)  # Generar 1000 simulaciones

simulaciones_ordenadas=pd.DataFrame(simulaciones)
simulaciones_limpias=limpiar_datos(simulaciones_ordenadas)

print(simulaciones_limpias)


