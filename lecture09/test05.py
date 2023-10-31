# คุณสมบัติเด่น Inheritance สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง ***(re-use)
# สืบทอด มีแม่ (super class) มีลูก (sub class)
# แม่มีอะไรลูกมีด้วย เมื่อมีการสืบทอด (Inheritance)

# คุณสมบัติเด่น Polymorphism (พ้องรูป:พฤติกรรมเดียวกันแต่วิธีการต่างกัน) คือ การที่คลาสลูก เอาเมธอดของคลาสแม่มาเขียนใหม่

class Sau01 : 
    infoA = 10

    def showHi():
        print('Hi.....')

class Sau02(Sau01) :
    infoB = 20

    def showHey() :
        print('Hey.....')    

    def showHi() :
        print('Hi Hi Hi....')
        
ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()
