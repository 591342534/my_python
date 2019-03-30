# 串口模块安装及使用例程

# pip install pyserial

# pip list
# Package    Version
# ---------- -------
# pip        19.0.3
# pyserial   3.4
# setuptools 40.8.0
# wheel      0.33.1

'my serial module demo'
_author = 'dai'

import sys
import serial

global _objSerial
_objSerial = None


def main():
    print("begin main")
    args = sys.argv
    if len(args) == 1:
        print("hello world!")
    elif len(args)==2:
        print("comport: %s" % args[1])
        print("open com port: ", open_com(args[1]))
        print("write data: ", write_com("hello, dai".encode("utf-8")))
        print("close com port: ", close_com())
    else:
        print("too many arguments!")
    print("end main")

def open_com(comport):
    bRet = False

    try:
        temp_comprt = comport
        baudrate = 9600
        timeout = 5
        global _objSerial
        _objSerial =serial.Serial(temp_comprt, baudrate=baudrate, timeout=timeout)
        bRet = True
    except Exception as e:
        print("except:", e)

    return bRet

def write_com(buf):
    bRet = False
    nWriteLen = 0
    send_buf = buf

    try:
        global _objSerial
        nWriteLen = _objSerial.write(send_buf)
    except Exception as e:
        print("except:", e)
    
    if nWriteLen==len(send_buf):
        bRet = True    

    return bRet

def close_com():
    global _objSerial
    if _objSerial!=None:
        _objSerial.close()
        _objSerial = None



if __name__ == '__main__':
    main()