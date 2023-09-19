def inputphone():
    name = input('ชื่อผู้ช้โทรศัพท์ : ')
    number = int(input('เบอร์โทรศัพท์ : '))
    minute = int(input('นาทีที่ใช้โทรศัพท์'))
    return name , number , minute

def checkphoneminute(minute):
    if minute == 1 and minute <= 15 :
        return minute * 5 
    elif minute == 16 and minute <= 30 : 
        return minute * 3
    else :
        return minute * 1.5 

def showphone(name , number , minute , bill ):
    print(f'ชื่อผู้ใช้โทรศัพท์ {name} เบอร์โทรศัพท์ {number} จำนวนนาที {minute} ค่าโทรศัพท์ {bill}')

name , number , minute = inputphone()
bill = checkphoneminute(minute)
showphone(name , number, minute , bill)
    
