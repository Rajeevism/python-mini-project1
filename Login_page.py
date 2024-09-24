from tkinter import *
from tkinter import messagebox
import openpyxl

root = Tk()
root.title('Login Page')
root.geometry('1080x600+300+200')
root.configure(bg="#A3D8FF")
root.resizable(True,True)

def get_credentials():
  wb = openpyxl.load_workbook('user_data.xlsx')
  sheet = wb.active

  credentials = []
  for row in sheet.iter_rows(min_row=2, max_col=3):
    email = row[1].value.strip()
    Password = row[2].value.strip()
    credentials.append((email, Password))

  return credentials
  
def sign_in():
  email_id = user_id.get()
  passwd = password.get()

  credentials = get_credentials()
  found_match = False  # Flag to indicate if a match was found

  for email, Password in credentials:
    if email_id == email and passwd == Password:
      # Login successful logic
      messagebox.showinfo("Success", "Succesfully Logged In!")
      screen = Toplevel(root)
      screen.title("App")
      screen.geometry('850x450+300+200')
      screen.config(bg='white')

      Label(screen,text='Vanakkam!',bg='#fff',font=('Times New Roman',48,'bold')).pack(expand=True)
      screen.mainloop()
      found_match = True  # Set the flag to True
      break
  if not found_match:
    messagebox.showerror("Invalid", "Invalid Email address or Password...")

#--------------------------------------------------------------
img = PhotoImage(file='login_icon.png')
Label(root,image=img,bg='#A3D8FF').place(x=50,y=70)

frame = Frame(root,width=600,height=500,bg='#A3D8FF')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign In',fg='blue',bg='#A3D8FF',font=('Times New Roman',28,'bold'))
heading.place(x=150,y=5)

####------------------------------------------
def on_enter(e):
      user_id.delete(0,'end')
def on_leave(e):
      name=user_id.get()
      if name==' ':
            user_id.insert(0,'Enter your email id')
user_id = Entry(frame,width=35,fg='blue',border=1,bg='#A3D8FF',font=('Times New Roman',16))
user_id.place(x=40,y=80)
user_id.insert(0,'Enter your email id')
user_id.bind('<FocusIn>',on_enter)
user_id.bind('<FocusOut>',on_leave)
####-------------------------------------------
def on_enter(e):
      password.delete(0,'end')
def on_leave(e):
      name=password.get()
      if name==' ':
            password.insert(0,'Enter your password')
password = Entry(frame,width=35,fg='blue',border=1,bg='#A3D8FF',font=('Times New Roman',16))
password.place(x=40,y=120)
password.insert(0,'Enter your password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
#--------------------------------------------------------------#
Button(frame,width=35,pady=7,text='Sign in', bg='blue',fg='white',border=0,command=sign_in).place(x=35,y=160)
label=Label(frame,text="Don't have an account?",fg='blue',bg='#A3D8FF',font=('Times New Roman',16))
label.place(x=40,y=210)
#--------------------------------------------------------------------
def open_sign_up():
  root.destroy()  # Destroy the current login window
  import Sign_up_page  # Import the signup file

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='#A3D8FF',cursor='hand2',fg='blue',command=open_sign_up)
sign_up.place(x=245,y=215)
root.mainloop()
