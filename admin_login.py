from tkinter import *
def admin_login(): 
    
    gui = Tk() 
    gui.configure(background="light grey") 
    gui.title("admin_login") 
    gui.geometry("800x500") 
    equation = StringVar()

    lbl=Label(gui,text='Event Management System',width= 33,bg='sky blue',fg='black',font=('Arial',30))
    lbl.place(x=20,y=70)
    
    lbl2=Label(gui,text='User Id',bg='blue',fg='black',font=('Arial',30))
    lbl2.place(x=50,y=230)
    
    lbl3=Label(gui,text='Password',bg='blue',fg='black',font=('Arial',30))
    lbl3.place(x=50,y=300)

    var=StringVar()
    ent=Entry(gui,bg='sky blue',fg='Black',font=('Arial',35), width= 18,textvariable=var)
    ent.place(x=300,y=230)
    
    var=StringVar()
    ent=Entry(gui,bg='sky blue',fg='Black',show="*", width= 18,font=('Arial',35),textvariable=var)
    ent.place(x=300,y=300)
    # button--------------------------------------------------------------------------
    btn=Button(gui,text='Cancel',bg='grey',fg='Black',font=('Arial',25))
    btn.place(x=410,y=400)
    #timmer Button
    btn=Button(gui,text='Login',bg='grey',fg='Black',font=('Arial',25))
    btn.place(x=600,y=400)
