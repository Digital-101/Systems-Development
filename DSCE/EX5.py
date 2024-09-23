products = {'iphoneX':5000, 'LenovoPC':5000, 'DellPC':4500, 'Samsung_A32':5540}

def get_price():
    p_name = input('Enter product name: ')
    msg = ''
    if p_name in products:
        msg = f'{p_name} found and price is {products.get(p_name)}'
    else:
        msg = 'Product is not found'
    return msg

def get_names():
    price = float(input('Enter price: '))
    print(f'--Products that costs: {price} are:')
    for k in products.items():
        if price in k:
            return k[0]

print(get_price())
get_names()