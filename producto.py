class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo:int = codigo
        self.nombre:str = nombre
        self.categoria:str = categoria
        self.precio:int = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}"

        


class Productos :
    def __init__(self):
        self.productos = []

    def agregar_productos(self, codigo:int, nombre:str, categoria:str, precio:str):
        nuevo_producto = Producto(codigo, nombre, categoria, precio)
        self.productos.append(nuevo_producto)
        return
    
    def agregar_productos_desde_archivo(ruta_archivo):
        pass


    def mostrar_productos(self, index = 0):

        if len(self.productos) == 0:
            return f"No hay productos"
        
        if index >= len(self.productos):
            return
        
        print(self.productos[index])

        self.mostrar_productos(index + 1)
        


        
        



tienda= Productos()
tienda.agregar_productos(11,"iman", "artesania", 1000)
tienda.agregar_productos(1,"botella", "artesania", 500)
tienda.agregar_productos(2,"iman grande", "artesania", 1700)
tienda.agregar_productos(0,"iman mini", "artesania", 1050)
tienda.mostrar_productos()
