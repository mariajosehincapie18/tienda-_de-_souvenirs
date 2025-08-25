from producto import Producto
from producto import GestorProductos
from operaciones import Operaciones


class Menu:
    def mostrar_menu(self):
        print("\n--- BIENVENIDO A COLOMBIA SOUVENIRS ---")
        print("1️⃣   BUSQUEDA POR NOMBRE")
        print("2️⃣   CALCULO TOTAL DE PRODUCTOS")
        print("3️⃣   CALCULO PROMEDIO POR CATEGORIA ")
        print("4️⃣   QUICKSORT")
        print("5️⃣   BUSQUEDA POR RANGO DE PRECIOS")
        print("6️⃣   RECOMENDACIONES ")
        print("7️⃣   LISTADO DE PRODUCTOS ORGANIZADOS ALFABETICAMENTE")

        print("❌ SALIR")


        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto_buscar = input("🔎 INGRESE EL PROUCTO QUE DESEA BUSCAR:  ")
            resultado =op.busqueda_binaria_por_nombre(pro.productos, producto_buscar.lower())
            if resultado:
                op.imprimir_lista(resultado) 
            else:
                print("⚠️​No se encontraron elementos")         
            
            self.mostrar_menu()   

        elif opcion == "2":
            calculo_prodctos = op.calculo_total_de_precios(pro.productos)
            print("TOTAL: 💲​ ", calculo_prodctos)
            self.mostrar_menu()   

        elif opcion == "3":
            print("🔎 ingresa la categoria para consultar el promedio:")
            categoria = input("'Artesania', 'souvenir', 'ropa', 'accesorio':  ")
            calculo_promedio = op.calculo_promedio_por_categoria(pro.productos, categoria.lower())
            print("TOTAL: 💲​", calculo_promedio)
            self.mostrar_menu()

        elif opcion == "4": 
            opcion =input("🔎 Ingresa el orden que quieres tus productos 'menor' o 'mayor':  ")   
            quick = op.Quicksort_precio(pro.productos,opcion.lower())
            print(quick)    
            self.mostrar_menu()

        elif opcion == "5":
            print("💲​MONEDA COLOMBIANA💲​ ")
            print("✔️ Precios apartir de 10.000")
            rango_menor= float(input("➖ ingrese el rango minimo de precio:   "))
            rango_mayor= float(input("➕​ ingrese el rango maximo de precio:  "))
            filtro_rango = op.busqueda_por_rango_de_precios(pro.productos, rango_menor,rango_mayor)
            print(f"✔️  PRODUCTOS DESDE 💲​{rango_menor} HASTA 💲​{rango_mayor}: ")
            op.imprimir_lista(filtro_rango)

            self.mostrar_menu()
        elif opcion == "6":
            producto_seleccionado = input("ingrese el nombre del producto:  ")
            reco = op.recomendaciones(pro.productos,producto_seleccionado.lower())
            print("💡​ recomendaciones:  ")
            op.imprimir_lista(reco)
          
            self.mostrar_menu()

        elif opcion == "7":
            print("\n🔎 Resultados encontrados:")
            pro.mostrar_productos()

            self.mostrar_menu()

        elif opcion == "x":
            print("👋 Gracias por visitar Colombia Souvenirs")
            return
          
        else:
            print("❌ Opción inválida, intente de nuevo.")
            self.mostrar_menu() 





pro = GestorProductos()
pro.precargar_productos_desde_txt("productos.txt")
op = Operaciones()
menu =Menu ()
menu.mostrar_menu()







