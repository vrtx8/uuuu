#price = 100
#discount = 5

def input_price():

    print("Введите цену товара и скидку")

    price = int(input())
    discount = int(input())

def price_with_discount(price, discount):
    if discount > 100:
        print("Введите корректное значение скидки, меньше 100 %")
    if discount or price < 0:
        abs(discount)
        abs(price)

        
    return price - price * discount / 100
print(price_with_discount(price, discount))

