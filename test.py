import pyb

lcd = pyb.LCD('x')
lcd.light(True)

while 1:
    adc1 = pyb.ADC(pyb.Pin.board.Y11)
    adc2 = pyb.ADC(pyb.Pin.board.Y12)
    val1 = adc1.read()/4095*3.3*11
    val2 = adc2.read()/4095*3.3*50*val1
    val1_str = str('%1.2f'%val1)
    val2_str = str('%1.2f'%val2)
    lcd.write('adc1:')
    lcd.write(val1_str)
    lcd.write('\n')
    lcd.write('adc2:')
    lcd.write(val2_str)
    lcd.write('\n\n\n')
    pyb.delay(1000)
    lcd.fill(0)
    lcd.show()
