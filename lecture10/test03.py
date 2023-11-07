# เขียนข้อมูลลงไฟล์
f_dti=open('myfile02.txt', 'x', encoding='utf-8') #เปิดไฟล์เพิ่อเขียนข้อมูลลงไฟล์
f_dti.write('SAU123....')
f_dti.write('DTI321....\n')
f_dti.write('บาย บาย.....\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')