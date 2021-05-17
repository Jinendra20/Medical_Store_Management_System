import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk

conn = sqlite3.connect("D:\Store Management Software\Database\store1.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory1")
for r in result:
    id = r[0]



class Database:
    def __init__(self,master,*args,**kwargs):

        self.master = master
        self.heading = Label(master,text="ENTRY",font=('CAMBRIA 40 bold'),fg='white', bg='#2A7563')
        self.heading.place(x=750,y=0)
        

         #labels and entries for the window
        self.name_l = Label(master,text ="PRODUCT NAME",font=('consolas 20 bold'), bg='#2A7563', fg = 'white')
        self.name_l.place(x=20,y=120)

        self.stock_l = Label(master,text ="STOCK",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.stock_l.place(x=20,y=200 )

        self.cp_l = Label(master,text ="COST",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.cp_l.place(x=20,y=280)

        self.sp_l = Label(master,text ="SELL",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.sp_l.place(x=20,y=360)

        self.vendor_l = Label(master,text ="VENDOR ",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.vendor_l.place(x=20,y=440)

        self.vendor_phone_l = Label(master,text ="VENDOR PHONE",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.vendor_phone_l.place(x= 20,y=520)

        self.id_l = Label(master,text ="PRODUCT ID",font=('CAMBRIA 18 bold'),bg='#2A7563', fg = 'white')
        self.id_l.place(x=20,y=600)


         #entries for the labels 

        self.name_e = Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=380, y = 120)
        self.name_e.focus()

        self.stock_e = Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380, y = 200)

        self.cp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380, y = 280)

        self.sp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380, y = 360)

        self.vendor_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x = 380, y = 440)


        self.vendor_phone_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x = 380, y = 520)

        self.id_e = Entry(master,width=25,font=('arial 18 bold'))
        self.id_e.place(x=380,y=600)


        #button to add to the database

        self.btn_add = Button(master,text ="New Entry",width= 20,height = 2,bg ='#c2673d',command = self.get_items)
        self.btn_add.place(x=590,y = 680)


        self.btn_clear = Button(master,text="Clear All",width = 20, height = 2,bg = '#7ac936',command = self.clear_all)
        self.btn_clear.place(x=350,y=680)

        #text box for the logs


        self.tbox = Text(master,width=100,height = 30)
        self.tbox.place(x = 750,  y= 120 )
        self.tbox.insert(END,"ID has reached upto : " +str(id))

    def get_items(self, *args, **kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get() 
        self.cp = self.cp_e.get() 
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        #dynamic entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name =='' or self.stock == '' or self.cp == '' or self.sp =='':
            tkinter.messagebox.showerror("Error", "Please Fill all the entries.")

         
        else:
            sql = "INSERT INTO inventory1(name, stock , cp, sp,totalcp, totalsp,assumed_profit, vendor,vendor_phoneno) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,( self.name ,self.stock,self.cp,self.sp,self.totalcp,self.totalsp, self.assumed_profit,self.vendor,self.vendor_phone))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Successfully added to the database")
            #textbox insert
            self.tbox.insert(END,"\n\nInserted "+ "\t" + str(self.name) + "\t" + "into the database with code" + "\t" + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success" , "Successfully added to the database")

    def clear_all(self , *args , **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0,END)
        self.name_e.focus()
               


        

root = Tk()
b = Database(root)
root.geometry('1920x1080')
root.title("New Entry")
root.configure(background = "#2A7563")
root.mainloop()





