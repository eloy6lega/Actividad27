#POO : patrón de desarrollo. Clase - Objeto
#empresa : CRM : customer relationship manager
#cliente : objeto. clase (plantilla)
#propiedades: codigo, nif, nombre, email, ciudad, activo, descuento, fecha de alta...
#métodos: añadir al carrito, add lista de deseos, compra, pago, pago aplazado, seguimiento de la compra, devolución
#producto : objeto, clase (plantilla)
#propiedades: codigo, nombre, familia, precio, unitstock, descuento, fecha caducidad, externo
#métodos: pedirnuevostock, devolverproductodevuelto
#proveedor : clase. objeto
#pedidos : clase. objeto
#propiedades: fecha fact, numero fact, cliente, producto, fecha entrega, transportista
#métodos: firmarentrega

#Crear una clase, entidad, modelo, dataClass
class Cliente: #clase, entidad
    #propiedades / atributos / campos / adjetivos calificatibos
    def __init__(self,id,nombre,ciudad,prime): #constructor
        self.id=id
        self.nombre=nombre
        self.ciudad=ciudad
        self.prime=prime
    def comprar(self): #método de instancia
        print('Cliente compra') #implementar el método
    def valorar(self):
        print('Cliente valora la compra')
    def consultarFicha(self):
        print('-----------------------------------------------------------------------------------------')
        print('FICHA')
        print(f'Nombre: {self.nombre}\nCiudad: {self.ciudad}\nEres Prime?: {self.prime}')
        print('-----------------------------------------------------------------------------------------')
    def fichaPDF(self):
        print(f'Cliente {self.nombre} en PDF')

#usar la clase
cliente1=Cliente(1,'Carlos','Cartagena',True) #dar de alta un cliente. instanciar
print(cliente1.nombre)
cliente1.consultarFicha()
cliente1.fichaPDF()