class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo:str = codigo
        self.nombre:str = nombre
        self.categoria:str = categoria
        self.precio:float = precio

    def __str__(self):
        return f"🏷️: {self.codigo}, 📝: {self.nombre}, 🗂️: {self.categoria}, 💰: {self.precio}"
    
    def __repr__(self):
        return str(self)


class GestorProductos :
    def __init__(self):
        self.productos = []

    def agregar_productos(self, codigo:str, nombre:str, categoria:str, precio:float):
        nuevo_producto = Producto(codigo, nombre, categoria, precio)
        self.productos.append(nuevo_producto)
        return
    
    def precargar_productos_desde_txt(self, ruta_archivo):
        with open(ruta_archivo,"r",encoding="utf-8") as archivo:
            self.cargar_recursivo(archivo)

        self.ordenar(self.productos, len(self.productos))

    def cargar_recursivo(self, archivo):
        linea = archivo.readline()
        if not linea:
            return
        linea = linea.strip()
        if linea:
            partes= linea.split(",")
            if len(partes) == 4:
                codigo, nombre, categoria, precio = partes
                self.agregar_productos(codigo.strip(), nombre.strip(), categoria.strip(),float(precio))

        self.cargar_recursivo(archivo)

    def ordenar(self,productos,n):
        if n <= 1:
            return
        self.ordenar(productos, n-1)
        ultimo = productos[n-1]
        self.insertar(productos, n-1, ultimo)

    def insertar(self, productos, j, valor):
        if j <= 0 or productos[j-1].nombre.lower() <= valor.nombre.lower():
            productos[j] = valor
            return
        
        productos[j] = productos[j-1]
        self.insertar(productos,j-1,valor)
    


    def mostrar_productos(self, index = 0):

        if len(self.productos) == 0:
            return f"No hay productos"
        
        if index >= len(self.productos):
            return
        
        print(self.productos[index])

        self.mostrar_productos(index + 1)
        


        
        



