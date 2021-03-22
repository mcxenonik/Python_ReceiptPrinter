def split_price(price):
    price_zl = price // 100
    price_gr = price % 100

    return (price_zl, price_gr)


def get_description(name, price):
    price_parts = split_price(price)

    return f'Price of {name} is {price_parts[0]}.{price_parts[1]:02}'


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_product():
    name = input('Enter product name: ')
    price = input('Enter product price: ')

    return (name, int(price))


def get_total_price(receipt):
    total_value = 0
    for element in receipt:
        total_value += element[1]

    return total_value


def format_price(price):
    zl, gr = split_price(price)

    return f'{zl}.{gr:02}'


receipt = [
    ('Bananas', 499),
    ('Oranges', 803),
    ('Milk', 315)
]


my_total_value = get_total_price(receipt)
print(format_price(my_total_value))
