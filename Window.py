from tkinter import *


class Ventanas:


    def Ventana(self):

        self.ventana = Tk()
        self.ventana.geometry('1000x600+350+100')
        self.ventana.configure(background='gray64')
        self.ventana.title('PROYECTO 2')
        self.ventana.resizable(False,False)

        Frane1 = Frame(self.ventana,width=950, height=530, relief='sunken',bd=5,background='gray80').place(x=20,y=50)

        self.Text_Area()
        self.Botones()

        self.ventana.mainloop()


    def Text_Area(self):

        self.area = Text(self.ventana, width=100, height=31)
        self.area.place(x=30,y=60)

    def Botones(self):

        boton1 = Button(self.ventana, text='Nuevo',height=1,width=10,background='gray64').place(x=20,y=10)
        boton2 = Button(self.ventana, text='Abrir',height=1,width=10,background='gray64').place(x=100,y=10)
        boton3 = Button(self.ventana, text='Guardar',height=1,width=10,background='gray64').place(x=180,y=10)
        boton4 = Button(self.ventana, text='Guardar Como',height=1,width=15,background='gray64').place(x=260,y=10)
        boton5 = Button(self.ventana, text='Salir',height=1,width=10,background='gray64', command=self.ventana.destroy).place(x=365,y=10)

        boton6 = Button(self.ventana, text='Generar WEB',height=1,width=15,background='gray64').place(x=840,y=60)
        boton7 = Button(self.ventana, text='Tokens',height=1,width=15,background='gray64').place(x=840,y=90)
        boton8 = Button(self.ventana, text='Errores',height=1,width=15,background='gray64').place(x=840,y=120)