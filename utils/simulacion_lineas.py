import random

def LineaProducto(numeroSimulaciones):

    #semillas por caada atributo de mi tabla 
    descrpciones=["Pinturas y accesorios","Construccion","Plomeria y gas","Electricos","Herramientas"]
    imagenes=["/img/Pinturas.webp", "/img/construccion.webp", "/img/Electricos.jfif", "/img/Plomeria.jfif", "/img/Herramientas.jfif"]
    codigos=[11,12,13,14,15]
    

    servicios=[]

    for _ in range (numeroSimulaciones):
        servicio={
            "id":random.choice(codigos),
            "descripcion":random.choice(descrpciones),
            "imagen":random.choice(imagenes)
        }

        #inyectando errores controlados 
        probabilidad_error=random.random()
        if probabilidad_error < 0.33:  
            servicio["id"] = None  
        elif probabilidad_error < 0.66: 
            servicio["descripcion"] = " "+servicio["descripcion"].upper() # Simulando un error al generar la descripción
        elif probabilidad_error < 0.9:  
            servicio["imagen"] = None  

        servicios.append(servicio)
    return servicios