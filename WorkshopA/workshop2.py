def inputcodeAndnamestu():
    code = input('ป้อนรหัสนักเรียน : ')
    name = input('ป้อนชื่อนักเรียน : ')
    return code , name

def inputstuTest():
    Test1 = float(input('ป้อนคะแนนการสอบครั้งที่ 1 : '))     
    Test2 = float(input('ป้อนคะแนนการสอบครั้งที่ 2 : '))     
    Test3 = float(input('ป้อนคะแนนการสอบครั้งที่ 3 : ')) 
    return Test1 , Test2 , Test3 

def calandshowtest(name, code ,Test1 , Test2 , Test3):
    average = (Test1+Test2+Test3) / 3
    print (f'ชื่อนักเรียน {name} รหัสนักเรียน {code} สอบครั้งที่ 1 ได้ {Test1} สอบครั้งที่ 2 ได้ {Test2} สอบครั้งที่ 3 ได้ {Test3} คะแนนเฉลี่ยจะได้ {average} คะแนน')

code , name = inputcodeAndnamestu()
Test1 , Test2 , Test3 = inputstuTest() 
calandshowtest (name , code , Test1 , Test2 ,Test3)