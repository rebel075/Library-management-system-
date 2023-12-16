from tkinter import *
def vendor():
    
    gui = Tk() 
    gui.configure(background="blue") 
    gui.title("Vendor") 
    gui.geometry("1100x400") 
    equation = StringVar()
    #labels
    lbl=Label(gui,text='Welcome\nVendor',bg='white',fg='black',width=41,font=('Arial',30))
    lbl.place(x=100,y=70)

    #buttons
    btn1=Button(gui,text='Your Item',font=('Arial',25),command='Pass')
    btn1.place(x=100,y=300)

    btn2=Button(gui,text='Add New Item',font=('Arial',25),command='Pass')
    btn2.place(x=300,y=300)

    btn3=Button(gui,text='Transaction',font=('Arial',25),command='Pass')
    btn3.place(x=600,y=300)

    btn4=Button(gui,text='LogOut',font=('Arial',25),command='Pass')
    btn4.place(x=900,y=300)
