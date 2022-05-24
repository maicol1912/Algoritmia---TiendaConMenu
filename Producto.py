from Tienda import Tienda
if __name__ == "__main__":
    print("no me puedo ejecutar soy un modulo")
else:
    class Producto:
        def __init__(self,nombreProducto,codProducto,precioProducto,cantidadProducto,sede):
            self.nombreProducto = nombreProducto
            self.codProducto = codProducto
            self.precioProducto = precioProducto
            self.cantidadProducto = cantidadProducto
            self.sede = sede
            
            
        def cambiarPrecio(self,nuevoPrecioProducto):
            self.precioProducto = nuevoPrecioProducto
            return f"el precio ha sido cambiado con exito"
 
        def verDetalles(self):
            return f"""el nombre del producto es : {self.nombreProducto}
                       el codigo del producto es : {self.codProducto}
                       el precio del producto es : {self.precioProducto}
                       la cantidad de este producto es : {self.cantidadProducto}
                       en la sede que esta disponible en : {self.sede}"""

        