class DtiTest03 :
    # data
    infoA = 10


    # constructor จะเป็นตัวทำให้ Object ที่สร้างจากคลาสเดียวกันไม่จำเป็นต้องเหมืือนกัน
    # constructor จะทำงานทุกครั้งที่มีการส้ราง Object
    def __init__(self, infoB, infoC):
        self.infoB = infoB
        self.infoC = infoC

    # method
    def showMixAndInfo(self , mix):
        print(self.infoA + self.infoB + self.infoC + mix)

# สร้าง Object  
sau1 = DtiTest03(20, 30) 
sau2 = DtiTest03(10, 100) 
sau3 = DtiTest03(20, 30) 