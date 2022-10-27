
from Tokens import *
from Errores import *

class Analisis:


    def Comienzo(self, direccion):

        ruta = direccion #direccion del archivo
        archivo = open(ruta, encoding='utf-8') #abrir el archivo
        texto = archivo.read() #leer y obtener el contenido del archivo

        linea = 1 #linea del archivo
        columna = 0 #columna del archivo 
        palabra = '' #contenido 
        estado = 0 # estado inicial 

        token = Token()
        error = Error()

        Lista = [] #lista principal

        Contenidos = [] #lista con contenidos 


        for i in texto:

            columna +=1 #aumnetar la columna
            
            if i == '\n': #si encuentra un salto de linea
                
                linea+=1 #aumentar linea
                columna = 0 #regresar columna a 0

            if estado == 0:

                pass
        
            if estado == 0:

                if i == '<':

                    Tipo = 'MENOR QUE' #Token 

                    token.Contruccion(Tipo,i,linea,columna) # contruccion del token

                elif i == '!':

                    Tipo = 'EXCLAMACION' #Token 

                    token.Contruccion(Tipo,i,linea,columna)

                elif i == '-':

                    Tipo = 'GUION' #Token 

                    token.Contruccion(Tipo,i,linea,columna)

                    estado = 1 #cambio de estado 


                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 1:

                if i == '-':

                    Tipo = 'GUION' #Token 

                    token.Contruccion(Tipo,i,linea,columna) #contruccion de token

                    estado = 2 #cambio de estado 

                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 2:

                if i.isalnum(): 

                    palabra += i #almacenar todos los caracterers dentro de la palabra


                if palabra.upper() == 'CONTROLES':


                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)


                    palabra = '' #Limpiar la palabra
                    estado = 3 #cambio de estado 


            elif estado == 3:


                if i.isalpha():

                    palabra += i #alamcenar contenido dentro del lector 

                elif i == ' ':
                    
                    if palabra == '': #cambio de estado y comprobacion si la palabra pertenece al lenguaje
                        continue
                    else: 
                        error.Crear(palabra,linea,columna) #lista de errores

                    estado = 4 #cambio de estado 

                elif i == '\n' or i == '\t':

                    continue #si vienen espacio 


                if palabra.upper() == 'ETIQUETA': 

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra
                
                elif palabra.upper() == 'BOTON':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'CHECK':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'RADIOBOTON':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'TEXTO':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra
                    
                elif palabra.upper() == 'AREATEXTO':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'CLAVE':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'CONTENEDOR':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 

                    palabra = '' #Limpiar la palabra

                elif palabra.upper() == 'CONTROLES':


                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)


                    palabra = '' #Limpiar la palabra
                    estado = 5 #cambio de estado 


            elif estado == 4:

                if i.isalpha() or i.isalnum():

                    palabra += i

                elif i == ';':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Contenidos.append(palabra) #agregar la palabra a la lista 
                    Lista.append(Contenidos)

                    Contenidos = [] #crear nueva instancia para otro contenido 

                    palabra = '' #Limpiar la palabra

                    Tipo = 'PUNTO Y COMA'

                    token.Contruccion(Tipo,i,linea,columna)

                    estado = 3
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            
            elif estado == 5:

                if i == '-':

                    Tipo = 'GUION' #Token 

                    token.Contruccion(Tipo,i,linea,columna) #contruccion de token

                    estado = 2 #cambio de estado 

                elif i == '>':

                    Tipo = 'MAYOR QUE' #Token 

                    token.Contruccion(Tipo,i,linea,columna) #contruccion de token

                    estado = 2 #cambio de estado 



                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores



        for j in Lista:

            print(j)

                    



                





                    



                







