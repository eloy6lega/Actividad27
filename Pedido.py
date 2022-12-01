#POO
#Pedido. clase, entidad
#atributos, campos, propiedades: id, fechaPedido, idCliente, idProducto, unidades
#métodos: comprar, devolver, facturarPDF, enviarSMS

from Cliente import Cliente #utilizar la clase Cliente de mi proyecto
from Producto import Producto


#nomenclatura ; mayúsculas, minúsculas, espacios
#camelCase : funciones
#snake_case : variables
#PascalCase : clases

class Pedido:
    def __init__(self,id,fecha_Pedido,id_Cliente,id_Producto,unidades):
        self.id=id
        self.fecha_pedido=fecha_Pedido
        self.id_cliente=id_Cliente
        self.id_producto=id_Producto
        self.uds=unidades
    def comprar(self):
        print('El cliente compra')
    def enviarSMS(self):
        print('Enviar SMS')
    def facturar(self):
        print(f'Factura: {self.id}\nNombre de cliente: {self.id_cliente}\nUnidades compradas: {self.uds}')

#crear un pedido
pedido1=Pedido('A1','10/05/2022',1,1,5) #No tiene en cuenta ni el cliente ni el producto
pedido1.facturar()
#crear otro pedido
cliente100=Cliente(100,'Maria','Fuengirola',True)
producto20=Producto(20,'Sombrero',15,12.99,'05/10/2022')
pedido2=Pedido('A2','11/05/2022',cliente100,producto20,7)
#fijate que puedes pasar como id_cliente como objeto porque id_cliente en pedidos es Any
pedido2.facturar()