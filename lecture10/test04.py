# เขียนข้อมูลลงไฟล์
f_dti=open('myfile03.txt', 'a', encoding='utf-8') #เปิดไฟล์เพิ่อเขียนข้อมูลลงไฟล์

f_dti.write('AAAA\n')
f_dti.write('BBBB\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')