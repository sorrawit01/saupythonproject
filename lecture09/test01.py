class DtiTest01:
    pass

class DtiTest02:
    infoA = ''
    infoB = 20

# method คือ ฟังก์ชั่นประเภทหนึ่ง
    def showHi(self):
        print('Hi....')

    def showInfoAandB(self):
        print(self.infoA)
        print(self.infoB)

# สร้าง object
objA = DtiTest02()
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA = 'XXX'
objB.infoB = 100
print(objA.infoB + objB.infoB)

sombat.showInfoAandB()