#Function 2 : have parameter/no return
#parameter คือ ตัวแปร (varible) ประเภทหนึ่ง
def funcC(x, y):
    print('AAA')
    z= x + y
    print(f'{x}+{y}= {z}')
def funcD(x, y ,z):
    print('{:.2f} {:.4f} {:.5f}'.format(x , y ,z))

funcC(10, 30)
funcC(5, 10)
funcD(1, 5 ,10)
