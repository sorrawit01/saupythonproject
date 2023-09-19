def inputnumber():
    number = int(input('ป้อนเลข : '))
    return number

def test(number):
    if number == 25 :
        print('Correct, You are the winner')
    else :
        print('Not Correct !!!.')

def show (result):
    return result

number = inputnumber()
result = test(number)
show(result) 