money = int(input())
proc = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
proc = per_cent.values()
for i in proc:

    deposit.append(round(i/100*money))
print(deposit)
print(max(deposit))