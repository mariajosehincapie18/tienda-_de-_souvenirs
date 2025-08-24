from producto import Producto
from producto import GestorProductos
from operaciones import Operaciones

pro = GestorProductos()
pro.precargar_productos_desde_txt("productos.txt")
pro.mostrar_productos()
op = Operaciones()
resultado =op.busqueda_binaria_por_nombre(pro.productos,"taza")
if resultado:
    print("\n🔎 Resultados encontrados:")
    print(resultado) 

else:
    print("\n❌ No se encontraron coincidencias.")



