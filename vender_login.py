from tkinter import *
from vendor import *

def vender_login():

    def get_value():
        c=(entry.get())
        print(type(c))
    def check_label_data(label_to_check):
        # MySQL database connection parameters
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',
            'database': 'lms',
            'port': '3306'
            }
        # Connect to the MySQL server
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the MySQL query to check if the label data is present
        query = "SELECT * FROM pass WHERE user_id = %s"
        
        # Execute the query with the label data as a parameter
        cursor.execute(query, (label_to_check,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if the label data is present in the table
        if result:
            print(f"Label data '{label_to_check}' is present in the table.")
        else:
            print(f"Label data '{label_to_check}' is not present in the table.")

        label_to_check= c
        check_label_data(label_to_check)
    gui = Tk() 
    gui.configure(background="light grey") 
    gui.title("vender_login") 
    gui.geometry("800x500") 
    equation = StringVar()        

    lbl=Label(gui,text='Event Management System',width= 33,bg='sky blue',fg='black',font=('Arial',30))
    lbl.place(x=20,y=120)
    
    lbl2=Label(gui,text='User Id',bg='blue',fg='black',font=('Arial',30))
    lbl2.place(x=50,y=230)
    
    lbl3=Label(gui,text='Password',bg='blue',fg='black',font=('Arial',30))
    lbl3.place(x=50,y=300)

    lbl4=Label(gui,text='CHART',bg='blue',fg='black',font=('Arial',30))
    lbl4.place(x=20,y=38)

    lbl5=Label(gui,text='BACK',bg='blue',fg='black',font=('Arial',30))
    lbl5.place(x=680,y=38)

    var=StringVar()
    entry=Entry(gui,bg='sky blue',fg='Black',font=('Arial',35), width= 18,textvariable=var)
    entry.place(x=300,y=230)
    
    var=StringVar()
    ent2=Entry(gui,bg='sky blue',fg='Black',show="*", width= 18,font=('Arial',35),textvariable=var)
    ent2.place(x=300,y=300)
    # button--------------------------------------------------------------------------
    btn=Button(gui,text='Cancel',bg='grey',fg='Black',font=('Arial',25))
    btn.place(x=410,y=400)
    #timmer Button
    btn=Button(gui,text='Login',bg='grey',fg='Black',font=('Arial',25), command= get_value)
    btn.place(x=600,y=400)

vender_login()
