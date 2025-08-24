from producto import Producto
from producto import GestorProductos
from operaciones import Operaciones

pro = GestorProductos()
pro.precargar_productos_desde_txt("productos.txt")
pro.mostrar_productos()
op = Operaciones()
resultado =op.busqueda_binaria_por_nombre(pro.productos,"Taza cafetera")
if resultado:
    print("\n🔎 Resultados encontrados:")
    print(resultado) 

else:
    print("\n❌ No se encontraron coincidencias.")


calculo_prodctos = op.calculo_total_de_precios(pro.productos)
print(calculo_prodctos)

calculo_promedio = op.calculo_promedio_por_categoria(pro.productos, "souvenir")
print(calculo_promedio)


filtro_rango = op.busqueda_por_rango_de_precios(pro.productos,120,200)
print(filtro_rango)


reco = op.recomendaciones(pro.productos,"pin",)
print(reco)


seleccionado = op.busqueda_binaria_por_nombre(pro.productos, "pin")
if seleccionado:
    sugerencia = op.recomendaciones(pro.productos,seleccionado)
    print(sugerencia)
