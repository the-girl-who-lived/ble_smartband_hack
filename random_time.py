import os
from random import randrange
import crcmod.predefined
import codecs
import time
decode_hex = codecs.getdecoder("hex_codec")
crc8 = crcmod.predefined.mkPredefinedCrcFun('crc-8-maxim')

for i in range(100):
	data = "ab0b040113" + format(randrange(12),'x').zfill(2) + format(randrange(12),'x').zfill(2) +  format(randrange(23),'x').zfill(2) + format(randrange(60),'x').zfill(2) + format(randrange(60),'x').zfill(2) 
	datacrc = data + format(crc8(decode_hex(data)[0]),'x')
	print("Data and CRC Calculted")
	os.system("gatttool -b 66:31:39:10:56:D0 --char-write-req -a 0x0e -n " + datacrc)
	print("wrote 0x" + datacrc + " at 0x0e ")
	time.sleep(0.5)
