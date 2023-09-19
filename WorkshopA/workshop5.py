def inputcodeAndname():
    code = input('ป้อนรหัสพนักงาน : ')
    name = input('ป้อนชื่อพนักงาน : ')
    return code , name 
def inputmoney():
    money = float(input('ป้อนเงินเดือน : '))
    return money
def calAndshow(money):
    total = money - (money * 7 /100 ) - 500
    print (f'เงินเดือนพนักงาน {money} บาท หักค่าภาษีและเบี้ยประกันสังคมไปแล้วจะเหลือ {total} บาท')
    return total

code , name = inputcodeAndname()
money = inputmoney()
calAndshow(money)