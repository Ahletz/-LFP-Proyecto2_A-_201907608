
class Analisis:


    def Comienzo(self, direccion):

        ruta = direccion #direccion del archivo
        archivo = open(ruta, encoding='utf-8') #abrir el archivo
        texto = archivo.read() #leer y obtener el contenido del archivo

        linea = 1 #linea del archivo
        columna = 0 #columna del archivo 
        palabra = '' #contenido 
        estado = 0 # estado inicial 


        for i in texto:

            columna +=1 #aumnetar la columna
            
            if i == '\n': #si encuentra un salto de linea
                
                linea+=1 #aumentar linea
                columna = 0 #regresar columna a 0

            if estado == 0:

                pass


