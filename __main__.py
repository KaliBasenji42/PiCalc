### Import ###

import sys
import time
import select
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
method = 0 # Method for calculating pi. 0: Nilakantha, 1: BBP

piStr = '' # Apprx of pi, stored as string

### (Basic) Functions ###

def detectKey(): # Detects key press (used for exiting graph loop)
  
  if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    key = sys.stdin.read(1)
    return key
  
  return None
  

### String Based Math Functions ###

def strAddInt(str1, str2): # Adds 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  
  # Make equal length
  
  while len(str1) < len(str2):
    str1 = '0' + str1
  
  while len(str1) > len(str2):
    str2 = '0' + str2
  
  DBStr = 'strAdd: \n  ' + str1 + ' +\n  ' + str2 + ' =\n '
  # Debug string
  DBStrC = '' # Debug string for carry
  
  # Compute
  
  out = ''
  carry = 0
  
  for i in range(len(str1)):
    
    i = i + 1
    
    if not str1[-i].isnumeric() or not str2[-i].isnumeric():
      raise Exception('None numeric value')
      # Throw if either not numeric
    
    logging.debug(str1[-i] + ', ' + str2[-i] + ', ' + str(carry))
    
    sumDig = int(str1[-i]) + int(str2[-i]) + carry
    # Add current digits & carry
    
    out = str(sumDig % 10) + out
    # Add digit to out
    
    carry = sumDig // 10 # Carry over
    
    DBStrC = str(carry)[0] + DBStrC # Debug
    
  
  # Final Carry
  
  if carry > 0: out = str(carry) + out
  
  # Debug
  
  if carry > 0: DBStr = DBStr + DBStrC + '\n ' + out
  else: DBStr = DBStr + DBStrC + '\n  ' + out
  logging.debug(DBStr)
  
  # Return
  
  return out, carry > 0
  # Return output and if it carried
  

def strSubInt(str1, str2): # Adds 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  
  # Make equal length
  
  while len(str1) < len(str2):
    str1 = '0' + str1
  
  while len(str1) > len(str2):
    str2 = '0' + str2
  
  DBStr = 'strAdd: \n  ' + str1 + ' +\n  ' + str2 + ' =\n '
  # Debug string
  DBStrC = '' # Debug string for carry
  
  # Compute
  
  out = ''
  carry = 0
  
  for i in range(len(str1)):
    
    i = i + 1
    
    if not str1[-i].isnumeric() or not str2[-i].isnumeric():
      raise Exception('None numeric value')
      # Throw if either not numeric
    
    logging.debug(str1[-i] + ', ' + str2[-i] + ', ' + str(carry))
    
    sumDig = int(str1[-i]) - int(str2[-i]) - carry
    # Add current digits & carry
    
    out = str(sumDig % 10) + out
    # Add digit to out
    
    carry = (-sumDig + 10) // 10 # Carry over
    
    DBStrC = str(carry)[0] + DBStrC # Debug
    
  
  # Debug
  
  DBStr = DBStr + DBStrC + '\n  ' + out
  logging.debug(DBStr)
  
  # Return
  
  return out, carry > 0
  # Return output and if it carried
  

print(strSubInt('100', '1'))

### Step Functions ###

### Pre-Loop ###

### Main Loop ###

try:
  
  while run:
    
    break
    
  

except Exception as e:
  logging.exception(e)
  print('\033[97;41mFatal Error\033[0m')
