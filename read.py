#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pigpio
import sys

addr = 0
adr1=0
adr2=0
startaddr = 0
endaddr = 0

def read_ROM():

    pi = pigpio.pi()
    h = pi.i2c_open(1, addr)

    print('%4s | %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X %2X ' %('Adr',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) )
    print('-'*54)

    for addressH in range(startaddr/256, endaddr/256+1):       
        for j in range(16):
            addressL = 16*j
            pi.i2c_write_byte_data(h, addressH, addressL)
            c, l1 = pi.i2c_read_device(h, 16)
        
            print('%4X | %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X ' %(256*addressH+addressL,l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],l1[8],l1[9],l1[10],l1[11],l1[12],l1[13],l1[14],l1[15]) )

            l1=[]

    pi.i2c_close(h)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4 :
        print('usage: python {} <Device Address(HEX)> <Start Address(HEX)> <End Address(HEX)>'.format(__file__))
        exit(0)


    addr = int(args[1],16)
    startaddr = int(args[2],16)
    endaddr = int(args[3],16)
    
    read_ROM()


