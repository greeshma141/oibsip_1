from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
root = Tk()
root.title("BMI Calculator")
un= Label(root, text="Enter user-id:")
un.grid(row=0, column=0)
u = Entry(root, width=42, borderwidth=5, bg="lightyellow")
u.grid(row=0, column=1, columnspan=3)
height = Label(root, text="Enter Height (cm):")
height.grid(row=1, column=0)
e1 = Entry(root, width=42, borderwidth=5, bg="lightyellow")
e1.grid(row=1, column=1, columnspan=3)
weight = Label(root, text="Enter Weight (kg):")
weight.grid(row=2, column=0)
e2 = Entry(root, width=42, borderwidth=5, bg="lightyellow")
e2.grid(row=2, column=1, columnspan=3)
current_entry = StringVar(value="un")
def set_current_entry(entry):
    current_entry.set(entry)
u.bind("<FocusIn>", lambda event: set_current_entry("un"))
e1.bind("<FocusIn>", lambda event: set_current_entry("height"))
e2.bind("<FocusIn>", lambda event: set_current_entry("weight"))
def click(number):
    if current_entry.get() == "un":
        c3 = u.get()
        u.delete(0, END)
        u.insert(0, str(c3) + str(number))
    elif current_entry.get() == "weight":
        c2 = e2.get()
        e2.delete(0, END)
        e2.insert(0, str(c2) + str(number))
    else:
        c1 = e1.get()
        e1.delete(0, END)
        e1.insert(0, str(c1) + str(number))

def clear():
    if current_entry.get() == "height":
        e1.delete(0,END)
    else:
        e2.delete(0,END)
def save(username,height,weight,res):
    filename=f"{username}bmi.txt"
    with open(filename,"a")as file:
        file.write(f"Height:{height}\nWeight:{weight}\nBMI:{res}")
def bmi():
    try:
        h=float(int(e1.get())/100)
        w=float(e2.get())
        r=w/(h**2)
        if r<18.5:
            e3.insert(0,r)
            cw=Label(root,text="UNDER WEIGHT",fg="blue")
            cw.grid(row=9,column=1)
        elif r>=18.5 and r<=24.9:
            e3.insert(0,r)
            cw=Label(root,text="NORMAL WEIGHT",fg="blue")
            cw.grid(row=9,column=1)
        elif r>=25.0 and r<=29.9:
            e3.insert(0,r)
            cw=Label(root,text="OVER WEIGHT",fg="blue")
            cw.grid(row=9,column=1)
        elif r>=30.0:
            e3.insert(0,r)
            cw=Label(root,text="OBESITY",fg="blue")
            cw.grid(row=9,column=1)
    except ValueError:
        print("Enter Correct value!!")
    xpoints = np.array([25,45,70,80,90])
    ypoints = np.array([175,145,155,150,145])
    for i in range(len(xpoints)):
        s=xpoints[i]/(ypoints[i]**2)
        plt.plot(xpoints,ypoints,marker="o")
    plt.text(35,160,"UnderWeight")
    plt.text(50,153,"NormalWeight")
    plt.text(77,153,"OverWeight")
    plt.text(77,147,"Obesity")
    plt.title("Graph by which BMI is categorized")
    plt.xlabel("weight")
    plt.ylabel("height")
    plt.show()
button_1 = Button(root, text="1", padx=60, pady=20, borderwidth=6,bg="light blue",command=lambda: click(1))
button_2 = Button(root, text="2", padx=60, pady=20, borderwidth=6,bg="light blue",command=lambda: click(2))
button_3 = Button(root, text="3", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(3))
button_4 = Button(root, text="4", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(4))
button_5 = Button(root, text="5", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(5))
button_6 = Button(root, text="6", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(6))
button_7 = Button(root, text="7", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(7))
button_8 = Button(root, text="8", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(8))
button_9 = Button(root, text="9", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(9))
button_0 = Button(root, text="0", padx=60, pady=20, borderwidth=6,bg="light blue", command=lambda: click(0))
button_bmi=Button(root,text="BMI",padx=55,pady=20, borderwidth=6,bg="light blue",command=bmi)
button_clear=Button(root,text="clr",padx=55, pady=20, borderwidth=6,bg="light blue",command=clear)
button_save=Button(root,text="save",padx=53, pady=20, borderwidth=6,bg="light blue",command=lambda: save(u.get(), e1.get(), e2.get(), e3.get()))
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_0.grid(row=6, column=0)
button_bmi.grid(row=6, column=1)
button_clear.grid(row=6, column=2)
button_save.grid(row=7,column=0)
result_label=Label(root,text="Result:",padx=20)
result_label.grid(row=8,column=0)
e3=Entry(root,width=42, borderwidth=5, bg="lightyellow")
e3.grid(row=8,column=1,columnspan=2)
root.mainloop()
