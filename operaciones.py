
class Operaciones():

    def busqueda_binaria_por_nombre(self, productos,objetivo, inicio = 0, fin= None ):
        if fin is None:
            fin = len(productos)-1

        if inicio > fin:
            return  []
            
        medio = (inicio + fin) // 2
        nombre_medio = productos[medio].nombre.lower()
        objetivo = objetivo.lower()

        if nombre_medio.startswith(objetivo):
            coincidencias = [productos[medio]]

            coincidencia_izquierda = self.busqueda_binaria_por_nombre(productos,objetivo, inicio, medio -1)

            coincidencia_derecha = self.busqueda_binaria_por_nombre(productos,objetivo, medio + 1, fin)


            return coincidencias + coincidencia_izquierda + coincidencia_derecha


        elif objetivo.lower() < nombre_medio:
            return self.busqueda_binaria_por_nombre(productos,objetivo, inicio, medio -1)
            
        else:
            return self.busqueda_binaria_por_nombre(productos,objetivo, medio + 1, fin)
        
    def calculo_total_de_precios(self, productos, index = 0, total_productos =0):
        if productos is None:
            return
        if index == len(productos):
            return total_productos
        
        producto_atual = productos[index].precio
        total_productos = producto_atual + total_productos
        return self.calculo_total_de_precios(productos,index +1, total_productos)
    
    def calculo_promedio_por_categoria(self, productos,categoria,  index = 0, cont = 0, suma_productos = 0):
        if productos is None or len(productos) == 0:
            return 0
        
        if index == len(productos):
            return (suma_productos//cont)
        
        if productos[index].categoria.lower() == categoria.lower():
            cont = +1
            suma_productos = productos[index].precio + suma_productos
        
        return self.calculo_promedio_por_categoria(productos,categoria, index +1, cont, suma_productos)
    

    def busqueda_por_rango_de_precios(self, productos,minimo, maximo , index=0, resultado = None):
        if resultado is None:
            resultado = []
        
        if index == len(productos):
            return resultado

        if minimo <=  productos[index].precio <= maximo:
            resultado.append(productos[index])
        
        return self.busqueda_por_rango_de_precios( productos, minimo,maximo, index +1, resultado)
    

    def recomendaciones(self, productos,nombre_producto,index = 0,   producto_seleccionado = None, recomendaciones = None):
        if recomendaciones is None:
            recomendaciones = []

        if producto_seleccionado is None:
            coincidencias = self.busqueda_binaria_por_nombre(productos, nombre_producto)
            if not coincidencias:
                return []
            producto_seleccionado = coincidencias[0]

        if index == len(productos):
            return recomendaciones
        
        
        
        if productos[index].categoria.lower() == producto_seleccionado.categoria.lower():
            recomendaciones.append(productos[index])

        return self.recomendaciones(productos,nombre_producto,index +1,  producto_seleccionado, recomendaciones)

        
        
        


        
         
        

            




