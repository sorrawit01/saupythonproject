# List Function/Tuple Function
# len(), min(), max()

var1 = [10, 20, 'Hello', True, [111, 'WoW'], 'มานะ']

var2 = (10 , 20 , 'Hello' , True, (111, 'WoW'), 'มานะ')

print(f'ใน var1 มีข้อมูลทั้งหมด {len(var1)} ข้อมูล')
print(f'ใน var2 มีข้อมูลทั้งหมด {len(var2)} ข้อมูล')
# min กับ max ใช้ไม่ได้กับข้อมูลคนละชนิด
# print(min(var1)) error
var3 = [10, 20, 30, True, 10, 20]
var4 = (10, 20, 30, True, 10, 20)
print(min(var3))
print(max(var4))