from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image

class login_system():
    def __init__(self,window):
        self.window= window
        self.window.title("Sistema de Ingreso")
        self.window.geometry("1350x700+0+0") #+0+0 es la ubicación 0,0
        
        #Images
        img_logo=Image.open("user.png").resize((150,150))
        img = Image.open("usuario.png").resize((50, 50)) 
        img_password=Image.open("password_1.png").resize((50, 50))     
        self.background= ImageTk.PhotoImage(file="./wh.jpg")
        self.user_icon= ImageTk.PhotoImage(img)
        self.password_icon=ImageTk.PhotoImage(img_password)
        self.logo_icon=ImageTk.PhotoImage(img_logo)

        #Variables a usar        
        self.user_name=StringVar()
        self.pass_word=StringVar()
        
        self.fun_tk()
        
    def fun_tk(self):
        
        background_label=Label(self.window,image=self.background).pack()
        
        title=Label(self.window,text="Sistema de Ingreso",font=("Arial",40,"bold"),bg='blue',
                    fg='white', relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        Login_Frame=Frame(self.window,bg="gray")
        Login_Frame.place(x=400, y=150)
        
        Logo_label=Label(Login_Frame, image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
       
        Logo_user=Label(Login_Frame, text="Usuario   ",image=self.user_icon, compound=LEFT, 
                        font=("Arial",20,"bold"),bg="gray").grid(row=1,column=0,padx=20,pady=10)
        
        txt_user=Entry(Login_Frame,textvariable=self.user_name, bd=5, relief=GROOVE,
                       font=("Arial",15)).grid(row=1,column=1,padx=20)
        
        Logo_password=Label(Login_Frame, text="Contraseña",image=self.password_icon, 
                            compound=LEFT, font=("Arial",20,"bold"),
                            bg="gray").grid(row=2,column=0,padx=20,pady=10)
        
        txt_password=Entry(Login_Frame,textvariable=self.pass_word, show="*",
                           bd=5,relief=GROOVE,font=("Arial",15)).grid(row=2,column=1,padx=20)
        
        button= Button(Login_Frame,text="Ingresar", command=self.login, 
                       width=15,font=("Arial",14,"bold"),bg="blue",
                       fg="white").grid(row=3,column=1,pady=10)
        
    def login(self):
        if self.user_name.get()=="" or self.pass_word.get()=="":
            messagebox.showerror("Error","Todos los campos son requeridos")
        elif self.user_name.get().isalpha() and self.pass_word.get().isnumeric():
            messagebox.showinfo("Ingreso exitoso",f"Bienvenid@ {self.user_name.get()}")
        else:
            messagebox.showerror("Error","Usuario o Contraseña inconrrecta")   
            
window=Tk()
objeto=login_system(window)
window.mainloop() 
