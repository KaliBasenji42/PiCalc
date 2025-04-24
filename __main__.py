import time

# Variables

inp = 0

# Functions

def strToInt(string):
    
    intStr = '0'
    
    string = string + ' '
    
    for char in string:
        
        if char.isnumeric(): intStr = intStr + char
        
    
    num = int(intStr)
    
    if string[0] == '-': num = num * -1
    
    return num
    

def strShift(string, shift):
    
    out = ''
    
    for i in range(len(string)):
        
        if 0 <= i + shift < len(string): out += string[i + shift]
        
        else: out += '0'
        
    
    return out
    

def numToStr(num, digits):
    
    num = str(num)
    
    out = ''
    
    for char in num:
        
        if char.isnumeric(): out += char
        
    
    if len(out) >= digits: out = out[:digits]
    
    for i in range(digits - len(out)): out += '0'
    
    return out
    

def longDivision(dividend, divisor):
    
    return (numToStr(dividend / divisor), 0)
    

def addStr(str1, str2, shift):
    
    out = ''
    
    str1 = shiftStr(str1, shift)
    
    for i in range(len(str1)):
        
        if i + shift < len(str2):
            
            out += str(int(str1[i]) + int(str2[i + shift]))
            
        
        else: out += str1[i]
        
    
    return out
    

def printCorrectDigits(string, shift, prev, prevShift, dot):
    
    out = 0
    
    dif = shift - prevShift
    
    if dif < 0: 
        
        print('Err!')
        
        return 0
        
    
    else:
        
        prev = prev[dif:]
        
    
    for i in range(min(len(prev),len(prev))):
        
        if prev[i] == string[i]:
            
            out += 1
            
            print(prev[i], end = '')
            
            if i + shift == dot: print('.', end = '')
            
        
    
    return out
    

def BBPStep(aprx, digtit, k):
    
    val = 4 / (8*k + 1)
    val -= 2 / (8*k + 4)
    val -= 1 / (8*k + 5)
    val -= 1 / (8*k + 6)
    val = val / (16 ** k)
    
    aprx += val * (10 ** digits)
    
    return aprx
    

def GLSStep(aprx, digits, k):
    
    val = -((2 * k) + 1) * ((k % 2) * 2 - 1)
    
    aprx += 4 / val * (10 ** digits)
    
    return aprx
    

def NilakanthaStep(aprx, digits, k):
    
    div = -((k*2) * ((k*2) + 1) * ((k*2) + 2)) * ((k % 2) * 2 - 1)
    
    if k == 0: div = 3 / 4
    
    aprx += 4 / div * (10 ** digits)
    
    return aprx
    

def step(aprx, shift, k):
    
    div = -((k*2) * ((k*2) + 1) * ((k*2) + 2)) * ((k % 2) * 2 - 1)
    
    if k == 0: div = 3 / 4
    
    aprx 
    
    

def piDigit(n):
    
    k = 0
    
    digits = ''
    
    shift = 0 # Currect Number if Digits
    
    while k < n:
        
        prev = digits
        
        prevShift = shift
        
        # Calc
        
        digits = step(digits, shift , k)
        
        # Currect Digit Calc
        
        shift += printCorrectDigits(digits, shift, prev, prevShift, 1)
        
        # Loop
        
        k += 1
        
        
    if digits == '': print('"n" to small :/')
    else: print('')
    

# Main Loop

while True:
    
    inp = strToInt(input('\nInput: '))
    
    piDigit(inp)
    