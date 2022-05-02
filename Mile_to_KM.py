import tkinter

window = tkinter.Tk()
window.title("MILE TO KM")
window.minsize(width=320, height=180)
window.config(padx=30, pady=30)

def mile_km():
    input = entry.get()
    output = float(input) * 1.6
    output1 = round(output, 3)
    return label4.config(text=f"{output1}")


label1 = tkinter.Label(text="Miles")
label2 = tkinter.Label(text="is equal to")
label3 = tkinter.Label(text="Km")
label1.grid(column=4, row=8)
label2.grid(column=1, row=12)
label3.grid(column=4, row=12)

entry = tkinter.Entry(width=6)
entry.grid(column=3, row=8)

button = tkinter.Button(text="Calculate", command=mile_km)
button.grid(column=3, row=16)
label4 = tkinter.Label()
label4.grid(column=3, row=12)









window.mainloop()