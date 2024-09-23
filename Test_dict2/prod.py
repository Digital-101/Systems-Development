products = {'usb': 120, 'mouse': 130, 'xbox':900}

def get_price(name):
    if name in products:
        return f'{name} is in the dictionary.'
    else:
        return f'{name} is not found.'

#0
# name = input('Enter product name to search: ').lower()
# print(get_price(name))

#1
new_products = {'gpu': 4000, 'router':700}
products.update(new_products)
print(products)

#2,3,4,5,6
#menu
# try:
#     print('==Choose option==')
#     choice = int(input('--1.Add \n2.Update \n3.Find Price \n4.Delete--\n'))

#     if choice == 1:
#         p_name = input('\nEnter product name to add: ').lower()
#         p_price = float(input('Enter price to add: '))
#         new_entry = {p_name:p_price}
#         products.update(new_entry)
#         print(products)
#     elif choice == 2:
#         p_name = input('\nEnter product name to update: ').lower()
#         p_price = float(input('Enter price to update: '))
#         new_entry = {p_name:p_price}
#         products.update(new_entry)
#         print(products)  
#     elif choice == 3:
#         p_name = input('\nEnter product name to find price for: ').lower()
#         if p_name in products:
#             print(f'{p_name} price is: R{products.get(p_name):.2f}')
#         else:
#             print(f'{p_name} not in dictionary.')
#     elif choice == 4:
#         p_name = input('\nEnter product name to delete: ')
#         if p_name in products:
#             del products[p_name]
#             print(f'{p_name} deleted successfully')
#             print(products)
#         else:
#             print(f'{p_name} not in dictionary')
# except ValueError:
#     print('Invalid Choice')

#7
def get_product_price_range(products, start, stop):
    #  start = float(input('Enter price start range: '))
    #  stop = float(input('Enter price stop range: '))
     print(f"Products in the range R{start} - R{stop}:")
     filtered_products = [(product, price) for product, price in products.items() if start <= price <= stop]
     return filtered_products
    # for product, price in products.items():
    #     if price >= start and price <= stop:
    #         print(f"{product}: R{price}")

print(get_product_price_range(products, 100, 1000))

#8
def get_products_cheaper_than(products, price_limit):
    """Returns a list of products cheaper than the given price."""
    return [product for product, price in products.items() if price < price_limit]

#print(get_products_cheaper_than(products, 500))

#9.
def get_expensive(products):
    if not products:
        return None
    return max(products.items(), key=lambda x: x[1] )

#print(get_expensive(products))

#10.
def get_cheaper(products):
    if not products:
        return None
    return min(products.items(), key=lambda x: x[1] )

#print(get_cheaper(products))

#11.
new_products = {'usb': [120, 'electronic',10], 
            'mouse': [130,'electronic',5], 
            'xbox':[900, 'console', 4],}
#print(new_products)

#12.
def get_all_products():
    p_name = input('Enter product name: ')
    if p_name in products:
        return products.get(p_name)
    else:
        return None
    
#print(get_all_products())