import tkinter

win2 = tkinter.Tk()
win2.title("Radio check")
win2.geometry("500x500")
win2.config(bg="blue")

def fct():
    res = ""
    if var.get() == 1 :     #avec StringVar on peut ecrire var.get() == "Python "
        res += "Python "
    if var.get() == 2 :
        res += "Java "
    if var.get() == 3 :
        res += "PHP "
    print("vous avez selectionne :"+" "+res)
var = tkinter.IntVar()  #var = tkinter.StringVar()
radio1 =tkinter.Radiobutton(win2 ,text="Python ", variable=var , value=1 , bg="blue")   #value = "Python "
radio1.place(x=250,y=20)
radio2 =tkinter.Radiobutton(win2 ,text="Java ", variable=var , value=2 , bg="blue")
radio2.place(x=250,y=80)
radio3 =tkinter.Radiobutton(win2 ,text="PHP ", variable=var , value=3 , bg="blue")
radio3.place(x=250,y=140)
but1 = tkinter.Button(text="Valider" ,command=fct)
but1.place(x=350,y=180)


win2.mainloop()
