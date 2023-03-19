from tkinter import *
from tkmacosx import *
root = Tk()
root.title("This Group B Project")
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

def back0():
    label0.destroy()
    button0.destroy()
    button_0.destroy()
    

def back0_0():
    label0.destroy()
    button0.destroy()
    button_0.destroy()
    tab0()

def tab0(): # home page
    global label0
    label0 = Label(root,text="Choose Record or Listerning",font=("Times_New_Roman",25))
    label0.pack(side=TOP)
    global button0
    button0 = Button(root,text="Record",font=("Times_New_Roman",50),activebackground="blue",height= 500, width=500,command=tab1)
    button0.pack(side=LEFT) 
    global button_0
    button_0 = Button(root,text="Listern",font=("Times_New_Roman",50),activebackground="red",height= 500,width=500,command=tab_listern_1)
    button_0.pack(side=RIGHT) 

def back_listerning_back_1():
    label9.destroy()
    button_3.destroy()
    button_4.destroy()
    tab0()

def tab_listern_1():#listern page
    back0()
    global label9
    label9 = Label(root,text="This is Listering Tab",font=("Times_New_Roman",25))
    label9.pack(side=TOP)
    global button_3
    button_3 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue",height= 50, width=100,command=back_listerning_back_1)
    button_3.pack(side=TOP) 
    button_3.place(x=10,y=10)
    global button_4
    button_4 = Button(root,text="Choose",font=("Times_New_Roman",25),activebackground="red",height= 50, width=100)
    button_4.pack(side=BOTTOM) 


def back01(): #first page destroy
    label1.destroy()
    button1.destroy()
    button2.destroy()

def back01_01(): #first page destroy
    label1.destroy()
    button1.destroy()
    button2.destroy()
    tab0()
    

def tab2():#second page
    back01()
    global label2
    label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    label2.pack()
    global button_1
    button_1 = Button(root,text="BACK_2",font=("Times_New_Roman",25),activebackground="yellow",command=back02)
    button_1.pack(side=LEFT) 
    global button_2
    button_2 = Button(root,text="NEXT_2",font=("Times_New_Roman",25),activebackground="green",command= tab3)
    button_2.pack(side=RIGHT) 
    

def back02(): #second page destroy and rebuild tab1
    label2.destroy()
    button_1.destroy()
    button_2.destroy()
    tab1()

def back02_1(): #second page destroy
    label2.destroy()
    button_1.destroy()
    button_2.destroy()

def tab1(): # first page
    back0()
    global label1
    label1 = Label(root,text="This is First Tab",font=("Times_New_Roman",25))
    label1.pack(side=TOP)
    global button1
    button1 = Button(root,text="BACK",font=("Times_New_Roman",25),activebackground="blue",height= 50, width=100,command=back01_01)
    button1.pack(side=LEFT) 
    global button2
    button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red",command= tab2)
    button2.pack(side=RIGHT) 

def tab3():# third page
    back02_1()
    global label3
    label3 = Label(root,text="This is thrid Tab",font=("Times_New_Roman",25))
    label3.pack(side=TOP)
    global button3
    button3 = Button(root,text="BACK_3",font=("Times_New_Roman",25),activebackground="blue",command=back03)
    button3.pack(side=LEFT) 
    global button4
    button4 = Button(root,text="NEXT_3",font=("Times_New_Roman",25),activebackground="red",command=tab4)
    button4.pack(side=RIGHT) 

def back03():
    label3.destroy()
    button3.destroy()
    button4.destroy()
    tab2()

def back03_1():
    label3.destroy()
    button3.destroy()
    button4.destroy()

def tab4():
    back03_1()
    global label4
    label4 = Label(root,text="This is fourth Tab",font=("Times_New_Roman",25))
    label4.pack(side=TOP)
    global button4
    button4 = Button(root,text="BACK_4",font=("Times_New_Roman",25),activebackground="yellow",command=back04)
    button4.pack(side=LEFT) 
    global button5
    button5 = Button(root,text="NEXT_4",font=("Times_New_Roman",25),activebackground="green",command=tab5)
    button5.pack(side=RIGHT) 

def back04():
    label4.destroy()
    button4.destroy()
    button5.destroy()
    tab3()

def back04_1():
    label4.destroy()
    button4.destroy()
    button5.destroy()

def tab5():
    back04_1()
    global label5
    label5 = Label(root,text="This is Fifth Tab",font=("Times_New_Roman",25))
    label5.pack(side=TOP)
    global button6
    button6 = Button(root,text="BACK_5",font=("Times_New_Roman",25),activebackground="yellow",command=back05)
    button6.pack(side=LEFT) 
    global button7
    button7 = Button(root,text="NEXT_5",font=("Times_New_Roman",25),activebackground="green",command= tab6)
    button7.pack(side=RIGHT) 

def back05():
    label5.destroy()
    button6.destroy()
    button7.destroy()
    tab4()

def back05_1():
    label5.destroy()
    button6.destroy()
    button7.destroy()

def tab6():
    back05_1()
    global label6
    label6 = Label(root,text="This is Sixth Tab",font=("Times_New_Roman",25))
    label6.pack(side=TOP)
    global button8
    button8 = Button(root,text="BACK_6",font=("Times_New_Roman",25),activebackground="yellow",command=back06)
    button8.pack(side=LEFT) 
    global button9
    button9 = Button(root,text="NEXT_6",font=("Times_New_Roman",25),activebackground="green",command=tab7)
    button9.pack(side=RIGHT)

def back06():
    label6.destroy()
    button8.destroy()
    button9.destroy()
    tab5()

def back06_1():
    label6.destroy()
    button8.destroy()
    button9.destroy()

def tab7():
    back06_1()
    global label7
    label7 = Label(root,text="This is Seventh Tab",font=("Times_New_Roman",25))
    label7.pack(side=TOP)
    global button10
    button10 = Button(root,text="BACK_7",font=("Times_New_Roman",25),activebackground="red",command=back07)
    button10.pack(side=LEFT) 
    global button11
    button11 = Button(root,text="NEXT_7",font=("Times_New_Roman",25),activebackground="green",command=tab8)
    button11.pack(side=RIGHT)

def back07():
    label7.destroy()
    button10.destroy()
    button11.destroy()
    tab6()

def back07_1():
    label7.destroy()
    button10.destroy()
    button11.destroy()

def tab8():
    back07_1()
    global label8
    label8 = Label(root,text="This is Eighth Tab",font=("Times_New_Roman",25))
    label8.pack(side=TOP)
    global button12
    button12 = Button(root,text="BACK_8(Submit)",font=("Times_New_Roman",25),activebackground="red",command=back08)
    button12.pack(side=BOTTOM) 

def back08():
    label8.destroy()
    button12.destroy()
    tab7()
 







#def tab4():

#def tab2():
    # label2 = Label(root,text="This is Second Tab",font=("Times_New_Roman",25))
    # label2.pack()
    # button2 = Button(root,text="NEXT",font=("Times_New_Roman",25),activebackground="red")
    # button2.pack(side=RIGHT) 

tab0()
#tab1()


root.mainloop()