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
def tab1(): 
    label1.destroy()
    button1.destroy()
    button2.destroy()
    tab2()

def tab2():
    label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    label2.pack()
    button_1 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue", commond =back)
    button_1.pack(side=LEFT) 
    button_2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red",command= tab1)
    button_2.pack(side=RIGHT) 
    

    def back():
        label2.destroy()
        button_1.destroy()
        button_2.destroy()
        tab1()

label1 = Label(root,text="This is First Tab",font=("Times_New_Roman",25))
label1.pack(side=TOP)
button1 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue")
button1.pack(side=LEFT) 
button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red",command= tab2)
button2.pack(side=RIGHT) 


#def tab2():
    # label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    # label2.pack()
    # button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red")
    # button2.pack(side=RIGHT) 


#tab1()
#tab2()

root.mainloop()