def inputmoneyperson( ):
    money = float( input('ป้อนเงิน : '))
    person = int( input('ป้อนคน : '))
    return money, person

def moneyshare(money, person ):
    print(f'จำนวนเงิน{money:.2f} บาท คน {person} คน แชร์กันคนละ {money/person} บาท')
    print('จำนวนเงิน', money , 'บาท','คน', (person) ,'คน', 'แชร์กันคนละ', round(money/person) ,'บาท')
    print('จำนวนเงิน' + str(money)+ 'บาท' + 'คน'+ str(person) + 'คน' + 'แชร์กันคนละ' + str(round(money/person))+ 'บาท'  )
    print('จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท'.format(money,person,round(money/person)))
    print('จำนวนเงิน %.2f บาท คน %d แชร์กันคนละ %s บาท'%(money, person, round(money/person)))
money , person = inputmoneyperson( )
moneyshare (money, person)
