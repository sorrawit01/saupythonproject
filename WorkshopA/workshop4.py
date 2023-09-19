def inputx():
    x= float(input('รับค่า x : '))
    return x 
def cal():
    y = 2*(x)**2 + 2*(x) + 1 
    return y 
def show(x,y):
    print(f'แก้สมการเมื่อ x = {x} จะได้ {y}')

x = inputx()
y = cal()
show(x,y)