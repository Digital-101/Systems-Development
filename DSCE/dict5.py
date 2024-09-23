products = {'iPhone':6000, 'Samsung':4000, 'DellPC':4600}

def get_price():
    pname = input('Enter product name: ')
    msg = ''
    if pname in products:
        msg = f'{pname} found and it cost {products.get(pname)}'
    else:
        msg = f'{pname} not Found'
    return msg

def get_products():
    price = float(input('Enter product price: '))
    print(f'--- List of Products that costs {price} ---')
    for k in products.items():
        if price in k:
            return k[0]

print(get_price())
print(get_products())