from pymongo import MongoClient 
from tkinter import *
 
cluster = MongoClient("mongodb://localhost:27017/") 
print(cluster.list_database_names()) 
db = cluster["bloods"] 


window = Tk()  # window->object name 
window.geometry("1250x820+130+0")
window.config(bg="white")

'''window.iconbitmap('myicon.ico')'''
window.title("Blood Bank")



l1=Label(window,text="BLOOD BANK",bg="white",fg="red2",font=("nunito",44,"bold"))
l1.place(x=420,y=50)

def c1() :
    import DonorsModule
    DonorsModule.fun1()

b1=Button(window,text="DONORS",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c1)
b1.place(x=100,y=200)


def c2() :
    import BloodsModule
    BloodsModule.fun2()

b2=Button(window,text="BLOODS",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c2)
b2.place(x=750,y=200)


def c3() :
    import HospitalsModule
    HospitalsModule.fun3()

b3=Button(window,text="HOSPITALS",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c3)
b3.place(x=100,y=400)


def c4() :
    import ReciptModule
    ReciptModule.fun4()

b4=Button(window,text="RECEPTIONISTS",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c4)
b4.place(x=750,y=400)

def c5() :
    import BloodBankModule
    BloodBankModule.fun5()

b5=Button(window,text="BLOODBANK",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c5)
b5.place(x=100,y=600)


def c6() :
    import BBMGRModule
    BBMGRModule.fun6()

b6=Button(window,text="BLOODBANK MGR",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c6)
b6.place(x=750,y=600)


window.mainloop()
