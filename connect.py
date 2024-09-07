# import mysql.connector as myc

# conn=myc.connect(host="localhost",user="root",password="1003")

# mycursor=conn.cursor()

# mycursor.execute("create database chandni")

# print("done")

from tkinter import*
import mysql.connector as myc
from tkinter import messagebox
root=Tk()
root.geometry('300x200')
root.title("library system")
def regis():
    name=ent6.get()
    colllege_enrollment_number=ent9.get()
    set_user_name=ent7.get()
    set_password=ent8.get()
    if name=="" or colllege_enrollment_number=="" or set_user_name=="" or set_password=="":
        messagebox.showerror("Error","Please fill all the fields")
    else:
        reg=myc.connect(host="localhost",user="root",password="1003",database="library_management_system")
        cur1=reg.cursor()
        sql="insert into tbl2(name,college_enrollment_number,set_user_name,set_password)values(%s,%s,%s,%s)"
        val=(name,colllege_enrollment_number,set_user_name,set_password)
        cur1.execute(sql,val)
        reg.commit()
        cur1.close()
        reg.close()
        messagebox.showinfo("success"," you are successfully registered")
new_registration=Tk()
new_registration.geometry("500x230")
new_registration.title("new_member")
lab9=Label(new_registration,text="new_registration_page!!",font='arialblack 12 bold underline')
lab9.place(x=20,y=5)
lab10=Label(new_registration,text="name",font='arialblack 12 bold')
lab10.place(x=20,y=50)
ent6=Entry(new_registration,width=20)
ent6.place(x=300,y=50)
lab11=Label(new_registration,text="college_enrollment_number",font='arialblack 12 bold')
lab11.place(x=20,y=80)
ent9=Entry(new_registration,width=20)
ent9.place(x=300,y=80)
lab12=Label(new_registration,text="set_user_name",font='arialblack 12 bold')
lab12.place(x=20,y=110)
ent7=Entry(new_registration,width=20)
ent7.place(x=300,y=110)
lab13=Label(new_registration,text="set_password",font='arialblack 12 bold')
lab13.place(x=20,y=140)
ent8=Entry(new_registration,width=20)
ent8.place(x=300,y=140)
btn9=Button(new_registration,text="register",font='arialblack 12 bold',command=regis)
btn9.place(x=350,y=180)
btn10=Button(new_registration,text="exit",font='arialblack 12 bold',command=new_registration.destroy)
btn10.place(x=310,y=180)
# btn11=Button(new_registration,text="login_page",font='arialblack 12 bold')
# btn11.place(x=260,y=180)


def log():
    user_name=ent1.get()
    password=ent3.get()
    if user_name=="" or password=="":
        messagebox.showerror("Error","Please fill all the fields")
    elif user_name=="chandni" and password=="12345":
        messagebox.showinfo("sucess","login is sucessful")
ent4=Label(root,text="Login Page!!",font='arialblack 12 bold underline')
ent4.place(x=20,y=5)
ent=Label(root,text="user_name",font='arialblack 12 bold')
ent.place(x=20,y=50)
ent1=Entry(root,width="10",font='arialblack 12 bold')
ent1.place(x=120,y=50)
ent2=Label(root,text="password",font='arialblack 12 bold')
ent2.place(x=20,y=100)
ent3=Entry(root,width="10",font='arialblack 12 bold')
ent3.place(x=120,y=100)
ent5=Button(root,text='exit',font='arialblack 12 bold',command=root.destroy)
ent5.place(x=148,y=150)
btn=Button(root,text="login>>",font='arialblack 12 bold',command=log)
btn.place(x=190,y=150)
btn7=Button(root,text="new_registration",font='arialblack 12 bold')
btn7.place(x=9,y=150)
mainloop()