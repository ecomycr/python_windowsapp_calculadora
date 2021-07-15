# Calculadora en Python con Tkinter con efecto hover
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Button, Tk, Frame,Entry,END


app = Tk()
app.geometry('300x350')
app.config(bg= "white")
app.iconbitmap(bitmap='icono.ico')
app.resizable(0,0)
app.title('Calculadora')

#hover

class click_cambio_color(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.click_sobre)
		self.bind("<Leave>", self.click_default)

	def click_sobre(self, e):
		self["background"] = self["activebackground"]

	def click_default(self, e):
		self["background"] = self.defaultBackground



i=0
def misnumeros(dato):
	global i
	i+=1
	Resultado.insert(i, dato)


def ejecutar_operacion():
	global i

	ecuacion = Resultado.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))

			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result) -4
			i = longitud

		except Exception as e:
			result = 'ERROR' + str(e)
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass


def borrar_numero():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1



def borrar_operacion():
	Resultado.delete(0, END)	
	i=0



frame = Frame(app, bg ='black', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)

Resultado = Entry(frame,bg='#9EF8E8', width=18, relief='groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

#fila 1

uno = click_cambio_color(frame, text= "1", borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="aqua", bg ='#999AB8',  anchor="center", command=lambda: misnumeros(1))  
uno.grid( column= 0 ,row=1, pady=1,padx=3)

dos = click_cambio_color(frame, text= "2", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8', anchor="center",command=lambda: misnumeros(2))  
dos.grid(column =1 , row=1, pady=1,padx=1)

tres = click_cambio_color(frame, text= "3", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua", bg ='#999AB8', anchor="center",command=lambda: misnumeros(3))  
tres.grid(column =2, row=1, pady=1,padx=1)

borrar_todo = click_cambio_color(frame, text= "⌫", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="red", bg='#999AB8',  anchor="center",command=lambda: borrar_numero())  
borrar_todo.grid(column =3, row=1, pady=2,padx=2)


#fila 2

cuatro = click_cambio_color(frame, text= "4",height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua", bg ='#999AB8', anchor="center",command=lambda: misnumeros(4))  
cuatro.grid( column= 0 ,row=2, pady=1,padx=1)

cinco = click_cambio_color(frame, text= "5", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8', anchor="center",command=lambda: misnumeros(5))  
cinco.grid(column =1 , row=2, pady=1,padx=1)

seis = click_cambio_color(frame, text= "6", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8',  anchor="center",command=lambda: misnumeros(6))  
seis.grid(column =2, row=2, pady=1,padx=1)

mas_boton = click_cambio_color(frame, text= "+", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#3a9e8c',  anchor="center",command=lambda: misnumeros('+'))  
mas_boton.grid(column =3, row=2, pady=2,padx=2)



#fila 3


siete = click_cambio_color(frame, text= "7",height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8',  anchor="center",command=lambda: misnumeros(7))  
siete.grid( column= 0 ,row=3, pady=1,padx=1)

ocho = click_cambio_color(frame, text= "8", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8', anchor="center",command=lambda: misnumeros(8))  
ocho.grid(column =1 , row=3, pady=1,padx=1)

nueve = click_cambio_color(frame, text= "9", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8',  anchor="center",command=lambda: misnumeros(9))  
nueve.grid(column =2, row=3, pady=1,padx=1)

menos_boton = click_cambio_color(frame, text= "-", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#3a9e8c',  anchor="center",command=lambda: misnumeros('-'))  
menos_boton.grid(column =3, row=3, pady=2,padx=2)

#fila 4

cero = click_cambio_color(frame, text= "0",height=5, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8',  anchor="center",command=lambda: misnumeros(0))  
cero.grid( column= 0, rowspan=2, row=4, pady=1,padx=1)

punto_boton = click_cambio_color(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02",bg ='#3a9e8c', anchor="center",command=lambda: misnumeros('.'))  
punto_boton.grid(column =1 , row=4, pady=1,padx=1)

dividir = click_cambio_color(frame, text= "÷", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02",bg ='#3a9e8c',  anchor="center",command=lambda: misnumeros('/'))  
dividir.grid(column =2, row=4, pady=1,padx=1)

multiplicar = click_cambio_color(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#3a9e8c',  anchor="center",command=lambda: misnumeros('*'))  
multiplicar.grid(column =3, row=4, pady=2,padx=2)


#fila 4

igual = click_cambio_color(frame, text= "=", height=2, width=12,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#3a9e8c', anchor="center",command=lambda: ejecutar_operacion())  
igual.grid(column =1 ,columnspan=2, row=5, pady=1,padx=1)


borrar_todo = click_cambio_color(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", activebackground="#FEEF02", bg='#3a9e8c', anchor="center",command=lambda: borrar_operacion())  
borrar_todo.grid(column =3, row=5, pady=2,padx=2)

app.mainloop()