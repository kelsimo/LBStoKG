from tkinter import *

win = Tk()
win.geometry("450x300")
win.config(bg="lightgrey")
win.resizable(0,0)
win.title("LBS to KG Converter")

#entry
weightvar = StringVar()

label = Label(win, text = "Enter your weight in lbs:", bg="lightgrey",  font='Century 16')
label.place(x=40, y=70)
weight = Entry(win, textvariable = weightvar, width=6, font='Century 16 bold', bg="darkgrey", fg="white", justify="center").place(x=300, y=70)

#output
label2 = Label(win, text = "", bg="lightgrey", font='Century 16')
label2.place(x=100, y=200)

def converter():
    lbstokg = int(weightvar.get()) * 0.453592
    label2.config(text=f'{"your weight is " + str(lbstokg) + " KG"}')

button1 = Button(win, text = "Convert to KG", bg="red", fg="white", font='Century 16', command=converter).place(x=150, y=120)

win.mainloop()
