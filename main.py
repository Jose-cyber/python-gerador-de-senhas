from os import get_blocking
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import string
import random



# colors -----------
cor0 =  "#444466" # black
cor1 =  "#feffff" # white 
cor2 =  "#f05a43" # red 


screen = Tk()
screen.title('Gerenciador de senhas')
screen.geometry('400x355')
screen.configure(bg=cor1)


# -------- style 
style = ttk.Style(screen)
style.theme_use('clam')
# ---------------------

# ------------- frame top
frame_top = Frame(screen, width=300, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_top.grid(row=0, column=0, sticky=NSEW)

frame_down = Frame(screen, width=300, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_down.grid(row=1, column=0, sticky=NSEW)
# --------------------------------------------

# image 
img = Image.open("/var/www/python-gerador-de senhas/_img/cadeado1.png")
img = img.resize((30,30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_top, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)
# ----------------------

# title
app_title = Label(frame_top, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor1, fg=cor0)
app_title.place(x=35, y=2)

app_linha = Label(frame_top, text='', width=400, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor2, fg=cor0)
app_linha.place(x=0, y=45)
# ------------------------


# frame down
app_senha = Label(frame_down, text='- - - - - - - -', width=26, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_down, text='Numero total de caracteres na senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=3, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_down, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=3, pady=8)

def create_pass():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numbers = "0123456789"
    symbol = "!@#$%¨&*()_=+=[]{/}|~^"

    global combinar
        
    if state_0.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass

    if state_1.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

    if state_2.get() == numbers:
        combinar = combinar + numbers
    else:
        pass

    if state_3.get() == symbol:
        combinar = combinar + symbol
    else:
        pass

    get_spin = int(spin.get())

    password = "".join(random.sample(combinar, get_spin))

    app_senha['text'] = password

    def copy_pass():
        info = password
        frame_down.clipboard_clear()
        frame_down.clipboard_append(info)
        messagebox.showinfo("sucesso!", "a senha foi copiada com sucesso")
    
    button_copy = Button(frame_down, command=copy_pass, text='Copiar', width=7, height=2,relief='raised', overrelief='solid',anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)
    button_copy.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)



# get dados
frame_caracteres = Frame(frame_down, width=300, height=210, bg=cor1, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW)


alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numbers = "0123456789"
symbol = "!@#$%¨&*()_=+=[]{/}|~^"


# uppercase
state_0 = StringVar()
state_0.set(False)
check_0 = Checkbutton(frame_caracteres, width=1, var=state_0, onvalue=alfa_maior, offvalue='off', relief='flat', bg=cor1)
check_0.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras maiusculas(ABC..)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)
# ---------------------------------------------------------

# Lowercase
state_1 = StringVar()
state_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=state_1, onvalue=alfa_menor, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras minusculas(abc..)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)
# --------------------------------------------------------



# numbers
state_2 = StringVar()
state_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=state_2, onvalue=numbers, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Numeros (0123....)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)
# --------------------------------------------------------

# symbol 
state_3 = StringVar()
state_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=state_3, onvalue=symbol, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Simbolos (!@$#...)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)
# --------------------------------------------------------



# button 
button_generate_pass = Button(frame_caracteres, command=create_pass, text='GERAR SENHA', width=29, height=1,relief='flat', overrelief='solid',anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)
button_generate_pass.grid(row=5, column=0, sticky=NSEW, padx=5, pady=10, columnspan=5)




screen.mainloop()

