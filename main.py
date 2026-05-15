
import pandas as pd
#tabla promociones
from notebook import consumopromociones
from notebook.limpiezapromociones import limpiar_datospromo
#tabla lineas
from notebook import consumolineas
from notebook.Limpiezalineas import limpiar_datoslinea
#Tabla productos
from notebook import consumoproductos
from notebook.limpiezaproductos import limpiar_datospro
#descripcion de productos
from notebook.descripcionproductos import describir_datos
#descripcion de lineas
from notebook.descripcionlineas import describir_lineas
#descripcion de promociones
from notebook.descripcionpromociones import describir_promociones
#analisis
from notebook.analisis import aplicar_analisis
from notebook.exportar import exportar_json
#analisis con relaciones
from notebook.analisisconrelaciones import aplicar_analisisrelaciones
from notebook.exportar import exportar_json


#PROMOCIONES 

# 1. Traes los datos (vienen con idPromocion)
simulacionespromo = consumopromociones.consumir_servicio_backendpromociones()

# 2. Creas el DataFrame
simulaciones_ordenadaspromo = pd.DataFrame(simulacionespromo)

# 3. ESTANDARIZACIÓN (La clave)
# Esto convierte 'idPromocion' -> 'idpromocion' y 'descripcionprom' -> 'descripcionprom'
simulaciones_ordenadaspromo.columns = simulaciones_ordenadaspromo.columns.str.lower()

# 4. Ahora la limpieza sí encontrará los campos en minúsculas
simulaciones_limpiaspromo = limpiar_datospromo(simulaciones_ordenadaspromo)

print(simulaciones_limpiaspromo)

#LINEAS 

# 1. Traes los datos (vienen con idLinea)
simulacioneslineas = consumolineas.consumir_servicio_backendlineas()

# 2. Creas el DataFrame
simulaciones_ordenadaslineas = pd.DataFrame(simulacioneslineas)

# 3. ESTANDARIZACIÓN (La clave)
# Esto convierte 'idLinea' -> 'idlinea' y 'descripcionlinea' -> 'descripcionlinea'
simulaciones_ordenadaslineas.columns = simulaciones_ordenadaslineas.columns.str.lower()

# 4. Ahora la limpieza sí encontrará los campos en minúsculas
simulaciones_limpiaslineas = limpiar_datoslinea(simulaciones_ordenadaslineas)

print(simulaciones_limpiaslineas)

#PRODUCTOS
# 1. Traes los datos (vienen con idProducto)
simulacionesproductos = consumoproductos.consumir_servicio_backendproductos()

# 2. Creas el DataFrame
simulaciones_ordenadasproductos = pd.DataFrame(simulacionesproductos)

# 3. ESTANDARIZACIÓN (La clave)
# Esto convierte 'idProducto' -> 'idproducto' y 'descripcionprod' -> 'descripcionprod'
simulaciones_ordenadasproductos.columns = simulaciones_ordenadasproductos.columns.str.lower()

# 4. Ahora la limpieza sí encontrará los campos en minúsculas
simulaciones_limpiasproductos = limpiar_datospro(simulaciones_ordenadasproductos)

print(simulaciones_limpiasproductos)
#describiendo los productos
describir_datos(simulaciones_limpiasproductos)

#describiendo las lineas
describir_lineas(simulaciones_limpiaslineas)

#describiendo las promociones
describir_promociones(simulaciones_limpiaspromo)

preguntas = aplicar_analisis(simulaciones_limpiasproductos)
exportar_json(preguntas)

preguntasrelaciones = aplicar_analisisrelaciones(
    simulaciones_limpiasproductos,
    simulaciones_limpiaslineas,
    simulaciones_limpiaspromo
)
exportar_json(preguntasrelaciones)

