def inputnameAndph():
    name = input('ป้อนชื่อจังหวัด : ')
    ph = int(input('ป้อนค่า ph : '))
    return name , ph

def checkph(ph):
    if ph == 7 or ph == 8 :
       return 'Result is Normal'
    elif ph > 8 :
       return 'Result is Acid'
    else :
        return 'Result is Alkali'

def show(name, result):
    print(f'จังหวัด {name} ค่า ph ของน้ำปะปาคือ {result}')

name , ph = inputnameAndph()
result = checkph(ph)
show(name , result)




    
    