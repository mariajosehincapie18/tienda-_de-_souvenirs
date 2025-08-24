
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
            




