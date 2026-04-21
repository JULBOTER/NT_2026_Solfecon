import pandas as pd
from utils import simulacion_lineas

simulaciones = simulacion_lineas.LineaProducto(1000)  # Generar 1000 simulaciones

simulaciones_ordenadas=pd.DataFrame(simulaciones)
print(simulaciones_ordenadas)


