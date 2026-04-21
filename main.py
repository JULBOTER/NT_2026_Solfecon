import pandas as pd
from utils.simulacion import simular_producto

productos=simular_producto(100000)
productos_ordenados=pd.DataFrame(productos)
print(productos_ordenados)
