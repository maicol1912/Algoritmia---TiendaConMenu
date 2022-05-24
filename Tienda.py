if __name__ == "__main__":
   print("no me puedo ejecutar soy un modulo")
else:
 class Tienda():   
    def __init__(self,nombreTienda,nitTienda,dirTienda,telTienda):
        self.nombreTienda= nombreTienda
        self.nitTienda = nitTienda
        self.dirTienda = dirTienda
        self.tel = telTienda
        self.estadoTienda = False

    def __str__(self):
            return f"el nombre de la tienda es {self.nombreTienda}"

    def abrirTienda(self):
        self.estadoTienda = True
        return f"la tienda ha sido abierta"

    def cerrarTienda(self):
        self.estadoTienda = False
        return f"la tienda ha sido cerrada"









