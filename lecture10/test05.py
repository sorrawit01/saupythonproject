# อ่านข้อมูลจากไฟล์ 
f_dti = open('myfile01.txt', 'r', encoding='utf-8')

try :
    data = f_dti.read()

    print(data)
except Exception :
    print('ติดต่อ Admin 012345555')
finally : 
    f_dti.close()