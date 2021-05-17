import tkinter
from tkinter import *
#from tkinter import ttk
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect("D:\Store Management Software\Database\store1.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory1")
for r in result:
    id = r[0]


class Database:
    def __init__(self,master,*args,**kwargs):

        self.master = master
        self.heading = Label(master,text="UPDATION",font=('cambria 40 bold'),fg='white', bg='#2A7563')
        self.heading.place(x=700,y=0)
        
        #label and entries for id
        self.id_le = Label(master,text="ENTER ID",font=("cambria",18,"bold"),fg = 'white', bg='#2A7563')
        self.id_le.place(x=0,y=80)

        self.id_leb= Entry(master,font=('cambria 18 bold'),width = 10)
        self.id_leb.place(x =320,y =80)

        self.btn_search=Button(master,text="Search",bg='#7ac936',width=15,height=2,command = self.search)
        self.btn_search.place(x=500,y=75)



        #labels and entries for the window
        self.name_l = Label(master,text ="PRODUCT NAME",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.name_l.place(x=0,y=140)

        self.stock_l = Label(master,text ="STOCK AVAILABLE",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.stock_l.place(x=0,y=200 )

        self.cp_l = Label(master,text ="COST PRICE",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.cp_l.place(x=0,y=260)

        self.sp_l = Label(master,text ="SELLING PRICE",font=('cambria 18 bold'), fg = 'white',bg='#2A7563')
        self.sp_l.place(x=0,y=320)

        self.totalsp_l = Label(master,text ="TOTAL SELLING PRICE",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.totalsp_l.place(x=0,y=380)

        self.totalcp_l = Label(master,text ="TOTAL COST PRICE",font=('cambria 18 bold'), fg = 'white',bg='#2A7563')
        self.totalcp_l.place(x=0,y=440)

        self.vendor_l = Label(master,text ="VENDOR",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.vendor_l.place(x=0,y=500)

        self.vendor_phone_l = Label(master,text ="VENDOR PHONE NO.",font=('cambria 18 bold'),fg = 'white', bg='#2A7563')
        self.vendor_phone_l.place(x=0,y=560)

        # self.id_l = Label(master,text ="ID",font=('arial 18 bold'))
        # self.id_l.place(x=0,y=420)


         #entries for the labels 

        self.name_e = Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=320, y = 140)

        self.stock_e = Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=320, y = 200)

        self.cp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=320, y = 260)

        self.sp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=320, y = 320)

        self.totalsp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.totalsp_e.place(x=320, y = 380)

        self.totalcp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.totalcp_e.place(x=320, y = 440)

        self.vendor_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x =320, y = 500)


        self.vendor_phone_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x =320, y = 560)

        # self.id_e = Entry(master,width=25,font=('arial 18 bold'))
        # self.id_e.place(x=380,y=420)


        #button to add to the database

        self.btn_add = Button(master,text ="Update",width= 25,height = 2,bg ='#c2673d',command = self.update)
        self.btn_add.place(x=464,y = 620)


        
        #text box for the logs


        self.tbox = Text(master,width=70,height = 30)
        self.tbox.place(x = 700,  y= 80 )
        self.tbox.insert(END,"ID has reached upto:"+str(id))
        self.tbox.insert(END,"\n")
        show_all = "Select id,name From inventory1"
        show = c.execute(show_all)
        rows = c.fetchall()
        self.tbox.insert(END,rows)
        
        



    def search(self,*args,**kwargs):
        sql = "SELECT *FROM inventory1 WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed profit
            self.n8 = r[8] #vendor
            self.n9 = r[9] #vendor phone number
        conn.commit()
        #insert into the entries to update

        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))  

        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))  

        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))  

        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0,str(self.n5))  

        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0,str(self.n6)) 


        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))  

        self.vendor_phone_e.delete(0,END)
        self.vendor_phone_e.insert(0,str(self.n9))

    def update(self,*args,**kwargs):
        #get all updated values

        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()

        query = "UPDATE inventory1 SET name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,vendor=?,vendor_phoneno=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Database Updated")


             



root = Tk()
b = Database(root)
root.geometry('1920x1080')
root.title("Update the Database")
root.configure(background = "#2A7563")
root.mainloop()