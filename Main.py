from Cliente import*
from Producto import*
from Tienda import*

if __name__ == "__main__":
 #inicio Atributos Cliente
 nombreCliente = input("ingrese el nombre del cliente ") 
 cantidadDinero= int(input("ingrese la cantidad de dinero que tiene ")) 
 cliente1 = Cliente(nombreCliente,cantidadDinero)
 #Fin Atributos Cliente

 #inicio Atributos Tienda
 """nombreTienda = input("ingrese el nombre de la tienda ") 
 nitTienda= input("ingrese el nit de la tienda ") 
 dirTienda= input("ingrese el nit de la tienda ") 
 telTienda= input("ingrese el telefono de la tienda ")"""
 principal = Tienda("Starbucks",1007348950,"cra 49 #52-26",5467812)
 #Fin Atributos Tienda

 #inicio Atributos Producto
 producto1 = Producto("Galletas",1121,9000,15,"sede1")
 producto2 = Producto("Pan",1122,5000,10,"sede2")
 producto3 = Producto("Tostadas",1123,7500,7,"sede3")
 #Fin Atributos Producto

 opt = 0 
 while opt != 8:
    opt = int(input("""Que accion desea Realizar: 
                    1. Abrir tienda
                    2. Ver productos
                    3. Cambiar precio al producto
                    4. Ver detalles de los productos
                    5. Comprar producto
                    6. Ver detalles del cliente
                    7. Cerrar tienda
                    8. Cerrar menu """))
    
    

    #opcion #1
    if opt == 1:
        if principal.estadoTienda == True:
         print("la tienda ya esta abierta ")
        elif principal.estadoTienda == False:
         print(principal.abrirTienda())
    
    #opcion #2
    elif opt == 2:
        print(producto1.verDetalles())
        print(producto2.verDetalles())
        print(producto3.verDetalles())

    #opcion #3
    elif opt == 3:
        optProducto = int(input(f"""que producto desea cambiar su precio
                               1. Producto #1 : {producto1.nombreProducto}
                               2. Producto #2 : {producto2.nombreProducto}
                               3. Producto #3 : {producto3.nombreProducto} """))
        if optProducto == 1:
            nuevoPrecioProducto = int(input("ingrese el nuevo valor para el producto "))
            print(producto1.cambiarPrecio(nuevoPrecioProducto))
        elif optProducto == 2:
            nuevoPrecioProducto = int(input("ingrese el nuevo valor para el producto "))
            print(producto2.cambiarPrecio(nuevoPrecioProducto))
        elif optProducto == 3:
            nuevoPrecioProducto = int(input("ingrese el nuevo valor para el producto "))
            print(producto3.cambiarPrecio(nuevoPrecioProducto))
    
    #opcion #4
    elif opt == 4:
        optProducto = int(input(f"""de que producto desea ver sus detalles
                               1. Producto #1 : {producto1.nombreProducto}
                               2. Producto #2 : {producto2.nombreProducto}
                               3. Producto #3 : {producto3.nombreProducto} """))
        if optProducto == 1:
           print(producto1.verDetalles())
        elif optProducto == 2:
           print(producto2.verDetalles())
        elif optProducto == 3:
           print(producto3.verDetalles())
        else:
           print("ingreso incorrecto")

        
    #opcion #5
    elif opt == 5:
      if principal.estadoTienda == True:
        optProducto = int(input(f"""que producto desea comprar
                               1. Producto #1 : {producto1.nombreProducto}
                               2. Producto #2 : {producto2.nombreProducto}
                               3. Producto #3 : {producto3.nombreProducto} """))
      
        if optProducto == 1:
            if cliente1.cantidadDinero > producto1.precioProducto :
              print(cliente1.comprarProducto(producto1.precioProducto))
              cliente1.historialCompras.append(producto1.nombreProducto)
              producto1.cantidadProducto= producto1.cantidadProducto - 1
            else: 
                print(f"no tienes el dinero suficiente para comprar el producto: {producto1.nombreProducto} ")
        

        elif optProducto == 2:
         
           if cliente1.cantidadDinero > producto2.precioProducto:
              print(cliente1.comprarProducto(producto2.precioProducto))
              cliente1.historialCompras.append(producto2.nombreProducto)
              producto2.cantidadProducto= producto2.cantidadProducto - 1
           else: 
                print(f"no tienes el dinero suficiente para comprar el producto: {producto2.nombreProducto} ")
         

        elif optProducto == 3:
         
           if cliente1.cantidadDinero > producto3.precioProducto:
              print(cliente1.comprarProducto(producto3.precioProducto))
              cliente1.historialCompras.append(producto3.nombreProducto)
              producto3.cantidadProducto= producto3.cantidadProducto - 1
           else: 
               print(f"no tienes el dinero suficiente para comprar el producto: {producto3.nombreProducto} ")
      else:
               print("la tienda esta cerrada no puedes comprar")
    
    #opcion #6
    elif opt == 6:
        print(cliente1.verDetalles())

    #opcion #7
    elif opt == 7:
        if principal.estadoTienda == False:
         print("la tienda ya esta cerrada ")
        elif principal.estadoTienda == True:
         print(principal.cerrarTienda())

        
else:
 print("no puedo ser importado,no soy un modulo ")

