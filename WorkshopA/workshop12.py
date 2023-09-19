def inputgrouptour():
    name = input('ชื่อหัวหน้ากรุ๊ป : ')
    phone = input('เบอร์โทรศัพท์ติดต่อกลับ : ')
    countgroup = int(input('จำนวนกรุ๊ป : '))
    return name , phone , countgroup

def checkgrouptour(countgroup):
    if countgroup <= 2 :
        pack = countgroup * 300
    elif countgroup <= 5 :
        pack = countgroup * 250
    elif countgroup <= 10 :
        pack = countgroup * 210
    else :
        pack = countgroup *150
    average =  pack / countgroup
    return  pack , average 

def showgrouptour(name , phone , countgroup , pack , average ):
    print(f'ชื่อหัวหน้ากรุ๊ป {name} เบอร์โทรศัพท์ติดต่อกลับ {phone} จำนวนกรุ๊ป {countgroup} แพ็คเก็จ {pack} เฉลี่ยคนละ {average} ต่อคน  ')

name , phone , countgroup = inputgrouptour()
checkgroup , average = checkgrouptour(countgroup)
showgrouptour(name , phone , countgroup, checkgroup , average )
