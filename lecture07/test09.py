var1 = [10, 20, 'Hello', True, [111, 'WoW'], 'มานะ']

var2 = var1
var3 = var1.copy()

print(var1)
print(var2)
print(var3)
print('-----------------')
print(var1)
print(var2)
print(var3)
print('-----------------')
var3[0] = 999
print(var1)
print(var2)
print(var3)
print('-----------------')