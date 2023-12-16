import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="lms"
)
from tkinter import *
import vender_login
from admin_login import *
from vender_login import *
gui = Tk() 
gui.configure(background="light green") 
gui.title("Library sytem management") 
gui.geometry("800x500") 
equation = StringVar()

#expression_field = Entry(gui, textvariable=equation) 
 
#expression_field.grid(columnspan=4, ipadx=70)

btn=Button(gui,text='Admin Login',font=('Arial',25), command= admin_login)
btn.place(x=50,y=100)

btn=Button(gui,text='Vender Login',font=('Arial',25), command= vender_login)
btn.place(x=530,y=100)

btn=Button(gui,text='User Login',font=('Arial',25))
btn.place(x=300,y=100)
 
