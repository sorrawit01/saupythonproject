# เขียนข้อมูลลงไฟล์
f_dti=open('myfile01.txt', 'w', encoding='utf-8') #เปิดไฟล์เพิ่อเขียนข้อมูลลงไฟล์
f_dti.write('Hello....')
f_dti.write('woow....\n')
f_dti.write('บาย บาย.....\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')