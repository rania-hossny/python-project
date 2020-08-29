from pymongo import MongoClient 
from tkinter import * 
 
def fun2(): 
    cluster = MongoClient("mongodb://localhost:27017/") 
    print(cluster.list_database_names()) 
    db = cluster["bloods"] 
    col = db["bloods"] 
    for x in col.find(): 
        print(x) 


    window = Tk()  # window->object name 
    window.geometry("1520x830+0+0")
    window.config(bg="red2")
     
     
    l=Label(window,text="BLOODS",bg="red2",fg="white",font=("nunito",44,"bold"))
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


    l1=Label(window,text="ID",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l1.place(x=30,y=160)
     
    e1 = Entry(window,width=25) 
    e1.place(x=200 , y=170)
     
    l2=Label(window,text="BLOOD TYPE",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l2.place(x=30,y=260)
     
    e2 = Entry(window,width=25) 
    e2.place(x=200, y=270)
     
    l3=Label(window,text="COST",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l3.place(x=30,y=360)
     
    e3 = Entry(window,width=25) 
    e3.place(x=200, y=370)
    
    l4=Label(window,text="DON_ID",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l4.place(x=30,y=460)
     
    e4 = Entry(window,width=25) 
    e4.place(x=200, y=470)

    l5 = Label(window, text="ID", bg="white", fg="red2", font=("nunito", 18, "bold", "italic"))
    l5.place(x=770, y=310)

    e5 = Entry(window, width=25)
    e5.place(x=830, y=320)


    def add():
        data={ 'id':e1.get(),
               'blood_type': e2.get(),
               'cost': e3.get(),
               'don_id':e4.get()
               }
        x=col.insert_one(data)
        tkinter.messagebox.showinfo('notice','one doc inserted')
     
     
    def delete(): 
        data = { 
            'id': e5.get()} 
        col.delete_one(data)
        tkinter.messagebox.askyesno('delete','r u sure to delete ?')
        tkinter.messagebox.showinfo('notice','one doc deleted')

    def update():
        print("h")

    def disp():
        for x in col.find():
        
            listbox.insert(END,x)

    def disp2():
        query={"id":e5.get()}
        x=col.find(query)
        for i in x:
            listbox.insert(END,i)
        
    def clear():  
        listbox.delete(0,last=END)
        
    b9 = Button(window, text=" CLEAR ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=clear) 
    b9.place(x=1200, y=110)

    b4 = Button(window, text=" ADD ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=add)
    b4.place(x=450, y=220)


    b5 = Button(window, text="UPDATE",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=7,height=1,font=("nunito",18,"bold"), command=update)
    b5.place(x=450, y=370)


    b6 = Button(window, text="DELETE",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=8,height=2,font=("nunito",14,"bold"), command=delete)
    b6.place(x=1200, y=190)

    b7 = Button(window, text="SHOW ONE",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=8,height=2,font=("nunito",14,"bold"), command=disp2)
    b7.place(x=1200, y=300)

    b8 = Button(window, text="SHOW ALL", activeforeground="red2", activebackground="white", bg="red2", fg="white", bd=5,relief="ridge", width=8, height=2, font=("nunito", 14, "bold"), command=disp)
    b8.place(x=1200, y=410)

    listbox=Listbox(f2,width=150,height=20)
    listbox.place(x=5,y=450)

    window.mainloop() 
