import smbus
import time

# Constants
DEVICE     = 0x23 
POWER_DOWN = 0x00 
POWER_ON   = 0x01 
RESET      = 0x07 
HIGH_RES_MODE = 0x20

# Uses I2C1 port
bus = smbus.SMBus(1)

# Converts data to lux
def convert(data):
  return ((data[1] + (256 * data[0])) / 1.2)
 

def read(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,HIGH_RES_MODE)
  return convert(data)
 
while True:
    print("Light Level : " + str(read()) + " lux")
    if read() < 50:
        print("too dark")
    elif read() < 100:
        print("dark")
    elif read() < 150:
        print("medium")
    elif read() < 500:
        print("bright")
    else:
        print("too bright")
    time.sleep(2)
