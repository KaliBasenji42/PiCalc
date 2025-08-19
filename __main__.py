### Import ###

import sys
import time
import select
import logging

logging.basicConfig(
    level=logging.DEBUG,
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

def strAddInt(str1, str2, frac = False): # Adds 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  # If Frac is set to True, it will format the strings as if they are fractional
  
  # Make equal length
  
  while len(str1) < len(str2):
    if frac: str1 = str1 + '0'
    else: str1 = '0' + str1
  
  while len(str1) > len(str2):
    if frac: str2 = str2 + '0'
    else: str2 = '0' + str2
  
  DBStr = 'strAddInt: \n  ' + str1 + ' +\n  ' + str2 + ' =\n '
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
  

def strSubInt(str1, str2, frac = False): # Subtracts 2 strings as if they where positive integers
  # Format: "...###" (Any positive integer)
  # Note: str1 must > str2
  # If Frac is set to True, it will format the strings as if they are fractional
  
  # Make equal length
  
  while len(str1) < len(str2):
    if frac: str1 = str1 + '0'
    else: str1 = '0' + str1
  
  while len(str1) > len(str2):
    if frac: str2 = str2 + '0'
    else: str2 = '0' + str2
  
  DBStr = 'strSubInt: \n  ' + str1 + ' -\n  ' + str2 + ' =\n '
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
    
    fracResult = strAddInt(str1[1], str2[1], frac = True) # Factional digits
    intResult = strAddInt(str1[0][1:], str2[0][1:]) # Interger Digits
    
    if fracResult[1]: # If frac. digits overflow
      fracResult = (fracResult[0][1:], True) # Remove first digit from frac. digits
      intResult = strAddInt(intResult[0], '1') # Add 1 to int. digits
    
    # Debug
    
    logging.debug('strSum:\n  ' +
                  str1[0] + '.' + str1[1] + ' +\n  ' +
                  str2[0] + '.' + str2[1] + ' =\n  ' +
                  '-' + intResult[0] + '.' + fracResult[0])
    
    # Out
    
    return '-' + intResult[0] + '.' + fracResult[0]
    
  
  elif str1[0][0] == '-' or str2[0][0] == '-': # 1 negative
    
    # Variiables
    
    fracUF = False # Fractional digitis underflow (should subtract 1 from int. digits)
    
    sign = '' # Sign of output
    
    # Define negative and positive string
    
    if str1[0][0] == '-':
      strNeg = str1
      strPos = str2
    else:
      strNeg = str2
      strPos = str1
    
    # Calculate
    
    fracResult = strSubInt(strPos[1], strNeg[1][1:], frac = True) # Factional digits
    intResult = strSubInt(strPos[0], strNeg[0][1:]) # Interger Digits
    
    if fracResult[1]: # If frac. digits underflow
      fracResult = (strSubInt(strPos[1], strNeg[1]), True) # Re-calc. frac
      intResult = strStrInt(intResult[0], '1') # Subtract 1 from int. digits
      fracUF = True
    
    if intResult[1]: # If int. digits underflow
      intResult = strSubInt(strNeg[0][1:], strPos[0]) # Re-calc. int
      if fracUF: intResult = strAddInt(intResult[0], '1') # Subtract 1 from int. digits
      sign = '-' # Change sign
      
    
    # Debug
    
    logging.debug('strSum:\n  ' +
                  strPos[0] + '.' + strPos[1] + ' -\n  ' +
                  strNeg[0][1:] + '.' + strNeg[1] + ' =\n  ' +
                  sign + intResult[0] + '.' + fracResult[0])
    
    # Out
    
    return sign + intResult[0] + '.' + fracResult[0]
    
  
  else: # Both positive
    
    # Calculate
    
    fracResult = strAddInt(str1[1], str2[1], frac = True) # Factional digits
    intResult = strAddInt(str1[0], str2[0]) # Interger Digits
    
    if fracResult[1]: # If frac. digits overflow
      fracResult = (fracResult[0][1:], True) # Remove first digit from frac. digits
      intResult = strAddInt(intResult[0], '1') # Add 1 to int. digits
    
    # Debug
    
    logging.debug('strSum:\n  ' +
                  str1[0] + '.' + str1[1] + ' +\n  ' +
                  str2[0] + '.' + str2[1] + ' =\n  ' +
                  intResult[0] + '.' + fracResult[0])
    
    # Out
    
    return intResult[0] + '.' + fracResult[0]
    
  

### Step Functions ###

### Pre-Loop ###

# License

print(
  'PiCalc\n'
  'Copyright (C) 2025 KaliBasenji42\n'
  '\n'
  'This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.\n'
  '\n'
  'This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n'
  '\n'
  'You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.\n'
  '\n'
  'Attached License: LICENSE.md\n'
  'GPL v2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html\n'
  'KaliBasenji42\'s Github: https://github.com/KaliBasenji42\n'
)

print(strSum('0.99', '9.01'))

### Main Loop ###

try:
  
  while run:
    
    break
    
  

except Exception as e:
  logging.exception(e)
  print('\033[97;41mFatal Error\033[0m')
