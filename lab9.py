# Лабораторная работа 9
# Написать программу логинскрин на ткинтере, которая будет в фаил записывать данные новых пользователей
# и читать фаил что бы произвести вход уже зарегестрированного пользователя
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import os

def enter():
    if loginEntry.get() == "":
        errmsg.set("Введите логин")
        return
    if passEntry.get() == "":
        errmsg.set("Введите пароль")
        return
    if not os.path.exists("base.txt"):
        base = open("base.txt","a+")
        base.close()
    base = open("base.txt","r+",encoding="utf-8")
    crypted = crypto(loginEntry.get(),passEntry.get())
    baseList = base.readlines()
    for i in baseList:
        if crypted[0] == i.rstrip() and (baseList.index(i) %2 == 0 or baseList.index(i) == 0):
            if crypted[1] == baseList[baseList.index(i)+1].rstrip():
                messagebox.showinfo("Уведомление","Вы вошли")
                base.close()
                return
            else:
                errmsg.set("Неверный пароль")
                base.close()
                return
    base.write(crypted[0]+"\n")
    base.write(crypted[1]+"\n")
    messagebox.showinfo("Уведомление","Вы успешно зарегистрировались")
    base.close()


def crypto(login,password):
    value = 10
    cryptedLogin = ""
    cryptedPassword = ""
    for i in login:
        cryptedLogin = cryptedLogin + chr(ord(i)+value)
    for j in password:
        cryptedPassword = cryptedPassword + chr(ord(i)+value)
    return cryptedLogin, cryptedPassword


def passvalid(newval):
    res = re.match("[a-zA-Z0-9_-]{,20}$",newval) is not None
    if not res:
        errmsg.set("Вы можете использовать только символы английского алфавита, цифры, а так же _ и - при вводе пароля, длинна должна быть не больше 20 символов")
    else:
        errmsg.set("")
    return res


def logvalid(newval):
    res = re.match("[a-zA-Z0-9]{,20}$",newval) is not None
    if not res:
        errmsg.set("Вы можете использовать только символы английского алфавита и цифры при вводе логина, длинна должна быть не больше 20 символов")
    else:
        errmsg.set("")
    return res


mainWindow = Tk()
mainWindow.title("lab9")
mainWindow.geometry("600x400")
checkLogin = (mainWindow.register(logvalid),"%P")
checkPass = (mainWindow.register(passvalid),"%P")
label1 = Label(mainWindow,text="Введите логин и пароль:")
label2 = Label(mainWindow,text="Логин:")
label3 = Label(mainWindow,text="Пароль:")
errmsg = StringVar()
errLabel = Label(mainWindow,foreground="red",textvariable=errmsg,wraplength=250)
loginEntry = Entry(mainWindow,width=40,validate="key",validatecommand=checkLogin)
passEntry = Entry(mainWindow,width=40,validate="key",validatecommand=checkPass)
enterButton = ttk.Button(mainWindow,text="Ввод",command=lambda :enter())
label1.pack(anchor="n")
label2.place(anchor="nw",relx=0.22,rely=0.045)
label3.place(anchor="nw",relx=0.21,rely=0.12)
loginEntry.pack(anchor="n")
passEntry.pack(anchor="n",pady=10)
enterButton.pack(anchor="n")
errLabel.pack(anchor="n")
mainWindow.mainloop()
