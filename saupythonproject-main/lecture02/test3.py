emp_name = input('ป้อนชื่อพนักงาน : ')
sale_price = input('ป้อนยอดขาย : ')
print("-------------------")
commission = float(sale_price) * 10 /100
print (f'คุณ {emp_name} ยอดขาย {sale_price} ได้ค่าคอม {commission} บาท')
print ('คุณ', emp_name , 'ยอดขาย', sale_price, 'ได้ค่าคอม', commission, 'บาท' )
print ('คุณ'+emp_name+'ยอดขาย'+str(float(sale_price))+'ได้ค่าคอม'+str(float(commission))+'บาท')
print ('คุณ {} ยอดขาย {} ได้ค่าคอม {} บาท' .format(emp_name,sale_price,commission))