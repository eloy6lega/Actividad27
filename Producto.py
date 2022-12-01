#POO
#entidad : Producto. clase
#propiedades, campos, atributos: id, nombre, unidades, precio, fechaFabricación
#métodos: reponerStock, aplicarDescuento

class Producto: #clase, entidad, modelo
    def __init__(self,id,nombre,unidades,precio,fechaFabricacion): #constructor
        self.id=id #almacenar la instancia en el parámetro
        self.nombre=nombre #string
        self.uds=unidades #entero
        self.precio=precio #con decimales
        self.fechaFab=fechaFabricacion #fecha
        #python utiliza inferencia de tipos. Por eso NO es necesario indicar el tipo de datos al almacenar la variable
        #si python NO tiene todavía el dato, por defecto el tipo es Any

        #explicar en la memoria qué diferencia hay entre tipado fuerte, débil e inferencia de tipado
        #compilados habitualmente tipado fuerte
        #interpretados suelen usar tipado por inferencia o a veces, tipado débil

    def reponerStock(self):
        if self.uds<10:
            print('Tenemos que pedir unidades para evitar roturas de stock')
        else:
            print(f'Mi stock actual es de {self.uds}')

producto1=Producto(100,'camisa',50,9.99,'10/05/2022')
producto1.reponerStock()
producto2=Producto(200,'pantalon',9,19.99,'10/05/2022')
producto2.reponerStock()
