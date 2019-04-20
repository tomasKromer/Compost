import Adafruit_DHT as dht #Importing Adafruit library for DHT
from Adafruit_CharLCD import Adafruit_CharLCD   # Importing Adafruit library for LCD
import os
import time

lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=20, cols=16, lines=2)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

addr_sensor[0] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’
addr_sensor[1] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’
addr_sensor[2] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’
addr_sensor[3] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’
addr_sensor[4] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’
addr_sensor[5] = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’

pin_sen_1 = 21
pin_sen_2 = 22
pin_sen_3 = 23
pin_sen_4 = 24

"""Leer las mediciones del sensor"""
def temp_raw(temp_sensor):

    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines
	
def read_temp(temp_sensor):
	lines = temp_raw(temp_sensor)
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = temp_raw()
	temp_output = lines[1].find('t=')
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c

"""Si estan todos los sensores conectados va a imprimir sus mediciones"""
while True:
	while i in range(6)
		lcd.set_cursor(0,0)                         # Set cursor to first line
		lcd.message('Temp: %d C' % read_temp(addr_sensor[i]))            # Print temperature on LCD
		time.sleep(5)
    time.sleep(1)
	hum_1, temp_1 = dht.read_retry(dht.DHT22, pin_sen_1)
	hum_2, temp_2 = dht.read_retry(dht.DHT22, pin_sen_2)
	hum_3, temp_3 = dht.read_retry(dht.DHT22, pin_sen_3)
	hum_4, temp_4 = dht.read_retry(dht.DHT22, pin_sen_4)
	lcd.set_cursor(0,0)                         # Set cursor to first line
	lcd.message('Temp: %d C' % temp_1)            # Print temperature on LCD
	lcd.set_cursor(0,1)                         # Set cursor on second line
	lcd.message('Humi: %d %%' % humi_1)           # Print Humidity on LCD
	time.sleep(5)
	lcd.set_cursor(0,0)                         # Set cursor to first line
	lcd.message('Temp: %d C' % temp_2)            # Print temperature on LCD
	lcd.set_cursor(0,1)                         # Set cursor on second line
	lcd.message('Humi: %d %%' % humi_2)           # Print Humidity on LCD
	time.sleep(5)
	lcd.set_cursor(0,0)                         # Set cursor to first line
	lcd.message('Temp: %d C' % temp_2)            # Print temperature on LCD
	lcd.set_cursor(0,1)                         # Set cursor on second line
	lcd.message('Humi: %d %%' % humi_2)           # Print Humidity on LCD
	time.sleep(5)
	lcd.set_cursor(0,0)                         # Set cursor to first line
	lcd.message('Temp: %d C' % temp_3)            # Print temperature on LCD
	lcd.set_cursor(0,1)                         # Set cursor on second line
	lcd.message('Humi: %d %%' % humi_3)           # Print Humidity on LCD
	time.sleep(5)