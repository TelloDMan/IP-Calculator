from tkinter import *
import tkinter as tk

class Lotfi(Entry):

    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set


    def remove(self,event):
         if event.keysym == "BackSpace":
            self.old_value = self.old_value[:-1]


    def check(self, *args):
        
        if self.get().isdigit():   
            self.old_value = self.get()
            

        elif self.get().isdigit() == False:
            self.set(self.old_value)
            
 #   def gett(self):
  #      return self.old_value
#

#def close_win(instance):
#    instance.destroy()


class PopUp(tk.Tk):
    def __init__(self):
       pass
       
def popupwin():

   top= Tk()
   top.title("New Prefix")
   #positionright = int(top.winfo_screenwidth() / 2 )
   #positiondown = int(top.winfo_screenheight() / 2 )
   #top.geometry("+{}+{}".format(positionright, positiondown))
   top.geometry("400x150")
   top.eval('tk::PlaceWindow . center')
   
   texts = Label(top,text="Please type a new subnet in digits and press Enter")
   texts.pack()
   entr=Lotfi(top, width=25)
   entr.focus_set()
   entr.pack()

   top.bind('<BackSpace>',lambda x:entr.remove(x))
   x1 = top.bind('<KP_Enter>', lambda x: top.destroy())
   x2 = top.bind('<Return>', lambda x:top.destroy())


   top.mainloop()
   return entr.old_value
   


if __name__ == "__main__":
    popupwin()