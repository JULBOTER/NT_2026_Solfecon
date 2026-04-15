import random

def simular_producto(numeroSimulaciones):
    # Semillas
    idproducto=[1,2,3,4,5]
    descripcion = ["Martillo", "Sierra", "Cautin", "Brocha", "Galon de pintura"]
    precio = [53000, 150000, 45000, 12000, 345000]
    estado = ["Activo", "Activo", "Activo", "Inactivo", "Activo"]
    
    #imagen = ["", "", "", "", ""]
    
    idlinea = [2,2,2,1,1]
    idpromocion = [4, 4, 4, 4, 1]

    productos = []

    for _ in range(numeroSimulaciones):
        servicio = {
            "idproducto": random.choice(idproducto), # Corregido: singular
            "descripcion": random.choice(descripcion),
            "precio": random.choice(precio),
            "estado": random.choice(estado),   # Corregido: antes decía valores
            #"imagen": random.choice(imagen),
            "idlinea": random.choice(idlinea),
            "idpromocion": random.choice(idpromocion)
        }
        productos.append(productos)
        return productos
