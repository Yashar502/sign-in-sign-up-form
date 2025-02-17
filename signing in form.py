import tkinter 
from tkinter import *
import PIL 
from PIL import ImageTk,Image
# importations
form= Tk()
# the window
form.geometry('600x420')
# resolution of the created window
def DONE():
    first_name=entry_1.get()
    last_name=entry_2.get()
    age=entry_3.get()
    ID=entry_4.get()
    data=[first_name,last_name,age,ID]
    yep=Image.open('lol done.png')
    nope=Image.open('Untitled.png')
    img_yep=ImageTk.PhotoImage(yep)
    img_nope=ImageTk.PhotoImage(nope)
    for i in data:
        if len(i)==0:
            NO=Label(form,image=img_nope)
            NO.image=img_nope
            NO.place(x=300,y=60)
        else:
            ok=Label(form,image=img_yep)
            ok.image=img_yep
            ok.place(x=300,y=60)
            
entry_1=Entry(form)
entry_2=Entry(form)
entry_3=Entry(form)
entry_4=Entry(form)
entry_1.place(x=160,y=60)
entry_2.place(x=160,y=110)
entry_3.place(x=160,y=160)
entry_4.place(x=160,y=210)

first_name_label=Label(form,text='First Name:',font=('Franklin Gothic',18,'bold italic'))
last_name_label=Label(form,text='Last Name:',font=('Franklin Gothic',18,'bold italic'))
age_label=Label(form,text='Age:',font=('Franklin Gothic',18,'bold italic'))
ID_code_label=Label(form,text='ID code:',font=('Franklin Gothic',18,'bold italic'))


first_name_label.place(x=20,y=50)
last_name_label.place(x=20,y=100)
age_label.place(x=100,y=150)
ID_code_label.place(x=60,y=200)

send=Button(form,text='SEND',font=('Franklin Gothic',20,'bold'),command=DONE)
send.place(x=150,y=260)
form.mainloop()