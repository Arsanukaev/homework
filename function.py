def discounted(price, discount, max_discount=20):
    try:
        price = abs(int(price))
        discount = abs(int(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        print ("введите число")
discounted (10000, 10)
