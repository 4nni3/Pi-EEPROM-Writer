#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import pigpio
import time
import sys

def write_ROM():
    pi=pigpio.pi()
    h=pi.i2c_open(1,addr)

    count=0
    addressH=0
    f=open(f_name,'r')
    for m in f:
        
        addressL=(count%16)*16
        
        l1=m[:-1].split(' ')
        l2=[ l1[0][0:2], l1[0][2:4], l1[0][4:6], l1[0][6:8], l1[1][0:2], l1[1][2:4], l1[1][4:6], l1[1][6:8], l1[2][0:2], l1[2][2:4], l1[2][4:6], l1[2][6:8], l1[3][0:2], l1[3][2:4], l1[3][4:6], l1[3][6:8] ]
        l3=[addressL,int(l2[0],16),int(l2[1],16),int(l2[2],16),int(l2[3],16),int(l2[4],16),int(l2[5],16),int(l2[6],16),int(l2[7],16),int(l2[8],16),int(l2[9],16),int(l2[10],16),int(l2[11],16),int(l2[12],16),int(l2[13],16),int(l2[14],16),int(l2[15],16) ]
        print l2

        pi.i2c_write_i2c_block_data(h,addressH,l3)
        count+=1
        
        if count%16 == 0:
            addressH+=1
        
        time.sleep(0.2)

    print('%dbytes'%(count*16))
    
    f.close()
    pi.i2c_close(h)


if __name__ == '__main__':
    args = sys.argv
    if len(args)<3:
        print('usage: python {} <Device Address(HEX)> <source file name>'.format(__file__))
        exit(0)

    addr=int(args[1],16)
    f_name=args[2]

    write_ROM()



