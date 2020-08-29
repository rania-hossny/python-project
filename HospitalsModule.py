from pymongo import MongoClient 
from tkinter import * 
 
def fun3():
    cluster = MongoClient("mongodb://localhost:27017/") 
    print(cluster.list_database_names()) 
    db = cluster["bloods"] 
    col = db["hospitals"] 
    for x in col.find(): 
        print(x) 


    window = Tk()  # window->object name 
    window.geometry("1520x830+0+0")
    window.config(bg="red2")
    '''window.iconbitmap('myicon.ico')'''
    window.title("Hospitals")
     

     
    l=Label(window,text="HOSPITALS",bg="red2",fg="white",font=("nunito",44,"bold"))
    l.place(x=600,y=10)

    f1 = Frame(window, height=730, width=710, bg="white")
    f1.place(x=20, y=80)
    '''
    img1=Image.open("bg.png")
    img1=img1.resize((710,730))
    img1 = ImageTk.PhotoImage(img1)

    bgimg1 = Label(f1,height=730,width=710,image=img1)
    bgimg1.place(x=0,y=0)
    '''

    f2 = Frame(window, height=730, width=745, bg="white")
    f2.place(x=750, y=80)

    l1=Label(window,text="NAME",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l1.place(x=30,y=210)
     
    e1 = Entry(window,width=25) 
    e1.place(x=200 , y=220)

    l2=Label(window,text="PHNO",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l2.place(x=30,y=310)
     
    e2 = Entry(window,width=25) 
    e2.place(x=200, y=320)
     
    l3=Label(window,text="ADDRESS",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l3.place(x=30,y=410)
     
    e3 = Entry(window,width=25) 
    e3.place(x=200, y=420)

    l4 = Label(window, text="ID", bg="white", fg="red2", font=("nunito", 18, "bold", "italic"))
    l4.place(x=770, y=310)

    e4 = Entry(window, width=25)
    e4.place(x=830, y=320)

    l5 = Label(window, text="ID", bg="white", fg="red2", font=("nunito", 18, "bold", "italic"))
    l5.place(x=30, y=120)

    e5 = Entry(window, width=25)
    e5.place(x=200, y=130)

    def add():
        data = {'id':e5.get(),
                "name": e1.get(),
                "phno":e2.get(),
                'address': e3.get()
                } 
        col.insert_one(data)
        tkinter.messagebox.showinfo('notice','one doc inserted')
     
     
    def delete(): 
        data = { 'id':e4.get() }
        col.delete_one(data)
        tkinter.messagebox.askyesno('delete','r u sure to delete ?')
        tkinter.messagebox.showinfo('notice','one doc deleted')

    def update():
        print("h")

    def disp():
        for x in col.find():
        
            listbox.insert(END,x)
    def disp2():
        query={"id":e4.get()}
        x=col.find(query)
        for i in x:
            listbox.insert(END,i)

    def clear():  
        listbox.delete(0,last=END)

    b4 = Button(window, text=" ADD ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=add)
    b4.place(x=450, y=220)

    b5 = Button(window, text="Delete",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=7,height=1,font=("nunito",18,"bold"), command=update)
    b5.place(x=450, y=370)


    b6 = Button(window, text="UPDATE",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=8,height=2,font=("nunito",14,"bold"), command=delete)
    b6.place(x=1200, y=190)


    b7 = Button(window, text="SHOW",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=8,height=2,
                font=("nunito",14,"bold"), command=disp2)
    b7.place(x=1200, y=300)

    b8 = Button(window, text="SHOW ALL", activeforeground="red2", activebackground="white", bg="red2", fg="white", bd=5,relief="ridge",
                width=8, height=2, font=("nunito", 14, "bold"), command=disp)
    b8.place(x=1200, y=410)

    b9 = Button(window, text=" CLEAR ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=clear) 
    b9.place(x=1200, y=110)

    listbox=Listbox(f2,width=150,height=20)
    listbox.place(x=5,y=450)

    window.mainloop() 
