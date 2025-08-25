
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
            return 0 
        if index == len(productos):
            return total_productos
        
        producto_actual = productos[index].precio
        total_productos = producto_actual + total_productos
        return self.calculo_total_de_precios(productos,index +1, total_productos)
    
    def calculo_promedio_por_categoria(self, productos,categoria,  index = 0, cont = 0, suma_productos = 0):
        if productos is None or len(productos) == 0:
            return 0
        
        if index == len(productos):
            return (suma_productos//cont) if cont > 0 else 0
        
        if productos[index].categoria.lower() == categoria.lower():
            cont = cont + 1
            suma_productos = productos[index].precio + suma_productos
        
        return self.calculo_promedio_por_categoria(productos,categoria, index +1, cont, suma_productos)
    


    def Quicksort_precio(self, productos, organizacion, index =1 , ele_izq = None, ele_der = None):
        if ele_izq  is None:
           ele_izq = []

        if ele_der is None:
            ele_der = []

        if productos is None or  len(productos) <= 1:
           return productos
        
        inicio = productos[0]

        if index == len (productos):
            izq_ordenado = self.Quicksort_precio(ele_izq, organizacion)
            der_ordenado = self.Quicksort_precio(ele_der, organizacion)

            if organizacion.lower() == "mayor":
                return der_ordenado + [inicio]+ izq_ordenado
           
            elif organizacion.lower() == "menor":
                return izq_ordenado + [inicio] + der_ordenado

            else:
                return "tipo de organizacion no valida"
        

        if productos[index].precio < inicio.precio:
            ele_izq.append(productos[index])
        else:
            ele_der.append(productos[index])
        
        return self.Quicksort_precio(productos, organizacion, index +1, ele_izq, ele_der)

         

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
    
 
        
        
        


        
         
        

            




