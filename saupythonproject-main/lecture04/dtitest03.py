#function แบบที่ 2 - Have parameters/No return
#parameter คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น

def funcA( x , y):
    print(f'x is {x}')
    print(f'y is {y}')
    print(f'Sum {x} + {y} = {x+y}')

funcA(20,30)
funcA(3,6)
print('AAAA.....')
funcA(30,30)