from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.604
    output.config(text=km)

window = Tk()
# window.minsize(350, 150)
window.title("My first GUI program.")
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(row=0, column=1)

Miles = Label(text="Miles")
Miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

output = Label(text='0')
output.grid(row=1, column=1)

kilometer = Label(text="km")
kilometer.grid(row=1, column=2)

button = Button(text="Convert", command=miles_to_km)
button.grid(row=2, column=1)

# # def button_clicked():
# #     # print("I got clicked.")
# #     my_label.config(text="I got clicked")
#


# def entries():
#     print(input)
#


window.mainloop()