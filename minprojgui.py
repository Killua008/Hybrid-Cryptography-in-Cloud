from tkinter import*
from tkinter import messagebox
#from aestrial import*
#from destrial import*
#from Stegano import*
from tkinter import filedialog as fd
from aesfileenc1 import*
from main import*
from hybrid1 import*
#from decrypt import*
from tkinter.ttk import Progressbar
import time

root=Tk()
root.title("CC")

Label0=Label(root,text="AES Encryption")
Label0.grid(row=1,column=1)


Label1=Label(root,text="Enter Bucket Name : ")
Label1.grid(row=2,column=1)

Label2=Label(root,text="Enter Object Name: ")
Label2.grid(row=3,column=1)

Label3=Label(root,text="Enter File Name: ")
Label3.grid(row=4,column=1)


def choose_File():

        #title="Open a file",intialdir="/",
                                    #filetypes=(("text files","*.txt"),("All files","*.*"))
        
        global ufilename
        ufilename=fd.askopenfilename()
        messagebox.showinfo(
            title="Selected  File",message=ufilename)
        

button_0=Button(root,text="Choose File",command=choose_File)
button_0.grid(row=5,column=1)




#Password input field
#passkey="Hello123"

e=Entry(root,width=40,fg="blue",bg="white",borderwidth=10)
e.icursor(0)
e.grid(row=2,column=2)


e1=Entry(root,width=40,fg="black",bg="white",borderwidth=10)
e1.grid(row=3,column=2)

e2=Entry(root,width=40,fg="black",bg="white",borderwidth=10)
e2.grid(row=4,column=2)

    
def myClick():
        file_location=ufilename
        buck=e.get()
        obj=e1.get()
        upload_file(file_location, buck, obj)

        
        messagebox.showinfo("Information","Upload Completed!")
    

Button1=Button(root,text="Upload",padx=50,command=myClick)
Button1.grid(row=6,column=1)

#Since pycryptodome only takes input into string but entry widget takes input has
#string only
#For first we will convert the cipher bytes into string encoding latin-1
#then taking this encoded string as input we will convert it in bytes again
#so in this way we get the input converted into bytes again

def myClick1():
        
        hybrid1.hy()
        
    

Button2=Button(root,text="Mail",padx=50,command=myClick1)
Button2.grid(row=6,column=2)





#plain_text=decrypt(cipher_text,password)
#print(plain_text)



def first():
    top=Toplevel()
    top.title('AES File Encryption')
    label1=Label(top,text="AES Algorithm")
    label1.grid(row=1,column=1)

    
    Label1=Label(top,text="Choose The File for Encryption: ")
    
    Label1.grid(row=3,column=1)

    def select_File():

        #title="Open a file",intialdir="/",
                                    #filetypes=(("text files","*.txt"),("All files","*.*"))
        
        global filename
        filename=fd.askopenfilename()
        messagebox.showinfo(
            title="Selected  File",message=filename)
        

    button_0=Button(top,text="Choose File",command=select_File)
    button_0.grid(row=3,column=2)

    def select_File1():

        #title="Open a file",intialdir="/",
                                    #filetypes=(("text files","*.txt"),("All files","*.*"))
        
        global Ofilename
        Ofilename=fd.askopenfilename()
        messagebox.showinfo(
            title="Selected  File",message=Ofilename)
        
    Label2=Label(top,text="Choose the File to write into : ")
    
    Label2.grid(row=4,column=1)


    button_1=Button(top,text="Choose File for enc and dec",command=select_File1)
    button_1.grid(row=4,column=2)

    Label2=Label(top,text="Enter Password : ")
    
    Label2.grid(row=5,column=1)

    e1=Entry(top,width=40,fg="black",bg="white",borderwidth=10)
    e1.grid(row=5,column=2)


   
    def enc():
        print (filename)
        password=e1.get()
        
        key=getKey(password)
        print(key,filename,Ofilename)
        
        encryptaes(key ,filename,Ofilename)
        """def bar():
            tasks=10
            x=0
            while (x<tasks):
                time.sleep(1)
                progress['value']+=10
                x+=1
                top.update_idletasks()
  
        progress.grid(row=7,column=1)"""
        messagebox.showinfo("Information","Encryption Completed of the File!")
    
    Button0=Button(top,text="Encrypt ",padx=50,command=enc)
    Button0.grid(row=6,column=1)

    def dec():
        print(Ofilename)
        password=e1.get()
        key=getKey(password)
        
        decryptaes(key,filename,Ofilename)
          
        messagebox.showinfo("Information","Decryption Completed of the File!")
    
    Button1=Button(top,text="Decrypt ",padx=50,command=dec)
    Button1.grid(row=6,column=2)


    



    
    return

Label7=Label(root,text="Try AES Algorithm for File encryption -> ")
    
Label7.grid(row=9,column=1)


Button7=Button(root,text="File Encryption ",padx=50,command=first)
Button7.grid(row=9,column=2)


def instruct():
    top=Toplevel()
    top.title('Insturction Manual')
    label1=Label(top,text="AES Algorithm ")
    label1.grid(row=1,column=1)

    label2=Label(top,text="1.Enter the text for encryption in 'Enter the text' \n 2.Enter the Passkey of your preference *Remember your password*\n 3.The encrypted text will appear in the text box.\n 4.For Decryption enter the Cipher text in the text box." )
    label2.grid(row=2,column=1)

    label3=Label(top,text="DES Algorithm ")
    label3.grid(row=3,column=1)

    label4=Label(top,text="1.Enter the text for encryption in 'Enter the text' \n 2.Enter the Passkey of 8 Byte *Remember your password*\n 3.The encrypted text will appear in the text box.\n 4.For Decryption enter the Cipher text in the text box." )
    label4.grid(row=4,column=1)

    label5=Label(top,text="Steganography ")
    label5.grid(row=5,column=1)

    label6=Label(top,text="1.To Encode you must provide the address of the image *Image must be in png format .\n 2.Name and the address to save the new *encoded image must be provided.\n 3.For decoding you must only submit the address of encoded image . ")
    label6.grid(row=6,column=1)

    label7=Label(top,text="AES File Encryption")
    label7.grid(row=7,column=1)


    label8=Label(top,text="1.Select the text file you want to encrypt or decrypt by clicking on 'Choose File' Button.\n 2.After selecting the File you want to encrypt or decrypt,now choose the file you want to write into .\n 3.For decoding or encoding type the KEY of more than *8 Characters* .")
    label8.grid(row=8,column=1)


    
    return
Button0=Button(root,text="Instruction manual",padx=50,command=instruct)
Button0.grid(row=0,column=2)




mainloop()
