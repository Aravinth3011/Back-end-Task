from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def on_enter1(Event):
    if usernameentry.get()=='USERNAME':
        usernameentry.delete(0,END)

def on_enter2(Event):
    if passwordentry.get()=='PASSWORD':
        passwordentry.delete(0,END)

def hide():
    closeeye.config(file='closeye.png')
    passwordentry.config(show='*')
    eyebutton.config(command=show)
    
def show():
    closeeye.config(file='openeye.png')
    passwordentry.config(show='')
    eyebutton.config(command=hide)
    
def signup_page():
    root.destroy()
    import signup
    
def login_user():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    
    else:
        try:
            connect = pymysql.connect(
                                host="localhost", 
                                user="root", 
                                password="root",
                                database="userdata"
                                )
            mycursor = connect.cursor()
        except:
            messagebox.showerror('Error','Connection Is Not Establishment Try Again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Sucess','Login Successfull')
    
root=Tk()
root.geometry('800x520')
root.resizable(0,0)
root.title('Login Page')
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)

heading=Label(root,text='LOGIN',font=('Fancy',21,'bold'),bg='white',fg='firebrick1')
heading.place(x=555,y=80)

usernameentry=Entry(root,width=25,font=('Fancy',11,'bold'),bd=0,fg='firebrick1')
usernameentry.place(x=500,y=175)
usernameentry.insert(0,'USERNAME')
usernameentry.bind('<FocusIn>',on_enter1)
Frame(root,width=225,height=2,bg='firebrick1').place(x=495,y=193)

passwordentry=Entry(root,width=25,font=('Fancy',11,'bold'),bd=0,fg='firebrick1',show='*')
passwordentry.place(x=500,y=225)
passwordentry.insert(0,'PASSWORD')
passwordentry.bind('<FocusIn>',on_enter2)
Frame(root,width=225,height=2,bg='firebrick1').place(x=495,y=243)
closeeye=PhotoImage(file='closeye.png')
eyebutton=Button(root,image=closeeye,bd=0,bg='white',activebackground='white',command=hide)
eyebutton.place(x=695,y=216)
forgetbutton=Button(root,text='Forget Password',font=('Fancy',9,'bold'),bd=0,bg='white',activebackground='white',activeforeground='firebrick1')
forgetbutton.place(x=620,y=255)
loginbutton=Button(root,text="LOGIN",font=('Fancy',16,'bold'),bd=0,width=18,bg='firebrick1',fg='white',activeforeground='white',activebackground='firebrick1',command=login_user)
loginbutton.place(x=490,y=295)
orlabel=Label(root,text='--------------OR---------------',font=('Fancy',16,'bold'),bd=0,bg='white',fg='firebrick1')
orlabel.place(x=490,y=342)
fb_logo=PhotoImage(file='facebook.png')
fblabel=Label(root,image=fb_logo)
fblabel.place(x=550,y=375)
gl_logo=PhotoImage(file='google.png')
gllabel=Label(root,image=gl_logo)
gllabel.place(x=620,y=375)
signuplabel=Label(root,text="Don't have an account",font=('Fancy',10,'bold'),bd=0,bg='white',fg='black')
signuplabel.place(x=490,y=440)
signupbutton=Button(root,text="SIGN UP",font=('Fancy',10,'bold'),bd=0,bg='white',fg='firebrick1',command=signup_page)
signupbutton.place(x=634,y=437)

root.mainloop()