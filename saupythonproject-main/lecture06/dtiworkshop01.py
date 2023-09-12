def inputBaseHight() :
    base = float(input('ป้อนฐาน : '))
    hight = float(input('ป้อนสูง : '))
    return base , hight
def calAndShowTriangleArea(base, hight):
    area = base * hight / 2
    print(f'สามเหลี่ยมฐาน {base:.2f} สูง {hight:.2f} มีพื้นที่ {area:.2f}')

print('--------------------------')
print('--Calculat Triangle Area--')
print('--------------------------')
base, hight = inputBaseHight()
print('--------------------------')
calAndShowTriangleArea(base, hight)
print('--------------------------')