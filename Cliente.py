if __name__ == "__main__":
    print("no me puedo ejecutar soy un modulo")
else:
    
  class Cliente():

      def __init__(self,nombreCliente,cantidadDinero):
          self.nombreCliente = nombreCliente
          self.cantidadDinero = cantidadDinero
          self.historialCompras = []

      def comprarProducto(self,precioProducto):
          self.cantidadDinero = self.cantidadDinero - precioProducto
          return f"su compra se ha realizado con exito"

      def verDetalles(self):
          return f"""
                     su nombre es : {self.nombreCliente}
                     su dinero restante es de : {self.cantidadDinero} 
                     sus compras han sido {self.historialCompras}"""
      
      


          