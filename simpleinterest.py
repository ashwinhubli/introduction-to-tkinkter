from time import time
from tkinter import *
window = Tk()



window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')



def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    msg = ""

    output_message = Label(result_frame, text=", your Str interest is "+str(interest) , bg="lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()


app_label = Label(window, text="Interest CALCULATOR", fg="black",
                  bg="lightcyan", font=("Calibri", 20), bd=5)
app_label.place(x=50, y=20)

name_label = Label(window, text="Rate of Interest", fg="black",
                   bg="lightcyan", font=("Calibri", 12), bd=1)
name_label.place(x=20, y=90)

principle_label = Label(window, text="Principal Amount", fg="black",
                   bg="lightcyan", font=("Calibri", 12), bd=1)
principle_label.place(x=20, y=90)

principle = Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)

time_label = Label(window, text="Enter time",
                     fg="black", bg="lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=140)

time = Entry(window, text="", bd=2, width=15)
time.place(x=150, y=142)

rateofinterest_label = Label(window, text="rate of interest",
                     fg="black", bg="lightcyan", font=("Calibri", 12))
rateofinterest_label.place(x=20, y=185)

rate = Entry(window, text="", bd=2, width=15)
rate.place(x=150, y=187)

calculate_button = Button(window, text="Calculate",
                          fg="black", bg="cyan", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Result",
                          bg="grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label = Label(result_frame, text=" ", bg="lightcyan",
                     font=("Calibri", 12), width=33)
result_label.place(x=20, y=20)
result_label.pack()


window.mainloop()
