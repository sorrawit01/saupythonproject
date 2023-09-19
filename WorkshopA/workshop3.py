def inputnameproduct():
    product = input('ป้อนชื่อสินค้า : ')
    return product
def inputprice():
    price = float(input('ป้อนราคาสินค้า : '))
    return price
def calandshow(product , price):
    total = price * 7 / 100 
    print(f'ชื่อสินค้า {product} ราคาสินค้า {price} มีภาษีทั้งหมด {total} บาท')
    return total

product = inputnameproduct()
price = inputprice()
calandshow(product , price)
