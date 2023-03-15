# 1.
#import tkinter
#top = tkinter.Tk()
#top.mainloop()

#2.
from contextlib import redirect_stderr
from tkinter import *
from tkmacosx import * # in macosx system need to import tkmacosx to show "background"
root = Tk()

root.title("This Group B Project") #creat title (not in the screen ,above the screen)
root.iconbitmap("Tatice-Cristal-Intense-Apple-multicolor.ico")#the image cant be showed like this way , i dont know why..
root.geometry("500x400")#control the whole screen size widexhigh
#=========== Radiobutton
# product = [

#     ("Microsoft Surface","Microsoft Surface 1"),
#     ("Google Piexl","Google Piexl 2"),
#     ("Asus RoG","Asus RoG 3"),
#     ("Macbook pro","Macbook pro 4"),
#     ("HP OMEN x","HP OMEN x 5"),
#     ("lenove ai","lenove ai 6")

# ]
# choise = StringVar()
# choise.set("Microsoft Surface")

# for text1,mode in product:
#     Radiobutton(root,text = text1, variable = choise, value = mode).pack(anchor='w')

# def clicked(value):
#     my_label = Label(root,text=value)
#     my_label.pack()

# my_button4 = Button(root, text = "submit",command = lambda: clicked(choise.get()))
# my_button4.pack()

#====================
# q = IntVar()
# q.get()
# q.set("2")

# #my_label = Label(root, text= "hello World this is test XXXXXXXXXXX").grid(row= 0,column= 0)
# my_label2 = Label(root, text= "how you doing today?") #pack or grid. just use one 
# #my_label3 = Label(root,text="This is label3.")
# #my_label4 = Label(root,text="This is label4")
# # my_label.pack()
# my_label2.pack() #can write after the lable
# #my_label.grid(row=0,column=0)
# #my_label3.grid(row=1,column=1)
# #my_label4.grid(row=1,column=2)
# def my_click():
#     my_label5 = Label(root,text= "Welcom to the GroupB!!!",fg="#3371FF")
#     #my_label5.grid(row=5, column=2)
#     my_label5.pack()
   
# mybutton = Button(root,text="Click this to submit!",command= my_click,fg= "green",bg="#00BFFF",padx= 30,pady= 40)
# # mybutton.borderless = 1
# #mybutton.config(background="red")
# #activeforeground when you press a button, the colour showing / activebackground backroung colour
# mybutton.pack()
# #mybutton.grid(row=3,column=2)
# e = Entry(root, width= 50, fg="red")#in put text fg = textcolor
# e.pack()

# def clickme():
#     mylabel6 = Label(root,text= "Hello"+e.get())
#     mylabel6.pack()

# mybutton2 = Button(root,text= "Enter your name",padx=10, pady=20,bg="white",fg="green",command=clickme)# important do not add () after funcation ,like clickme,not clickme()
# mybutton2.pack()

# def click_label7(value):
#     my_label = Label(root,text= value)
#     my_label.pack()
    
    

# Radiobutton(root,text = "option 1",variable = q, value = 1).pack(anchor ="w")
# Radiobutton(root,text = "option 2",variable = q, value = 2).pack(anchor ="n")
# Radiobutton(root,text = "option 3",variable = q, value = 3).pack(anchor ="e")
# Radiobutton(root,text = "option 4",variable = q, value = 4).pack(anchor ="s")

# my_label7 = Label(root,text= q.get())
# my_label7.pack()

# my_button3 = Button(root, text = "submit",command = lambda: click_label7(q.get())) #important:q.get() imstead of q.get!!!!
# my_button3.pack()

#================ drop
# def open():
#     my_label = Label(root,text= clicked.get())
#     my_label.grid(row=2, column=2, padx=10,pady=10,ipadx=30)
# options = [
#     "iPhone XR",
#     "iPhone SE",
#     "iPhone X",
#     "iPhone X MAX",
#     "Google Pixel",

# ]
# clicked = StringVar()
# clicked.set(options[0])

# drop = OptionMenu(root, clicked,*options)
# drop.grid(row=0 , column=1,padx=10, pady=10)


# my_button = Button(root,text = "Submit",command = open)
# my_button.grid(row=0 , column=2,padx=10, pady=10)

#================ labelframe
# frame = LabelFrame(root,text="This is a frame !",padx=100,pady=100)
# frame.grid(padx=20,pady=20)

# def myclick():
#     label1 = Label(frame,text="Hello User!",fg="blue")
#     label1.grid(row=10,column=10)

# b1 = Button(frame,text= "click me",command =myclick)
# b1.grid(row=0,column=1)

# c = Button(frame,text= "Exit",command= root.quit)
# c.grid(row=0,column=3)



#=================



#===============

root.mainloop()