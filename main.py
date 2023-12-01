import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

def convert():
    miles = int(t_input.get())
    km = round(miles * 1.609, 3)
    result.config(text=km)

# Entry

t_input = tkinter.Entry(width=10)
t_input.grid(column=1, row=0)

# Label
is_equal_to = tkinter.Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

miles = tkinter.Label(text='Miles')
miles.grid(column=2, row=0)

km = tkinter.Label(text='Km')
km.grid(column=2, row=1)

result = tkinter.Label(text='0')
result.grid(column=1, row=1)

# Button

button = tkinter.Button(text='Calculate', command=convert)
button.grid(column=1, row=2)

window.mainloop()