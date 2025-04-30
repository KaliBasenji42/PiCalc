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
  

def splitFracStr(string): # Splits a string by the first "."
  
  index = string.find('.')
  
  if index == 0: return '0', string[1:]
  if index < 0: return string, '0'
  
  return string[:index], string[index+1:]
  

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
      raise Exception('Non-numeric value')
      # Throw if either not numeric
    
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
  

def strSubInt(str1, str2): # Subtracts 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  # Note: str1 must > str2
  
  # Make equal length
  
  while len(str1) < len(str2):
    str1 = '0' + str1
  
  while len(str1) > len(str2):
    str2 = '0' + str2
  
  DBStr = 'strAdd: \n  ' + str1 + ' -\n  ' + str2 + ' =\n '
  # Debug string
  DBStrC = '' # Debug string for carry
  
  # Compute
  
  out = ''
  carry = 0
  
  for i in range(len(str1)):
    
    i = i + 1
    
    if not str1[-i].isnumeric() or not str2[-i].isnumeric():
      raise Exception('Non-numeric value')
      # Throw if either not numeric
    
    sumDig = int(str1[-i]) - int(str2[-i]) - carry
    # Add current digits & carry
    
    out = str(sumDig % 10) + out
    # Add digit to out
    
    carry = 0
    if sumDig < 0: carry = 1
    # Carry over
    
    DBStrC = str(carry)[0] + DBStrC # Debug
    
  
  # Debug
  
  DBStr = DBStr + DBStrC + '\n  ' + out
  logging.debug(DBStr)
  
  # Return
  
  return out, carry > 0
  # Return output and if it underflowed
  

def strSum(str1, str2): # Uses strAddInt and strSubInt to sum 2 strings as if they where floats
  # Format: "-###.###..." (Any float, may be negative)
  
  try: # Throw if non-numeric
    float(str1)
    float(str2)
  except:
    raise Exception('Non-numeric value')
  
  str1 = splitFracStr(str1)
  str2 = splitFracStr(str2)
  
  if str1[0][0] == '-' and str2[0][0] == '-': # Both negative
    
    # Calculate
    
    fracResult = strAddInt(str1[1], str2[1])
    intResult = strAddInt(str1[0][1:], str2[0][1:])
    
    if fracResult[1]: intResult = strAddInt(intResult, '1')
    
    # Out
    
    return '-' + intResult[0] + '.' + fracResult[0]
    
  
  elif str1[0] == '-': # str1 negative
    
    pass
    
  

print(strSum('-1.', '-1.0'))

### Step Functions ###

### Pre-Loop ###

### Main Loop ###

try:
  
  while run:
    
    break
    
  

except Exception as e:
  logging.exception(e)
  print('\033[97;41mFatal Error\033[0m')
