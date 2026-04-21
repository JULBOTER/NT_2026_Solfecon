import random

def LineaProducto(numeroSimulaciones):

    #semillas por caada atributo de mi tabla 
    descripciones=["Pinturas y accesorios","Construccion","Plomeria y gas","Electricos","Herramientas"]
    imagenes=["/img/Pinturas.webp", "/img/construccion.webp", "/img/Electricos.jfif", "/img/Plomeria.jfif", "/img/Herramientas.jfif"]
    codigos=[11,12,13,14,15]
    

    lineas=[]

    for _ in range (numeroSimulaciones):
        linea={
            "id":random.choice(codigos),
            "descripcion":random.choice(descripciones),
            "imagen":random.choice(imagenes)
        }

        #inyectando errores controlados 
        probabilidad_error=random.random()
        if probabilidad_error < 0.33:  
            linea["id"] = None  
        elif probabilidad_error < 0.66: 
            linea["descripcion"] = " "+linea["descripcion"].upper() # Simulando un error al generar la descripción
        elif probabilidad_error < 0.9:  
            linea["imagen"] = None  

        lineas.append(linea)
    return lineas