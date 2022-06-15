import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 8888)

print('Welcome to currencies exchange')
print('1- List all currencies rates')
print('2- Convert USD to another currency')
select = int(input('select 1 or 2: '))

if select == 1:
    for currency in ['EUR', 'SYP', 'AED', 'CAD']:
        s.sendto(currency.encode(), server_address)
        message, address = s.recvfrom(1024)
        rate = float(message.decode())
        print('1 USD =', round(rate,2), currency)
elif select == 2:
    currency = input('Enter currency (EUR, SYP, AED, CAD): ')
    if currency not in ['EUR', 'SYP', 'AED', 'CAD']:
        print('Invalid currency')
    else:
        s.sendto(currency.encode(), server_address)
        message, address = s.recvfrom(1024)
        rate = float(message.decode())
        usd_amount = float(input('Enter the amount (in USD):'))
        amount = usd_amount * rate
        print(round(amount,2),currency)
