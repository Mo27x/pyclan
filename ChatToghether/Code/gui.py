from tkinter import *

root=Tk()
root.title("Chat Together")
root.geometry("700x500")

Label1=Label(root,text="Inserisci l'username")
Label2=Label(root,text="Inserisci la password")
Label1.grid(row=0,column=0,pady=20,padx=20)
Label2.grid(row=0,column=1,pady=20,padx=20)

for x in range(2):
    my_entry=Entry(root)
    my_entry.grid(row=1,column=x,pady=20,padx=5)
    
Button1=Button(root,text="Login")
Button1.grid(row=2,column=0,pady=20)

root.configure(bg='light blue')

root.mainloop()