from ipcal import *
from tkinter import *
from subnetter import *
string = ""

root = Tk()
root.title("Menu")
try:
    root.iconbitmap("C:/Users/yerva/Desktop/tello.ico")
except:
    pass

positionRight = int(root.winfo_screenwidth()/2 - 500/2)
positionDown = int(root.winfo_screenheight()/2 - 300/2)

root.geometry("500x300+{}+{}".format(positionRight, positionDown))


def ip():
    root.destroy()
    main1 = Tk()
    main1.title("IP Calculator")
    #main1.iconbitmap("C:/Users/yerva/Desktop/tello.ico")
    windowwidth = main1.winfo_reqwidth()
    windowheight = main1.winfo_reqheight()
    positionright = int(main1.winfo_screenwidth()/2 - windowwidth/1.5)
    positiondown = int(main1.winfo_screenheight()/2 - windowheight/1.2)
    main1.geometry("+{}+{}".format(positionright, positiondown))
    
    e = Entry(main1, width=40, justify="center")
    e.configure(state="disabled")

    def click(x):
        global string
        if x == "/":
            string += str(x)
            e.configure(state="normal")
            e.insert(END, x)
            e.configure(state="disabled")
        elif x == ".":
            string += str(x)
            e.configure(state="normal")
            e.insert(END, x)
            e.configure(state="disabled")
        elif x == "c":
            xx = Label(main1, text=ipcal(string))
            xx.grid(row=8, column=0, columnspan=4)
        elif x == "d":
            e.configure(state="normal")
            e.delete(len(e.get())-1, END)
            string = string[:-1]
            e.configure(state="disabled")
        else:
            string += str(x)
            e.configure(state="normal")
            e.insert(END, str(x))
            e.configure(state="disabled")
        return None

    button_1 = Button(main1, text="1", padx="45", pady="20", command=lambda: click(1))
    button_2 = Button(main1, text="2", padx="45", pady="20", command=lambda: click(2))
    button_3 = Button(main1, text="3", padx="45", pady="20", command=lambda: click(3))

    button_4 = Button(main1, text="4", padx="45", pady="20", command=lambda: click(4))
    button_5 = Button(main1, text="5", padx="45", pady="20", command=lambda: click(5))
    button_6 = Button(main1, text="6", padx="45", pady="20", command=lambda: click(6))

    button_7 = Button(main1, text="7", padx="45", pady="20", command=lambda: click(7))
    button_8 = Button(main1, text="8", padx="45", pady="20", command=lambda: click(8))
    button_9 = Button(main1, text="9", padx="45", pady="20", command=lambda: click(9))

    button_0 = Button(main1, text="0", padx="45", pady="20", command=lambda: click(0))
    button_sign = Button(main1, text="/", padx="45.59", pady="20", command=lambda: click("/"))
    button_period = Button(main1, text=". ", padx="45", pady="20", command=lambda: click("."))
    button_calculate = Button(main1, text="Calculate", padx="80", pady="20", command=lambda: click("c"))
    button_remove = Button(main1, text="←", padx="45", pady="20", command=lambda: click("d"))
    
    e.grid(row=1, column=1, columnspan=3)
    button_1.grid(row=4, column=1)
    button_2.grid(row=4, column=2)
    button_3.grid(row=4, column=3)
    
    button_4.grid(row=3, column=1)
    button_5.grid(row=3, column=2)
    button_6.grid(row=3, column=3)
    
    button_7.grid(row=2, column=1)
    button_8.grid(row=2, column=2)
    button_9.grid(row=2, column=3)
    
    button_0.grid(row=5, column=1)
    button_period.grid(row=5, column=2)
    button_sign.grid(row=5, column=3)


    button_calculate.grid(row=6, column=1, columnspan=2)
    button_remove.grid(row=6, column=3)
    
    main1.mainloop()


def subnet():
    root.destroy()
    main2 = Tk()
    main2.title("IP Calculator")

    windowwidth = main2.winfo_reqwidth()
    windowheight = main2.winfo_reqheight()
    positionright = int(main2.winfo_screenwidth() / 2 - windowwidth / 1.5)
    positiondown = int(main2.winfo_screenheight() / 2 - windowheight / 1.2)
    main2.geometry("+{}+{}".format(positionright, positiondown))

    e = Entry(main2, width=40, justify="center")
    e.configure(state="disabled")

    def click(x):
        global string
        if x == "/":
            string += str(x)
            e.configure(state="normal")
            e.insert(END, x)
            e.configure(state="disabled")
        elif x == ".":
            string += str(x)
            e.configure(state="normal")
            e.insert(END, x)
            e.configure(state="disabled")
        elif x == "c":
            xx = Label(main2, text=subnett(string))
            xx.grid(row=8, column=0, columnspan=4)
        elif x == "d":
            e.configure(state="normal")
            e.delete(len(e.get()) - 1, END)
            string = string[:-1]
            e.configure(state="disabled")
        else:
            string += str(x)
            e.configure(state="normal")
            e.insert(END, str(x))
            e.configure(state="disabled")
        return None

    button_1 = Button(main2, text="1", padx="45", pady="20", command=lambda: click(1))
    button_2 = Button(main2, text="2", padx="45", pady="20", command=lambda: click(2))
    button_3 = Button(main2, text="3", padx="45", pady="20", command=lambda: click(3))
    button_4 = Button(main2, text="4", padx="45", pady="20", command=lambda: click(4))
    button_5 = Button(main2, text="5", padx="45", pady="20", command=lambda: click(5))
    button_6 = Button(main2, text="6", padx="45", pady="20", command=lambda: click(6))
    button_7 = Button(main2, text="7", padx="45", pady="20", command=lambda: click(7))
    button_8 = Button(main2, text="8", padx="45", pady="20", command=lambda: click(8))
    button_9 = Button(main2, text="9", padx="45", pady="20", command=lambda: click(9))
    button_0 = Button(main2, text="0", padx="45", pady="20", command=lambda: click(0))
    button_sign = Button(main2, text="/", padx="45", pady="20", command=lambda: click("/"))
    button_period = Button(main2, text=".", padx="45", pady="20", command=lambda: click("."))
    button_calculate = Button(main2, text="Calculate", padx="80", pady="20", command=lambda: click("c"))
    button_remove = Button(main2, text="←", padx="40", pady="20", command=lambda: click("d"))

    e.grid(row=1, column=1, columnspan=4)
    button_1.grid(row=4, column=1)
    button_2.grid(row=4, column=2)
    button_3.grid(row=4, column=3)

    button_4.grid(row=3, column=1)
    button_5.grid(row=3, column=2)
    button_6.grid(row=3, column=3)

    button_7.grid(row=2, column=1)
    button_8.grid(row=2, column=2)
    button_9.grid(row=2, column=3)

    button_0.grid(row=5, column=1)
    button_sign.grid(row=5, column=2)
    button_period.grid(row=5, column=3)
    button_calculate.grid(row=6, column=1, columnspan=2)
    button_remove.grid(row=6, column=3)

    main2.mainloop()


button1 = Button(root, text="ip", command=ip, padx="83", pady="10")
button1.place(relx=0.5, rely=0.3, anchor=CENTER)
button2 = Button(root, text="subnet", command=subnet, padx="70", pady="10")
button2.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
