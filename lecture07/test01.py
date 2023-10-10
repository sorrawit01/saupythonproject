#List 
var1 = [10, 20, 'Hello', True, [111, 'WoW'], 'มานะ']
#       -6  -5    -4      -3      -2          -1

print(var1[0] + var1[1])
print(var1[-6]+ var1[-5])
print(var1[0] + var1[4][0])
print(var1[-6] + var1[-2][-2])

#Tuple
var2 = (10 , 20 , 'Hello' , True, (111, 'WoW'), 'มานะ')
print(var2[0] + var2[1])
print(var2[-6]+ var2[-5])
print(f'{var2[2]}...{var2[5]} {var2[4][1]}...')