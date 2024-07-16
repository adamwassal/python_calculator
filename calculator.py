# import all libraries
from tkinter import *
from tkinter import Entry
import math
import numpy as np
# --------------------

# make window
root = Tk()
root.title("adam4.0")
root.geometry("570x520")
# --------------------

# functions

# add to entry
def addEntry(ch):
    e.insert(20, ch)

# equal button
def calculatorEntry():
    try:
        expression_e = e.get()
        expression = eval(expression_e)
        e.delete(0, END)
        e.insert(20, expression)
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")


# press on enter to calculate
def calculator_Entry_enter(event):
    try:
        expression_e = e.get()
        expression = eval(expression_e)
        e.delete(0, END)
        e.insert(20, expression)
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")


# clear all in entry
def clear():
    e.delete(0, END)

# delete one number from entry
def clear_number_one():
    length = len(e.get())
    e.delete(length-1, "end")

# turn off app
def close():
    root.destroy()

# sine button
def sin():
    try:
        number = float(e.get())
        result = math.sin(number)
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")

# cosine button
def cos():
    try:
        number = float(e.get())
        result= math.cos(number)
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")

# tan button
def tan():
    try:
        number = float(e.get())
        result= math.tan(number)
        e.delete(0, END)
        e.insert(0, result)

    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")

# square root button
def square_root():
    try:
        result = float(e.get())
        e.delete(0, END)
        e.insert(0, float(math.sqrt(result)))
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")

# cube root button
def cube_root():
    try:
        result = float(e.get())
        e.delete(0, END)
        e.insert(0, float(np.cbrt(result)))
    except:
        e.delete(0, END)
        e.insert(0, "Math Error Press (cl)")

# power number of 2
def power_2():
    result = int(np.power(int(e.get()), 2))
    e.delete(0,END)
    e.insert(0, result)

# power number of 3
def power_3():
    result = int(np.power(int(e.get()), 3))
    e.delete(0, END)
    e.insert(0, result)

