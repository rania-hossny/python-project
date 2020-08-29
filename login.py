from tkinter import *
from tkinter import scrolledtext
from PIL import *
from PIL import ImageTk,Image
from tkinter import messagebox

    
window = Tk()
 
window.title("Blood Bank")
 
window.geometry('500x700+500+100')

'''window.iconbitmap('myicon.ico')'''

f=Frame(window,height=700,width=500,bg="red")
f.place(x=0,y=0)
'''
img=Image.open("bg.png")
img=img.resize((500,700))
img = ImageTk.PhotoImage(img)
bgimg = Label(f, image=img)
bgimg.place(x=0,y=0)'''


l1 = Label(f, text="Login",fg="red2",font=("nunito",45,"bold"))
l1.place(x=150,y=10)

l2 = Label(window, text="USER NAME",fg="red2",font=("nunito",20,"bold","italic"))
l2.place(x=60,y=210)

'''userimg=Image.open("username.jpg")
userimg=userimg.resize((40,40))
userimg = ImageTk.PhotoImage(userimg)
imgl2 = Label(window, image=userimg)
imgl2.place(x=5,y=200)'''

username = Entry(window,width=25) 
username.place(x=250,y=215) 
    


l3 = Label(window, text="PASSWORD",fg="red2",font=("nunito",20,"bold","italic")) 
l3.place(x=60,y=350)

'''passwordimg=Image.open("password.png")
passwordimg=passwordimg.resize((40,40))
passwordimg = ImageTk.PhotoImage(passwordimg)
imgl3 = Label(window, image=passwordimg)
imgl3.place(x=5,y=340)'''

password = Entry(window,width=25,show="*") 
password.place(x=250,y=355) 

def x():

    if username.get()=="admin" and password.get()=="admin":
        import MainModule

    elif username.get()=="donor" and password.get()=="donor":
        import DonorsModule
        DonorsModule.fun1()

    elif username.get()=="blood" and password.get()=="blood":
        import BloodsModule
        BloodsModule.fun2()

    elif username.get()=="hospital" and password.get()=="hospital":
        import HospitalsModule
        HospitalsModule.fun3()

    elif username.get()=="bloodbank" and password.get()=="bloodbank":
        import BloodBankModule
        BloodBankModulefun5()

    elif username.get()=="mgr" and password.get()=="mgr":
        import BBMGR
        BBMGR.fun6()

    elif username.get()=="reception" and password.get()=="reception":
        import ReciptModule
        ReciptModule.fun4()

    else:
        messagebox.showinfo("login error","Incorrect username or password")

        
b1 = Button(window, text="LOGIN",activeforeground="red2",activebackground="white",bg="firebrick2",fg="white",bd=5,relief="ridge",width=7,font=("nunito",20,"bold"),command=x) 
b1.place(x=170,y=450)

    
window.mainloop()
