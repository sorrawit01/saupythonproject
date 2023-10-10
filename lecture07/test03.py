# List Method
var1 = [10, 20, 'Hello', True, [111, 'WoW'], 'มานะ']
# append
var1.append(555)
var1.append(['Hi', 'Hey', 999])
print(var1)
# extend เพิ่มแต่ละข้อมูล
var1.extend([10, 20 , 30])
print(var1)
# remove
var1.remove('Hello')
var1.remove(10)
print(var1)
# ----
var2 = [10, 20 , 'Hello']
# insert
var2.insert(2, 'Hi')
print(var2)
# pop
var2.pop()
print(var2)
var2.pop(1)
print(var2)
# index
print(var2.index('Hi'))
# count นับจำนวนข้อมูลนั้นๆที่อยู่ใน list
print(var1.count(10))
var3 = [10, 10, 20, 'Hi', 10, 'Hi']
print(f'ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว')
print(f'ใน var3 มี Hi ทั้งหมด {var3.count("Hi")} ตัว')
# เมธอดต่อไปนี้ใช้ได้เฉพาะข้อมูลในที่เป็นประเภทเดียวกันเท่านั้น
# sort
var4 = [10, 10, 20, 'Hi', 10,'Hi']
# var4.sort() error
var5 = [99, 34, 635, 3423, 99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)