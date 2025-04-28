### Import ###

import sys
import time
import termios
import tty
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s | %(levelname)s: %(message)s',
    filename='app.log'
)
logging.debug('New Run: ')

### Variables ###

run = True # Run Main Loop
pastKeys = [''] * 4 # To detect if a key was an arrow/escape key, and sould not be returned

piStr = '' # Apprx of pi, stored as string

### (Basic) Functions ###

def getKey(): # Get key from terminal input
  
  global pastKeys
  
  fd = sys.stdin.fileno()
  old = termios.tcgetattr(fd) # Old terminal settings
  
  try:
    tty.setraw(sys.stdin.fileno()) # Terminal to raw (non-conical & no echo)
    
    chr = sys.stdin.read(1) # Get char entered
    
    pastKeys = roll(pastKeys, chr) # Roll chr into pastKeys
    
    shouldReturn = False # Should it return chr?
    if pastKeys[-2] != '[': shouldReturn = True
    elif pastKeys[-3] != '\x1b': shouldReturn = True
    
    logging.debug('Key Press: ' + chr + ' (shouldReturn: ' + str(shouldReturn) + ', ' + str(pastKeys) + ')') # Logging
    
    if shouldReturn: return chr # Return
    return '' # Base case
    
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old) # Restore terminal settings
  

### String Based Math Functions ###

def strAddInt(str1, str2): # Adds 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  
  # Make equal length
  
  while len(str1) < len(str2):
    str1 = '0' + str1
  
  while len(str1) > len(str2):
    str2 = '0' + str2
  
  DBStr = 'strAdd: \n  ' + str1 + ' +\n  ' + str2 + ' =\n  '
  # Debug string
  
  # Compute
  
  out = ''
  carry = 0
  
  for i in range(len(str1)):
    
    if not str1[-i].isnumeric() or not str1[-i].isnumeric():
      continue
      # Skip if either not numeric
    
    sumDig = int(str1[-i]) + int(str2[-i]) + carry
    # Add current digits
    
    out = strint((sumDig % 10)) + out
    # Add digit to out
    
    carry = sumDig // 10
    # Carry over
    
  
  # Final Carry
  
  if carry > 0: out = str(carry) + out
  
  # Debug
  
  DBStr = DBStr + out
  logging.debug(DBStr)
  
  # Return
  
  return out
  

print(strAdd('1', '1'))

### Step Functions ###

### Pre-Loop ###

### Main Loop ###

try:
  
  while run:
    
    pass
    
  

except Exception as e:
  logging.exception(e)
  print('\033[97;41mFatal Error\033[0m')
