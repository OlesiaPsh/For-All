n = int(input('Сколько билетов покупаете? '))

age = [int(input('Введите возраст посетителя: ')) for i in range(n)]
price = []
for a in age:
    if a < 18:
        price.append(0)
    if 25 >= a >= 18:
        price.append(990)
    if a > 25:
        price.append(1390)
sum = 0
for k in price:
    sum += k
if n > 3:
    sum *= 0.9

print('Сумма к оплате: ', sum)