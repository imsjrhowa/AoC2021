# AoC 2021 Day 16
# Challenge 2
# Answer 116672213160

import sys
import os
import heapq

lines = [] 
activeBits = 0 

ans = 0

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
    data = f.read()

for line in data.splitlines():
    lines.append( line )

def challenge1():
    global bytesRead
    ret = 0

    def binaryToDecimal(n):
        return int(n,2)
    
    def hexToBinary(n):
        num_of_bits = 4
        return bin(int(n, 16))[2:].zfill(num_of_bits)

    def deleteBits(bits:str, count:int):
        del bits[:count]
        return bits

    def getVersion(bits:str, stream:str):
        if len(bits) < 3:
            bits, stream = getNextByte(bits, stream)
        id = ("".join([bits[0],bits[1],bits[2]]))
        bits = deleteBits(bits,3)
        ret = binaryToDecimal(id)
        global ans
        ans+=ret
        #print("Ver %d" % ret)
        return ret,bits, stream

    def getType(bits:str, stream:str):
        if len(bits) < 3:
            bits, stream = getNextByte(bits, stream)
        type = ("".join([bits[0],bits[1],bits[2]]))
        bits = deleteBits(bits,3)
        ret = binaryToDecimal(type)
        #print("Type %d" % ret)
        return ret,bits,stream

    def getOperatorType(bits:str, stream:str):
        if len(bits) < 1:
            bits, stream = getNextByte(bits,stream)       
        type = ("".join([bits[0]]))
        bits = deleteBits(bits,1)

        return binaryToDecimal(type),bits,stream,1

    def getOperatorLength(bits:str, stream:str, length:int):
        data = []
        readBits = 0
        
        while len(bits) < length:
            bits, stream = getNextByte(bits,stream)

        for i in range(length):
            data.append( bits[0] )
            bits = deleteBits(bits,1)
            readBits += 1
        
        data = ''.join(data)
        return binaryToDecimal(data), bits, stream, readBits

    def getNextByte(bits:str, steam:str):
        
        if len(steam) <= 0:
            return bits,steam

        s = str(hexToBinary( steam[0] ))
        for c in s:
            bits.append(c)
        steam = steam[1:len(steam)]

        s = str(hexToBinary( steam[0] ))
        for c in s:
            bits.append(c)
        steam = steam[1:len(steam)]

        return bits,steam

    def getLiteral(bits:str,stream:str):
        data = []
        while True:
            if len(bits) <= 0:
                bits, stream = getNextByte(bits,stream)         

            flag = int(("".join([bits[0]])))
            bits = deleteBits(bits,1)
            
            if len(bits) < 4:
                bits, stream = getNextByte(bits,stream)
            
            for i in range(4):
                data.append( bits[0] )
                bits = deleteBits(bits,1)

            if flag == 0:           
                data = ''.join(data)
                return binaryToDecimal(data), bits, stream

    def getOperator(bits:str, stream:str):
        length = 0
        readBits = 0
        type, bits, stream, read = getOperatorType(bits, stream)
        readBits+=read

        if type == 0:
            length, bits, stream, read = getOperatorLength(bits,stream,15)
            readBits += read
            data, bits, stream, read = getDataWithLength(bits,stream,length)
            readBits += read
        
        elif type == 1:            
            length, bits, stream, read = getOperatorLength(bits,stream,11)
            readBits += read
            output = []
            for i in range(length):
                data, bits, stream, read = getDataPacket(bits, stream)          
                readBits += read
                output.append(data)                
            return output, bits, stream, readBits
        else:
            print("Type Unknown %d" % type)
            exit(0)

        return data, bits, stream, readBits

    def getDataPacket(bits:str, stream:str):
        data = []
        readBits = 0
        id, bits, stream = getVersion(bits,stream)    
        type, bits, stream = getType(bits,stream)
        readBits += 6

        if type == 4:        
            while True:
                if len(bits) <= 0:
                    bits, stream = getNextByte(bits,stream)         

                flag = int(("".join([bits[0]])))
                bits = deleteBits(bits,1)
                readBits+=1
                if len(bits) < 4:
                    bits, stream = getNextByte(bits,stream)
            
                for i in range(4):
                    data.append( bits[0] )
                    bits = deleteBits(bits,1)
                readBits+=4
                if flag == 0:              
                    data = ''.join(data)
                    return binaryToDecimal(data), bits, stream, readBits
        else:
            output = 0
            if type == 0: # add
                data,bits,stream,read= getOperator(bits,stream)
                output = sum(data)
            elif type == 1: # pruduct
                data,bits,stream,read= getOperator(bits,stream)
                result = 1
                for x in data:
                    result = result * x
                output = result
            elif type == 2: # min
                data,bits,stream,read= getOperator(bits,stream)
                output = (min(data))
            elif type == 3: # max
                data,bits,stream,read= getOperator(bits,stream)
                output = (max(data))
            elif type == 5: # > then ? 1 : 0
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] > data[1] :
                    output = 1
            elif type == 6: # < then ? 1 : 0
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] < data[1] :
                    output = 1 
            elif type == 7: # ==
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] == data[1]:
                    output = 1
            else:
                print("error")

            readBits+=read

        return output,bits,stream,readBits
    
    def getDataWithLength(bits:str,stream:str,length:int):
        outData = []
        data = []
        readBits = 0
        while readBits < length:
            read = 0
            data,bits,stream,read = getDataPacket( bits, stream )
            readBits += read
            outData.append(data)

        return outData, bits, stream, readBits

    def parse(stream:str):
        bits = []        
        ret = []

        while len(bits) > 0 or len(stream) > 0:

            _, bits, stream = getVersion(bits, stream)
            type, bits, stream = getType(bits, stream)

            if type == 0: # add
                data,bits,stream,read= getOperator(bits,stream)
                ret.append(sum(data))
            elif type == 1: # pruduct
                data,bits,stream,read= getOperator(bits,stream)
                result = 1
                for x in data:
                    result = result * x
                ret = result
            elif type == 2: # min
                data,bits,stream,read= getOperator(bits,stream)
                ret.append(min(data))
            elif type == 3: # max
                data,bits,stream,read= getOperator(bits,stream)
                ret.append(max(data))
            elif type == 4: # single number 
                data, bits, stream = getLiteral(bits, stream)          
                ret.append(data)
            elif type == 5: # > then ? 1 : 0
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] > data[1] :
                    ret.append(1)
                else:
                    ret.append(0)
            elif type == 6: # < then ? 1 : 0
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] < data[1] :
                    ret.append(1)
                else:
                    ret.append(0)
            elif type == 7: # ==
                data,bits,stream,read= getOperator(bits,stream)
                if data[0] == data[1]:
                    ret.append(1)
                else:
                    ret.append(0)
            else:
                print("error")
                data,bits,stream,read= getOperator(bits,stream)              

            # we done.. clear zero pads..            
            bits = []

        return ret

    for line in lines:
        ret = parse(line)    
    return ret

print("Answer2 %s" % challenge1())