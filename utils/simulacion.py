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
        producto = {
            "idproducto": random.choice(idproducto), # Corregido: singular
            "descripcion": random.choice(descripcion),
            "precio": random.choice(precio),
            "estado": random.choice(estado),   # Corregido: antes decía valores
            #"imagen": random.choice(imagen),
            "idlinea": random.choice(idlinea),
            "idpromocion": random.choice(idpromocion)
        }
        #inyectando errores controlados
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            producto["idproducto"]=None
        elif(probabilidadError<0.3):
            producto["descripcion"]=random.choice(["cita medica","Inyección"])
        elif(probabilidadError<0.4):
            producto["precio"]=random.choice([0,-1000,None])
        elif(probabilidadError<0.5):
            producto["estado"] =random.choice(["Actualizado","Desactualizado"])
        elif(probabilidadError<0.6):
            producto["idlinea"]=None
        elif(probabilidadError<0.7):
            producto["idpromocion"]=None    


        productos.append(producto)
    return productos
