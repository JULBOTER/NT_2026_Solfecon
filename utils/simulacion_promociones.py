import random

def simular_promocion(numeroSimulaciones):
    #semillas para cada atributo de mi tabla
    descripciones=["Navidad","Saldos","Productos Seguridad","Sin Promoción"]
    imagenes=["/img/Navidad.webp", "/img/Saldos.webp", "/img/Seguridad.webp", "/img/SinPromocion.webp"]
    codigos=[1,2,3,4]
    descuentos=[30,50,10,0]

    promociones=[]

    for _ in range (numeroSimulaciones):
        promocion={
            "id":random.choice(codigos),
            "descripcion":random.choice(descripciones),
            "imagen":random.choice(imagenes),
            "descuento":random.choice(descuentos)
        }

        #inyectando errores controlados 
        probabilidad_error=random.random()
        if probabilidad_error < 0.33:  
            promocion["id"] = None  
        elif probabilidad_error < 0.70:
            promocion["descuento"] =None    
        
        elif probabilidad_error < 0.9:  
            promocion["imagen"] = None  

        promociones.append(promocion)
    return promociones


