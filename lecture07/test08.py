var2 = (10 , 20 , 'Hello' , True, (111, 'WoW'), 'มานะ')

# var2[2] = 'Hi' error
# การเปลี่ยนแปลงคำเพิ่ม ลบ ข้อมูลใน Tuple
# list(), Tuple()
varTemp = list(var2)
varTemp[2] = 'Hi'
var2 = tuple(varTemp)
print(var2)