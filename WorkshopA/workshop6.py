def inputname():
    name = input('ชื่อผู้กู้ : ')
    return name
def inputmoney():
    money = float(input('จำนวนเงินกู้ : '))
    return money 
def cal(money):
    if money > 1000 :
        more = money *(2.5/100) 
        return more
    else :
        less = money *(5.5/100)
        return less
def show (name , money):
    print(f'ชื่อผู้กู {name} จำนวนเงินอัตราดอกเบี้ย {money} บาท')
    

name = inputname()
money = inputmoney()
money = cal(money)
show (name , money)

    
