#ATM

money_value = int(input('how much money do you want to withdraw?'))

banknotes_50 = money_value // 50
if banknotes_50 > 0:
	print(f'Received: {banknotes_50} 50$ banknotes')
money_value = money_value % 50

banknotes_20 = money_value // 20
if banknotes_20 > 0:
	print(f'Received: {banknotes_20} 20$ banknotes')
money_value = money_value % 20

banknotes_10 = money_value // 10
if banknotes_10 > 0:
	print(f'Received: {banknotes_10} 10$ banknotes')
money_value = money_value % 10

banknotes_1 = money_value // 1
if banknotes_1 > 0:
	print(f'Received: {banknotes_1} 1$ banknotes')
money_value = money_value % 1