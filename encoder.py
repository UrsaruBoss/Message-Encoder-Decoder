from tkinter import *
import customtkinter
import base64

customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.geometry('800x400')
root.resizable(0,0)
root.title("Message Encoder/Decoder")

customtkinter.CTkLabel(root, text ='Message Encoder/Decoder', font =('Agency FB', 48)).pack()

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid')

def Copy():
        root.clipboard_clear()
        root.clipboard_append(str(Result))

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


message = customtkinter.CTkLabel(root, text='MESSAGE', font =('Agency FB', 24)).place(x= 60,y=80)
customtkinter.CTkEntry(root, textvariable = Text, width=500).place(x=290, y = 80)
key = customtkinter.CTkLabel(root, text ='KEY', font =('Agency FB', 24)).place(x=60, y = 125)
customtkinter.CTkEntry(root, textvariable = private_key).place(x=290, y = 125)
encode = customtkinter.CTkRadioButton(master=root, text="Encode",
                                             command=Mode, variable= mode, value="e", font =('Agency FB', 24)).place(x=60, y=175)
decode = customtkinter.CTkRadioButton(master=root, text="Decode",
                                             command=Mode, variable= mode, value="d", font =('Agency FB', 24)).place(x=290, y=175)
encode_decode = customtkinter.CTkEntry(root, textvariable = Result, width=500).place(x=290, y = 250)
copy = customtkinter.CTkButton(root, text = 'COPY',command = Copy, font =('Agency FB', 24), fg_color="dark blue").place(x=640, y = 300)
convert = customtkinter.CTkButton(root, text = 'CONVERT',command = Mode, font =('Agency FB', 24), fg_color="green").place(x=60, y = 250)
reset = customtkinter.CTkButton(root, text ='RESET' ,width =6, command = Reset, font =('Agency FB', 24), fg_color="dark red").place(x=60, y = 350)
exit = customtkinter.CTkButton(root, text= 'EXIT' , width = 6, command = Exit, font =('Agency FB', 24), fg_color="red").place(x=180, y = 350)
root.mainloop()