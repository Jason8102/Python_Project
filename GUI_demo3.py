from tkinter import *
from tkmacosx import *
root = Tk()
root.minsize(height=480,width=800)

# def tab1():
#     def tab2():
#         label1.destroy()
#         button1.destroy()
#         label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
#         label2.pack()
#         def back():
#             label2.destroy()
#             button2.destroy()
#             tab1()

#         button2 = Button(root,text="Back",font=("Times_New_Roman",25),command=back,activebackground="red")
#         button2.pack(side=BOTTOM)
        

#     label1 = Label(root,text="This is First Tab",font=("Times_New_Roman",25))
#     label1.pack()
#     button1 = Button(root,text="NEXT",font=("Times_New_Roman",25),command= tab2,activebackground="blue")
#     button1.pack(side=BOTTOM)
# tab1()

def tab1(): #first page destroy
    label1.destroy()
    button1.destroy()
    button2.destroy()
    

def tab2():#second page
    tab1()
    global label2
    label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    label2.pack()
    global button_1
    button_1 = Button(root,text="BACK_2",font=("Times_New_Roman",25),activebackground="yellow",command=back)
    button_1.pack(side=LEFT) 
    global button_2
    button_2 = Button(root,text="NEXT_2",font=("Times_New_Roman",25),activebackground="green",command= tab1)
    button_2.pack(side=RIGHT) 
    

def back(): #second page destroy
    label2.destroy()
    button_1.destroy()
    button_2.destroy()
    tab0()

def tab0(): # first page
    global label1
    label1 = Label(root,text="This is First Tab",font=("Times_New_Roman",25))
    label1.pack(side=TOP)
    global button1
    button1 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue")
    button1.pack(side=LEFT) 
    global button2
    button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red",command= tab2)
    button2.pack(side=RIGHT) 

def tab3():
    global label1
    label1 = Label(root,text="This is First Tab",font=("Times_New_Roman",25))
    label1.pack(side=TOP)
    global button1
    button1 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue")
    button1.pack(side=LEFT) 
    global button2
    button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red",command= tab2)
    button2.pack(side=RIGHT) 

#def tab2():
    # label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    # label2.pack()
    # button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red")
    # button2.pack(side=RIGHT) 


tab0()
#tab2()

root.mainloop()