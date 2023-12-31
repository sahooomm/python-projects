from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root,width=50,borderwidth=5,bg="white",fg="black")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    
    
def button_clear():
    e.delete(0,END)
    

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "Addition":
        e.insert(0, f_num + float(second_number))
    if math == "Subtract":
        e.insert(0, f_num - float(second_number))
    if math == "Multiply":
        e.insert(0, f_num * float(second_number))
    if math == "Divide":
        e.insert(0, f_num / float(second_number))
    if math == "Modulo":
        e.insert(0, f_num % float(second_number))
    if math == "Resiprocal":
        e.insert(0, 1/float(f_num))
    if math == "sqroot":
        e.insert(0, f_num ** 0.5)
    
    
    
def button_add():
    first_number = e.get()
    global f_num
    global math 
    math = "Addition"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_subtract():
    first_number = e.get()
    global f_num
    global math 
    math = "Subtract"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math 
    math = "Multiply"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_divide():
    first_number = e.get()
    global f_num
    global math 
    math = "Divide"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_modulo():
    first_number = e.get()
    global f_num
    global math
    math = "Modulo"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_reciprocal():
    first_number = e.get()
    global f_num 
    global math
    math = "Resiprocal"
    f_num = float(first_number)
    e.delete(0,END)
    
def button_sqroot():
    first_number = e.get()
    global f_num
    global math
    math = "sqroot"
    f_num = float(first_number)
    e.delete(0,END)
    
    
    
    
button_1 = Button(root,text="1",padx=40,pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2",padx=40,pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3",padx=40,pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4",padx=40,pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5",padx=40,pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6",padx=40,pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7",padx=40,pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8",padx=40,pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40,pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0",padx=40,pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+",padx=39,pady=20, command=button_add).grid(row=5,column=0)
button_clear = Button(root, text="clear",padx=89,pady=20, command=button_clear).grid(row=4,column=1,columnspan=2)
button_equal = Button(root,bg="yellow", text="=",padx=91,pady=20, command=button_equal).grid(row=5,column=1,columnspan=2)

button_subtract = Button(root, text="-",padx=41,pady=20, command=button_subtract).grid(row=6,column=0)
button_multiply = Button(root, text="*",padx=41,pady=20, command=button_multiply).grid(row=6,column=1)
button_divide = Button(root, text="/",padx=41,pady=20, command=button_divide).grid(row=6,column=2)

button_modulo = Button(root, text="%",padx=41,pady=20,command=button_modulo).grid(row=7,column=0)
button_reiprocal = Button(root, text="1/x",padx=41,pady=20,command=button_reciprocal).grid(row=7,column=1)
button_sqroot = Button(root, text="√",padx=41,pady=20,command=button_sqroot).grid(row=7,column=2)
button_decimal = Button(root, text=".",padx=41,pady=20,command=lambda:button_click(".")).grid(row=8,column=0)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_0.grid(row=4,column=0)






#myButton.pack()
root.mainloop()