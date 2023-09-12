def inputCarDetail():
    carNo = input('ป้อนทะเบียนรถ : ')
    carWeight = float(input('ป้อนน้ำหนักรถ : '))
    return carNo , carWeight

def checkCarAndShowWeight(carNo, carWeight):
    if carWeight > 1000 :
        print(f'ทะเบียนรถ {carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'ทะเบียนรถ {carNo} น้ำหนักผ่านเกณฑ์')
print('--------------------------')
print('====Turck Checker====')
print('--------------------------')
carNo , carWeight = inputCarDetail()
print('--------------------------')
checkCarAndShowWeight(carNo, carWeight)
print('--------------------------')