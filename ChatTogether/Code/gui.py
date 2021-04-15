from tkinter import *

root=Tk()
root.title("Chat Together")
root.geometry("700x500")

app_width=1000
app_height=500

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

Label1=Label(root,text="Insert your username")
Label2=Label(root,text="Insert your ID")
Label1.grid(row=0,column=0,pady=20,padx=20)
Label2.grid(row=0,column=1,pady=20,padx=20)

for x in range(2):
    my_entry=Entry(root)
    my_entry.grid(row=1,column=x,pady=20,padx=5)
    
Button1=Button(root,text="Login")
Button1.grid(row=2,column=0,pady=20)

root.configure(bg='light blue')

root.mainloop()