# power number of choose number
def choose_power():
    # make power number window
    power= Tk()
    power.title("Power number of number")

    # turn off power window
    def close_power():
        power.destroy()

    # power calculate button
    def power_cal():
        # main variables on the function
        base_num= int(e.get())
        power_num = int(e_p_n.get())
        result= pow(base_num, power_num)

        # delete all from all entry
        e_p_n.delete(0, END)
        e.delete(0, END)

        # insert result
        e_p_n.insert(20, result)
        e.insert(20, result)
        
        power.destroy()

    # title of the base number entry
    label_power_num = Label(power, text="Power number:", bg="darkred", fg="white", font=("Arial", 14, "bold"))
    label_power_num.grid(row=2, column=0, pady=10)

    # power number entry
    e_p_n: Entry = Entry(power, width=50, font=("Arial", 14, "bold"), justify="left", bg="white", fg="black", border=8.2)
    e_p_n.grid(row=2, column=2, columnspan=4, pady=5)

    # power calculate button
    button_power = Button(power, text="Calculate", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2",command=lambda: power_cal())
    button_power.grid(row=3, column=3, pady=10)

    # turn off button
    button_exit = Button(power, text="Exit power", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"),cursor="hand2", command=lambda: close_power())
    button_exit.grid(row=4, column=4, pady=10)


# about button
def about():
    # make about window
    about= Tk()
    about.title("About")
    about.geometry("650x260")

    # Dev_name label
    label=Label(about, text="Developer_Name: Adam wael |", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, pady=10)

    # calculator_name label
    label2 = Label(about, text="Calculator_Name: adam |", font=("Arial", 14, "bold"))
    label2.grid(row=0, column=4, pady=10)

    # version label
    label3 = Label(about, text="Version: 4.0 |", font=("Arial", 14, "bold"))
    label3.grid(row=1, column=0, pady=10)

    # last_update label
    label4 = Label(about, text="Last_updates: 28/2/2023 |", font=("Arial", 14, "bold"))
    label4.grid(row=1, column=4, pady=10)

    # language_programming label
    label5 = Label(about, text="language_programming: Python |", font=("Arial", 14, "bold"))
    label5.grid(row=2, column=0, pady=10)

    # made_in label
    label6 = Label(about, text="Made_in: (1)Year |", font=("Arial", 14, "bold"))
    label6.grid(row=2, column=4, pady=10)

    # Dev_age label
    label7 = Label(about, text="Dev_age: 14 |", font=("Arial", 14, "bold"))
    label7.grid(row=3, column=0, pady=10)

    # os label
    label8 = Label(about, text="os: Linux |", font=("Arial", 14, "bold"))
    label8.grid(row=3, column=4, pady=10)

    # turn off about window function
    def turn_off():
        about.destroy()

    # turn off button
    button=Button(about, text="OK",font=("Arial", 14, "bold"),cursor="hand2", command=lambda: turn_off())
    button.grid(row=4, column=3, pady=10)
# -----------End all function---------------

# make main Entry box
e: Entry = Entry(root, width=50, font=("Arial", 14, "bold"), justify="left", bg="white", fg="black", border=8.2)
e.grid(row=0, column=0, columnspan=4, pady=5)
e.bind("<Return>", calculator_Entry_enter)


# make buttons
# zero number button
button0 = Button(root, text="0", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(0))
button0.grid(row=5, column=0, pady=10)

# dote button
button_dote = Button(root, text=".", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("."))
button_dote.grid(row=5, column=1, pady=10)

# all clear button
button_clear = Button(root, text="AC", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: clear())
button_clear.grid(row=1, column=0, pady=10)

# Def button
button_on=Button(root, text="/",width=10, bg="green", fg="black",font=("Arial", 14, "bold"),cursor="hand2", command=lambda: addEntry("/"))
button_on.grid(row=5, column=3, pady=10)

# one number button
button1 = Button(root, text="1", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(1))
button1.grid(row=4, column=0, pady=10)

# two number button
button2 = Button(root, text="2", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(2))
button2.grid(row=4, column=1, pady=10)

# three number button
button3 = Button(root, text="3", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(3))
button3.grid(row=4, column=2, pady=10)

# plus button
button_plus = Button(root, text="+", width=10, bg="green", fg="black", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("+"))
button_plus.grid(row=4, column=3, pady=10)

# four number button
button4 = Button(root, text="4", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(4))
button4.grid(row=3, column=0, pady=10)

# five number button
button5 = Button(root, text="5", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(5))
button5.grid(row=3, column=1, pady=10)

# six number button
button6 = Button(root, text="6", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(6))
button6.grid(row=3, column=2, pady=10)

# minus button
button_minus = Button(root, text="-", width=10, bg="green", fg="black", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("-"))
button_minus.grid(row=3, column=3, pady=10)

# seven number button
button7 = Button(root, text="7", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(7))
button7.grid(row=2, column=0, pady=10)

# eight number button
button8 = Button(root, text="8", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(8))
button8.grid(row=2, column=1, pady=10)

# nine number button
button9 = Button(root, text="9", width=10, bg="darkred", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(9))
button9.grid(row=2, column=2, pady=10)

# multi button
button_in = Button(root, text="x", width=10, bg="green", fg="black", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("*"))
button_in.grid(row=2, column=3, pady=10)

# turn off button
button_close = Button(root, text="off", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=close)
button_close.grid(row=1, column=3, pady=10)

# equal button
button_equal = Button(root, text="=", width=10, bg="darkorange", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: calculatorEntry())
button_equal.grid(row=7, column=3, pady=10)

# ( button
button_qw = Button(root, text="(", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("("))
button_qw.grid(row=7, column=0, pady=10)

# ) button
button_wq = Button(root, text=")", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry(")"))
button_wq.grid(row=7, column=1, pady=10)

# % button
button_ih = Button(root, text="%", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: addEntry("%"))
button_ih.grid(row=7, column=2, pady=10)

# delete button
button_clear_number_one = Button(root, text="DEL", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: clear_number_one())
button_clear_number_one.grid(row=5, column=2, pady=10)

# square root button
button_square_root = Button(root, text="√", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: square_root())
button_square_root.grid(row=8, column=3, pady=10)

# cube root button
button_cube_root = Button(root, text="√3", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: cube_root())
button_cube_root.grid(row=9, column=3, pady=10)

# power number of 2 button
button_os2=Button(root, text="x²",width=10, bg="darkblue", fg="white",font=("Arial", 14, "bold"),cursor="hand2", command=lambda: power_2())
button_os2.grid(row=8, column=0, pady=10)

# power number of 3 button
button_os3=Button(root, text="x3",width=10, bg="darkblue", fg="white",font=("Arial", 14, "bold"),cursor="hand2", command=lambda: power_3())
button_os3.grid(row=8, column=1, pady=10)

# power number of choose number button
button_os_=Button(root, text="x^",width=10, bg="darkblue", fg="white",font=("Arial", 14, "bold"),cursor="hand2", command=lambda: choose_power())
button_os_.grid(row=8, column=2, pady=10)

# about button
button_about_ = Button(root, text="About",width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: about())
button_about_.grid(row=1, column=2, pady=10)

# sine button
button_sin_ = Button(root, text="sin", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: sin())
button_sin_.grid(row=9, column=0, pady=10)

# cosine button
button_cos_ = Button(root, text="cos", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: cos())
button_cos_.grid(row=9, column=1, pady=10)

# tan button
button_tan_ = Button(root, text="tan", width=10, bg="darkblue", fg="white", font=("Arial", 14, "bold"), cursor="hand2", command=lambda: tan())
button_tan_.grid(row=9, column=2, pady=10)


# start calculator
root.mainloop()
