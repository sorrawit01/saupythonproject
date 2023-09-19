def inputcodeAndnameAndmoney():
    code = int(input('ป้อนรหัสพนักงาน : '))
    name = input('ป้อนชื่อพนักงาน : ')
    money = float(input('ป้อนจำนวนเงินยอดขาย : '))
    return code , name , money 

def checkCommission(money):
    if  money >= 1001 or money == 2000 :
        return money * (1/ 100)
    elif money >= 2001 or money == 3000 :
        return money * (3 / 100)
    elif money > 3000 :
        return money * (5 / 100)
    else :
        return money * 0 
    
def showcommission(code , name , commision):
    print(f'รหัสพนักงาน {code} ชื่อพนักงาน {name} ค่าคอมมิชชั่นจะได้ {commision}')

code , name , money = inputcodeAndnameAndmoney()
commission = checkCommission(money)
showcommission(code , name ,commission )
    