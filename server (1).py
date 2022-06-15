import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", 8888)
s.bind(address)

currencies_rates = {}

# load_currencies
url = "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=USD,EUR,SYP,AED,CAD"
res = requests.get(url,headers={'Accept':'application/json','apikey':'hNyyYLiFXgHQqYMPWa5fou4ac1ptoB9P'})
if res.status_code != 200:
    print('error while loading currencies')
else:
    data = res.json()
    currencies_rates = data['rates']
    print('currencies loaded successfully')

    print('waiting a message on port 8888')
    while True:
        message, address = s.recvfrom(1024)
        print('Message from address: ', address)
        
        currency = message.decode()
        if currency in currencies_rates:
            rate = str(currencies_rates[currency])
            s.sendto(rate.encode(), address)
        else:
            s.sendto("NOT_FOUND".encode(), address)
