import tkinter
import tkinter.ttk
import tkinter.messagebox
class mywindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        
        self.entry_setter=tkinter.StringVar()
        self.geometry("500x500")

        self.menu_master=tkinter.Menu(self)
        self.config(menu=self.menu_master)

        self.master=tkinter.Menu(self.menu_master)
        self.master.add_command(label="new")
        self.master.add_command(label="old")
        self.menu_master.add_cascade(label="master",menu=self.master)
        

     
        self.dester=tkinter.Menu(self.menu_master)
        self.dester.add_command(label="dfdf")
        self.dester.add_command(label="f")
        self.menu_master.add_cascade(label="dester",menu=self.dester)
        

        self.insider=tkinter.Menu(self.dester)
        self.insider.add_command(label="new_company")
        self.insider.add_command(label="new")
        
        self.dester.add_cascade(label="leno",menu=self.insider)


        self.combo=tkinter.ttk.Combobox(value=("vfv","fvfvf","vfv"),state="readonly")
        self.combo.grid(row=1,column=0)





        self.button=tkinter.ttk.Button(master=self,text="show",width=5,command=self.show)
        self.button.grid(row=2,column=0)

        self.entry=tkinter.ttk.Entry(self,textvariable=self.entry_setter)
        self.entry.grid(row=3,column=1)


        self.fram1=tkinter.Frame(self,width=10,height=24)
        self.fram_lab1=tkinter.ttk.Label(self.fram1,text="my self")
        self.fram_lab1.grid(row=0,column=0)
        self.fram_lab2=tkinter.ttk.Label(self.fram1,text="her self")
        self.fram_lab2.grid(row=1,column=2)
        self.fram1.grid(row=10,column=10)
    def show(self):
        tkinter.messagebox.showinfo(title="info",message=f"{self.combo.get()}  {self.entry_setter.get()}")
        
window=mywindow()
window.mainloop()