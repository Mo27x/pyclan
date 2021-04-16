from tkinter import *

  
root = Tk()
root.title("Chat Together")
root.geometry("400x250")

def showId():
    global ID
    global e2
    ID.place(x=30,y=140)
    e2.place(x = 120, y = 140)
def hideId():
    global ID
    global e2
    ID.place_forget()
    e2.place_forget()

inizio=Label(root, text="Welcome to Chat Together").place(x=120, y=10)
SignIn = Button(root, text = "Sign In",command=hideId,activebackground = "pink", activeforeground = "blue").place(x = 140, y = 50)  
Login=Button(root, text = "Login",command=showId,activebackground = "pink", activeforeground = "blue").place(x = 200, y = 50)

username = Label(root, text = "Username").place(x = 30,y = 100)  
ID = Label(root, text = "ID")  

e1 = Entry(root,width = 20).place(x = 120, y = 100)  
e2 = Entry(root, width = 20)

Submit=Button(root,text="Submit",activebackground="pink",activeforeground="blue").place(x=150,y=160)
root.configure(bg='light blue')

root.mainloop()