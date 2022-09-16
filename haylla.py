from tkinter import *




def appsub(info,root):
    root2=Tk()
    root2.title("Subnet IP list")
    windowwidth = root2.winfo_reqwidth() +200
    windowheight = root2.winfo_reqheight() +200
    positionright = int(root2.winfo_screenwidth() / 2 - windowwidth / 2)
    positiondown = int(root2.winfo_screenheight() / 2 - windowheight / 1.2)
    root2.wm_geometry("%dx%d+%d+%d" % (windowwidth, windowheight, positionright, positiondown))

    def data(dete):
        for i in dete:
            Label(frame,text=i).grid(row=dete.index(i),column=0)
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=350,height=350)
    
    def restart(old_tab):
        root2.destroy()
        root.reopen()

    myframe=Frame(root2,relief=GROOVE,width=50,height=50,bd=1)
    myframe.place(x=10,y=10)
    canvas=Canvas(myframe)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    data(info)
    root2.protocol("WM_DELETE_WINDOW",lambda: restart(root))
    root2.mainloop()
