print('\nРаспределение процентных ставок по вкладам в различных банках:')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for key, value in per_cent.items():
  print("{0}: {1}".format(key,value))
print('-' * 80)
money = input('Введите сумму (целое число), которую планируете положить под проценты:\n')
if money.isnumeric()==True or money.isdigit()==True:
            print('-'*80)
            money = float(money)
            print("Ваша сумма: ", money,"руб.")
else: print("Пожалуйста, введите корректную сумму!")
print('Накопленные средства за год вклада в каждом из банков:')
per_centList = list(per_cent.values())
depTKB = round(per_centList[0]*money/100, 2)
depSKB = round(per_centList[1]*money/100, 2)
depVTB = round(per_centList[2]*money/100, 2)
depSBER = round(per_centList[3]*money/100, 2)
deposit = {'ТКБ': depTKB, 'СКБ': depSKB, 'ВТБ': depVTB, 'СБЕР': depSBER}
for key, value in deposit.items():
  print("{0}: {1}".format(key,value))
print('-' * 80)
stonks = max(deposit.values())
print('Максимальная сумма, которую вы можете заработать', stonks)