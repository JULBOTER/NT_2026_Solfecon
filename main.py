import pandas as pd
from utils.simulacion_lineas import LineaProducto
from utils.simulacion import simular_producto

lineas = LineaProducto(1000)  # Generar 1000 simulaciones
lineas_ordenadas=pd.DataFrame(lineas)
print(lineas_ordenadas)

productos=simular_producto(1000)
productos_ordenados=pd.DataFrame(productos)
print(productos_ordenados)


