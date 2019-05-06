#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import pigpio
import time
import sys

def write_ROM():
    pi=pigpio.pi()
    h=pi.i2c_open(1,addr)


    count=0
    i=0
    addressH=0
    c=[]
    f=open(f_name, 'rb')
    for b in f.read():
        c.append(b)
        i+=1
        if i==16:
            print c
            addressL=(count%16)*16
            c.insert(0,addressL);
        
            pi.i2c_write_i2c_block_data(h,addressH,c)
            count+=1
            
            i=0
            c=[]
        
            if count%16 == 0:
                addressH+=1
        
            time.sleep(0.1)

    print c
    addressL=(count%16)*16
    c.insert(0,addressL);
        
    pi.i2c_write_i2c_block_data(h,addressH,c)

    print('%dbytes'%(count*16+i))
    
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



