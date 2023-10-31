# คุณสมบัติ Encapsulation (ห่อหุ้ม data/attribute/field/property)
class DtiTest05 :
    # data
    infoA = 10  #ไม่ได้ห่อหุ้ม
    __infoB = 20 #ห่อหุ้ม

    def __init__(self, infoC, infoD) :
        self.infoC = infoC #ไม่ได้ Encap
        self.__infoD = infoD #Encap ดูจาก__??

        # เมื่อใดก็ตาม Encap จะต้องมีเมธอด 2 ตัวนี้เสมอ คือ get, set ของ data ตัวนั้น
    def setInfoB(self, infoB):
        self.__infoB = infoB

    def getInfoB(self):
        return self.__infoB
    
    def setInfoB(self, infoD):
        self.__infoD = infoD

    def getInfoB(self):
        return self.__infoD
    
    def showInfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.__infoD, end='')
        print(self.infoC)
        print('=============')


ob1 = DtiTest05(30, 40)
ob2 = DtiTest05(30, 100)
ob1.showInfo()
ob1.infoA = 555
# ob1.__infoB = 999 ไม่เปลี่ยนค่า เพราะ ถูก Encap
ob1.showInfo(999)
ob1.showInfo()
# print(ob1.__infoB + ob.__infoD) มันถูก Encap ถ้าจะเอาค่าที่เก็บมาใช้งานต้องมาเมธอด get
print(ob1.getInfoB() + ob1.getInfo())