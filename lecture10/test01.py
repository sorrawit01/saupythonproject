try :
    num1 = int( input('Input number 1 : '))
    num2 = int( input('Input number 2 : '))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f'{num1} x {num2} = {result1}')
    print(f'{num1} / {num2} = {result2}')
except ValueError : 
    print('ตรวจสอบการป้อนข้อมูล เนื่องจากป้อนข้อมูลไม่ถุกต้อง')
except ZeroDivisionError :
    print('ตรวจสอบการป้อนข้อมูล ตัวเลขตัวที่ 2 ห้ามเป็น 0')
except Exception : 
    print('มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อ 01234555555 ทีม IT')
finally :
    print('WoW wow wow')
