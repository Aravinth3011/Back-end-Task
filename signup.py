from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def  clear():
    emailentry.delete(0,END)
    usernameentry.delete(0,END)
    passwordentry.delete(0,END)
    confirmpassentry.delete(0,END)
    
def signin_page():
    signup_window.destroy()
    import signin
    
def connect_database():
    if emailentry.get()=='' or usernameentry.get()=='' or passwordentry.get()=='' or confirmpassentry.get()=='':
        messagebox.showerror('ERROR','All Fields Are Required')
    elif passwordentry.get() !=confirmpassentry.get():
        messagebox.showerror('ERROR','Password Mismatch')
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
            messagebox.showerror('ERROR','Database Connectivity Issue')
            return
        mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameentry.get()))
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('ERROR','Username Already Taken')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailentry.get(),usernameentry.get(),passwordentry.get()))
            connect.commit()
            connect.close()
            messagebox.showinfo('Success','Registration is Sucessfull')
            clear()
            signup_window.destroy()
            import signin
        
signup_window=Tk()
signup_window.geometry('800x520')
signup_window.resizable(0,0)
signup_window.title('Signup Page')
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(signup_window,image=bgimage)
bglabel.place(x=0,y=0)

heading=Label(signup_window,text='CREATE AN ACCOUNT',font=('Fancy',18,'bold'),bg='white',fg='firebrick1')
heading.place(x=470,y=65)
Frame(signup_window,width=270,height=2,bg='firebrick1').place(x=470,y=95)

emaillabel=Label(signup_window,text='Email',font=('Fancy',11,'bold'),bd=0,fg='firebrick1',bg='white')
emaillabel.place(x=480,y=130)
emailentry=Entry(signup_window,width=29,font=('Fancy',11,'bold'),bd=2,fg='white',bg='firebrick1')
emailentry.place(x=485,y=155)
usernamelabel=Label(signup_window,text='Username',font=('Fancy',11,'bold'),bd=0,fg='firebrick1',bg='white')
usernamelabel.place(x=480,y=185)
usernameentry=Entry(signup_window,width=29,font=('Fancy',11,'bold'),bd=2,fg='white',bg='firebrick1')
usernameentry.place(x=485,y=205)
passwordlabel=Label(signup_window,text='Password',font=('Fancy',11,'bold'),bd=0,fg='firebrick1',bg='white')
passwordlabel.place(x=480,y=235)
passwordentry=Entry(signup_window,width=29,font=('Fancy',11,'bold'),bd=2,fg='white',bg='firebrick1')
passwordentry.place(x=485,y=255)
confirmpasslabel=Label(signup_window,text='Confirm Password',font=('Fancy',11,'bold'),bd=0,fg='firebrick1',bg='white')
confirmpasslabel.place(x=480,y=285)
confirmpassentry=Entry(signup_window,width=29,font=('Fancy',11,'bold'),bd=2,fg='white',bg='firebrick1')
confirmpassentry.place(x=485,y=305)
terms=Checkbutton(signup_window,text='I agree to the Terms & Conditions',font=('Fancy',8,'bold'),bd=2,fg='black',bg='white')
terms.place(x=480,y=335)
signupbutton=Button(signup_window,text="SIGN UP",font=('Fancy',16,'bold'),bd=0,width=18,bg='firebrick1',fg='white',activeforeground='white',activebackground='firebrick1',command=connect_database)
signupbutton.place(x=485,y=365)
signinlabel=Label(signup_window,text="Already have an account",font=('Fancy',10,'bold'),bd=0,bg='white',fg='black')
signinlabel.place(x=490,y=420)
signinbutton=Button(signup_window,text="Sign in",font=('Fancy',10,'bold'),bd=0,bg='white',fg='firebrick1',command=signin_page)
signinbutton.place(x=650,y=417)




signup_window.mainloop()