def inputProduct():
    product = input('ชื่อสินค้า : ')
    return product

def inputPrice():
    price = float(input('ราคาสินค้า : '))
    return price

def CalandshowProductsellingprice(product , price ):
    productprice = price + (price *10 / 100)
    print(f'ชื่อสินค้า {product} ราคาสินค้า {price} ราคาขายสินค้าคือ {productprice} บาท')    

print('----------------------')
product = inputProduct()
price = inputPrice()
CalandshowProductsellingprice(product , price)