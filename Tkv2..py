import tkinter


def sumar():
    print("Hola")
    valor = TBox.get()
    print(valor)
    texto = "La edad del empleado es " + str(valor) + " años."
    L1.configure(text=texto)


x = 650
y = 400
tk = tkinter.Tk("Nueva ventana")
tk.geometry(f"{x}x{y}+200+200")
Titulo = tkinter.Label(tk, text="Introducción Python")
Titulo.pack()

TBox = tkinter.Scale(tk, label=":Años", from_=18, to_=63)
TBox.pack()
B = tkinter.Button(tk, text="Oprima para saludar", command=sumar)
B.pack()
L1 = tkinter.Label(tk, text="Bienvenidos")
L1.pack()
d = tkinter.Spinbox(tk, from_=10, to=30)
d.pack()

tk.mainloop()
