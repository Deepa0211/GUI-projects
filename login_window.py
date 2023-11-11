# importing all required modules
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox # to print a message for success of login or not 

# function for logging in the login window
def login():
    email = email_input.get()
    password = password_input.get()
    if email == "classroom@gmail.com" and password == "12345":
        messagebox.showinfo("Login Sunccessful")
    else:
        messagebox.showerror("Login Failed")
        
# for creating login window
root = Tk()

root.title("Login Form")

# specify the proper width and height of the window 
root.geometry("350x550") 

root.configure(background="#0078CD")

# inserting image in the window
img = Image.open("flipkart.jpeg")
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(20, 20))

# writing text 
text_label = Label(root, text = "Flipkart", fg = "yellow", bg = "#0078CD")
text_label.pack()
text_label.config(font=("Poppins", 28))

# creating a label for specifying email
email_label = Label(root, text = "Enter your email", bg = "#0078CD")
email_label.pack(pady=(20, 20))
email_label.config(font=("Poppins", 12))

email_input = Entry(root, width = 50)
email_input.pack(ipady=6, pady=(1, 10))

# creating a label for specifying password
password_label = Label(root, text = "Enter your password", bg = "#0078CD")
password_label.pack(pady=(20, 20))
password_label.config(font=("Poppins", 12))

password_input = Entry(root, width = 50)
password_input.pack(ipady=6, pady=(1, 10))

# creating a button for entering the details of the user
login_button = Button(root, text="Login Here", bg="white", fg="black", width= 10, height = 2, command=login)
login_button.config(font=("Poppins", 12))
login_button.pack(pady=(20, 20))

# for displaying the login window
root.mainloop()