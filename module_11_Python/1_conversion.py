
# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например,
# если купить что-то в евро,
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
#
# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
#
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

euro_price = float(input("Enter price in euro: "))
euro_to_usd = round(euro_price * 1.25, 2)
usd_to_rub = round(euro_to_usd * 60.87, 2)

print(f'Price in USD: {usd_to_rub}')
