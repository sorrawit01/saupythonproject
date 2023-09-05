import math
def inputRadius( ):
    return float( input('ป้อนรัศมี :'))
def areaCircle(r):
    area = math.pi * r**2
    return area
def roundCircle(r):
    round =  2*math.pi *r
    return round
def cubecircle(r):
    cube = 4/3 *math.pi *r**3
    return cube
def show( ):
    a = inputRadius( )
    print(f'พื้นที่วงกลม {areaCircle(a):.4f} เส้นรอบวง {roundCircle(a):.4f} ปริมาตร {cubecircle(a):.4f}' )
show( )