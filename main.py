import tkinter

window = tkinter.Tk()
window.title("FIRST GUI PROGRAM")
window.minsize(width=420, height=350)
window.config(padx= 30,pady= 30)


my_label = tkinter.Label(text="This is a text", font=("Arial", 27))
my_label.grid(column=0, row=0)


my_entry = tkinter.Entry(width=10)
my_entry.grid(column=3, row=3)




def button_clicked():
    input = my_entry.get()
    return my_label.config(text=f'{input}')

my_button = tkinter.Button(text='Click Me',command=button_clicked)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text='Hi')
new_button.grid(column=0, row=2)



















window.mainloop()