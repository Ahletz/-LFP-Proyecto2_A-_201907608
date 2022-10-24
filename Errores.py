class Error:


    lista = []

    def Lista(self):

         self.lista = [] # lista de errores

    def Crear(self, contenido, linea, columna):

        Lista = [contenido,linea,columna]

        self.lista.append(Lista) #agregar error a la lista

    def Mostrar_error(self):

        for i in self.lista:

            print(i)

    def Reporte_Errores(self):

        #inicio de thml
         
        inicio = '<!doctype html><html lang="en"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="Css errores table.css" rel="stylesheet" ><title>TOKENS</title></head><body><table><thead><tr>'

        #final html

        final = '</table></body></html>'
        #contenido de html

        contenido = '<tr>' + '<th>' + 'Error' + '</th>' + '<th>' + 'LINEA' + '</th>' + '<th>' + 'COLUMNA' + '</th>' +'</tr>'+'</thead>'

        for i in self.lista: #agregar a la tabla los respectivos tokens 

            tokenn = '<tr>' + '<td>' +str(i[0]) + '</td>' + '<td>' +str(i[1]) + '</td>' + '<td>' +str(i[2]) + '</td>' +'</tr>'

            contenido += tokenn

        texto = inicio + contenido + final

        op = open('REPORTE ERRORES.html','w')

        op.write(texto)

        op.close()
        self.Css_reporte()

    def Css_reporte(self):

        cuerpo = 'body{background-color: #632432;font-family: Arial;}#main-container{margin: 150px auto;width: 600px;}table{background-color: white;text-align: left;border-collapse: collapse;width: 100%;}th, td{padding: 20px;}thead{background-color: #246355;border-bottom: solid 5px #0F362D;color: white;}tr:nth-child(odd){background-color: #ddd;}tr:hover td{background-color: #369681;color: white;}'

        op = open('Css errores table.css', 'w')

        op.write(cuerpo)
        op.close()
