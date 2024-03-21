from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import random
import time
from tkinter import Tk, Entry, Label, Button, Frame
from tkcalendar import Calendar
from tkinter import ttk
import mysql.connector as mc
root=Tk()
root.title('BOOK MY SHOW')
root.geometry('800x500')


title=Label(root,text='login Page',bg='white',fg='Blue',font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

from PIL import ImageTk, Image


url = ImageTk.PhotoImage(Image.open(r"C:\Users\NEW ACER\Desktop\resume\tickets.png"))


p1 = Label(root, image = url)

p1.pack(side = "left", fill = "both")


label2 = Label(root,text='Username:',font=('Areal',25,'bold'),bg='white',fg='black',relief=RAISED,bd=12)
label2.place(x=310,y=100)

label3 = Label(root,text='Password:',font=('Areal',25,'bold'),bg='white',fg='black',relief=RAISED,bd=12)
label3.place(x=310,y=200)

entry1 = Entry(root,font=('Areal',20),relief=RAISED,bd=12)
entry1.place(x=550,y=100)

entry2 = Entry(root,font=('Areal',20),show=('*'),relief=RAISED,bd=12)
entry2.place(x=550,y=200)

from datetime import datetime

def book_now():
    b_name = name_entry.get()
    b_screen = screen_entry.get()
    b_date_str = date_entry.get()
    b_date = datetime.strptime(b_date_str, "%d.%m.%Y").timestamp()  # Convert to Unix timestamp
    b_time = time_entry.get()
    b_tickets = tc_entry.get()
    b_amount = amt_entry.get()

    # Connect to the MySQL database
    db = mc.connect(host="localhost", user="root", password="", database="sm")

    cur = db.cursor()

    # Define the query with placeholders
    query = "INSERT INTO book (Movie_name, Screen, Date, Show_timing, tickets, Amount) VALUES (%s, %s, %s, %s, %s, %s)"

    # Define the values as a tuple
    values = (b_name, b_screen, b_date, b_time, b_tickets, b_amount)
    cur.execute(query, values)
    db.commit()
    messagebox.showinfo('success','Booked successfully')
    cur.close()
    db.close()

def bookin():
    global name_entry, screen_entry, date_entry, time_entry, tc_entry, amt_entry
    bookin = Toplevel(root)
    bookin.title('BOOKED')
    bookin.config(bg="cyan")
    bookin.geometry('800x500')

    frame = Frame(bookin, bg='pink', relief='groove', borderwidth=15)
    frame.pack(padx=50, pady=45)

    db = mc.connect(host="localhost", user="root", password="", database="sm")
    cur = db.cursor()
    cur.execute('SELECT * FROM book')
    data = cur.fetchall()
    db.close()
    cur.close()

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            # Convert the 'Date' value to a readable format
            if j == 2:  # Assuming 'Date' is the third column (index 2)
                date_str = datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')
                label = Label(frame, text=date_str, bg='pink', padx=10, pady=5)
            else:
                label = Label(frame, text=value, bg='pink', padx=10, pady=5)
            label.grid(row=i, column=j)

    
    #def open_new_rootdow():
      
def login_window():

    
    
    login = Toplevel(root)
    login.title('BOOK NOW')
    login.config(bg="black")
    login.geometry('800x500')

    from tkinter import PhotoImage

    
    frame = Frame(login, bg='red', relief='raised', borderwidth=5)
    frame.pack(padx=100, pady=70)

    head_label = Label(frame, text='Booking details', bg='white', fg='red', relief='groove', font=('GARAMOND', 25))
    head_label.grid(row=1, column=0, padx=10, pady=5, sticky='s')
    
    global name_entry, screen_entry, date_entry, time_entry, tc_entry, amt_entry

    i_name = StringVar()
    i_screen = IntVar()
    i_date = StringVar()
    i_time = IntVar()
    i_tickets = IntVar()
    i_amount = IntVar()

    l_name = Label(frame, text='Movie name', bg='red', font=('Arial', 15))
    l_name.grid(row=3, column=0)
    name_entry = Entry(frame, textvariable=i_name, width=20)
    name_entry.grid(row=3, column=1, sticky='ew')

    l_screen = Label(frame, text='Screen', bg='red', font=('Arial', 15))
    l_screen.grid(row=5, column=0)
    screen_entry = Entry(frame, textvariable=i_screen, width=20)
    screen_entry.grid(row=5, column=1)
    
    from datetime import datetime

    

    l_date = Label(frame, text='Select Date', bg='red', font=('Arial', 15))
    l_date.grid(row=7, column=0)
    date_entry = ttk.Combobox(frame, textvariable=i_date, value=["28.01.2024", "29.01.2024", "30.01.2024", "31.01.2024", "01.02.2024"], width=20)
    date_entry.grid(row=7, column=1)

    l_time = Label(frame, text='Show Timing', bg='red', font=('Arial', 15))
    l_time.grid(row=9, column=0)
    time_entry = ttk.Combobox(frame, textvariable=i_time, value=["10.00AM", "1.15PM", "04.10PM", "7.15PM", "10.00PM"], width=20)
    time_entry.grid(row=9, column=1)

    l_tickets = Label(frame, text='No Of Tickets', bg='red', font=('Arial', 15))
    l_tickets.grid(row=13, column=0)
    tc_entry = ttk.Combobox(frame, textvariable=i_tickets, value=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width=20)
    tc_entry.grid(row=13, column=1)

    l_amount = Label(frame, text='Amount', bg='red', font=('Arial', 15))
    l_amount.grid(row=11, column=0)
    amt_entry = ttk.Combobox(frame, textvariable=i_amount, value=["190", "290", "390", "490"], width=20)
    amt_entry.grid(row=11, column=1)

    
    b1 = Button(frame, text="Book", fg='black', command=book_now)
    b1.grid(row=15, column=0, sticky='ew')

    b2 = Button(frame, text="History", fg='black',command=bookin)
    b2.grid(row=15, column=1, sticky='ew')

    img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\NEW ACER\Desktop\resume\download-movies.jpg"))
    img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\NEW ACER\Desktop\resume\images-movie2.jpg"))

    p1=Label(frame, image= img1)
    p1.grid(row=17,column=0,sticky='se')

    img1.image = img1
   
    p2=Label(frame, image= img2 )
    p2.grid(row=17,column=1,sticky='sw')

    img2.image = img2

    
    

button = Button(root, text='LOGIN', font=('Arial', 17), bg='blue', relief=RAISED, bd=15, command=login_window)
button.place(x=500, y=300)






root.mainloop()


