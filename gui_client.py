import socket
from tkinter import *

# build GUI

w = Tk()
w.title("Currencies Exchange")

frame = Frame(width=400, height=400)
frame.pack()

label1 = Label(master=frame, text="Currencies rate:", font=('Arial', 12, 'bold'))
label1.place(x=25, y=25)

all_currencies_label = Label(master=frame, bg="#DDDDDD", width=50, height=5, anchor='w')
all_currencies_label.place(x=25, y=60)

label2 = Label(master=frame, text="Convert USD to other currencies:", font=('Arial', 12, 'bold'))
label2.place(x=25, y=180)

usd_amount_entry = Entry(master=frame, width=20)
usd_amount_entry.place(x=25, y=217)

def calculate(event):
    usd_amount = float(usd_amount_entry.get())
    t = ""
    for currency, rate in currencies.items():
        amount = usd_amount * rate
        t += "{} USD = {} {}\n".format(usd_amount, round(amount,2), currency)
    result_label.config(text = t)

button = Button(master=frame, width=15, text="Calculate")
button.place(x=160, y=215)
button.bind("<Button-1>", calculate)

result_label = Label(master=frame, bg="#DDDDDD", width=50, height=5, anchor='w')
result_label.place(x=25, y=250)


# load currencies
currencies ={}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 8888)

t = ""
for currency in ['EUR', 'SYP', 'AED', 'CAD']:
    s.sendto(currency.encode(), server_address)
    message, address = s.recvfrom(1024)
    rate = float(message.decode())
    currencies[currency] = rate
    t += "1 USD = {} {}\n".format(round(rate,2), currency)
all_currencies_label.config(text = t)


w.mainloop()
