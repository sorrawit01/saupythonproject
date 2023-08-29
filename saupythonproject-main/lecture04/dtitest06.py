name = input('ชื่อสินค้า')
price = float(input('ราคาสินค้า'))
total = price + (price * 10 / 100)
print(f'ชื่อของสินค้า {name} ราคาสินค้า {price} จะมีราคาขาย {total} ')