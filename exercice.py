import tkinter

win = tkinter.Tk()
win.geometry("500x100")
win.title("Ma Fenetre")
win.config(bg="purple")

def background():
    if var.get() == 1:
        win.config(bg="red")
        L1.config(bg="red")
        radio1.config(bg="red")
        radio2.config(bg="red")
        radio3.config(bg="red")
        check1.config(bg="red")
    elif var.get() == 2:
        win.config(bg="green")
        L1.config(bg="green")
        radio1.config(bg="green")
        radio2.config(bg="green")
        radio3.config(bg="green")
        check1.config(bg="green")
    elif var.get() == 3:
        win.config(bg="blue")
        L1.config(bg="blue")
        radio1.config(bg="blue")
        radio2.config(bg="blue")
        radio3.config(bg="blue")
        check1.config(bg="blue")

L1 = tkinter.Label(win, text="Couleurs", bg="purple")
var = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="Rouge", variable=var, value=1, bg="purple", command=background)
radio2 = tkinter.Radiobutton(win, text="Vert", variable=var, value=2, bg="purple", command=background)
radio3 = tkinter.Radiobutton(win, text="Bleu", variable=var, value=3, bg="purple", command=background)
def Afficher():
    if var1.get() == 1:
        win.geometry("500x200")
        background()
        L1.place(x=30, y=80)
        radio1.place(x=30, y=120)
        radio2.place(x=120, y=120)
        radio3.place(x=200, y=120)
    else :
        win.geometry("500x100")
        win.config(bg="purple")
        check1.config(bg="purple")
        L1.place_forget()
        L1.config(bg="purple")
        var.set(0)
        radio1.place_forget()
        radio1.config(bg="purple")
        radio2.place_forget()
        radio2.config(bg="purple")
        radio3.place_forget()
        radio3.config(bg="purple")

var1 = tkinter.IntVar()
check1 = tkinter.Checkbutton(win, text="Afficher les couleur", variable=var1, bg="purple", command=Afficher)
check1.place(x=30, y=30)

def reset():
    check1.deselect()
    win.geometry("500x100")
    win.config(bg="purple")
    check1.config(bg="purple")
    Afficher()
    win.destroy()

but1 = tkinter.Button(win, text="Quitter", command=reset)
but1.place(x=230, y=30)

win.mainloop()

"""
import tkinter

win = tkinter.Tk()
win.geometry("500x100")
win.title("Ma Fenetre")
win.config(bg="purple")

def Afficher():
    def color():
        if var.get() == 1 :
            win.config(bg="red")
            L1.config(bg="red")
            radio1.config(bg="red")
            radio2.config(bg="red")
            radio3.config(bg="red")
            check1.config(bg="red")
        if var.get() == 2 :
            win.config(bg="green")
            L1.config(bg="green")
            radio1.config(bg="green")
            radio2.config(bg="green")
            radio3.config(bg="green")
            check1.config(bg="green")
        if var.get() == 3 :
            win.config(bg="blue")
            L1.config(bg="blue")
            radio1.config(bg="blue")
            radio2.config(bg="blue")
            radio3.config(bg="blue")
            check1.config(bg="blue")
    L1 = tkinter.Label(win , text="Couleurs" , bg="purple")
    var = tkinter.IntVar()
    radio1 = tkinter.Radiobutton(win , text="Rouge" ,variable=var , value=1 , bg="purple", command=color)
    radio2 = tkinter.Radiobutton(win , text="Vert" ,variable=var , value=2 , bg="purple", command=color)
    radio3 = tkinter.Radiobutton(win , text="Bleu" ,variable=var , value=3 , bg="purple", command=color)
    if var1.get() == 1 :
        win.geometry("500x200")
        L1.place(x=30,y=80)
        radio1.place(x=30,y=120)
        radio2.place(x=120,y=120)
        radio3.place(x=200,y=120)
    else:
        L1.destroy()
        radio1.destroy()
        radio2.destroy()
        radio3.destroy()
var1 = tkinter.IntVar()
check1 = tkinter.Checkbutton(win , text="Afficher les couleur" , variable=var1 , bg="purple" , command=Afficher)
check1.place(x=30,y=30)

def reset():
    check1.deselect()
    win.geometry("500x100")
    win.config(bg="purple")
    check1.config(bg="purple")

but1 = tkinter.Button(win , text="Quitter" , command=reset)
but1.place(x=230,y=30)

win.mainloop()
"""
