# PiCalc
# Copyright (C) 2026 KaliBasenji42

# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# License: ../LICENSE.md
# GPL v2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
# KaliBasenji42's Github: https://github.com/KaliBasenji42

### Imports ###

import os
import time
import random
import json
import math
import fractions
import decimal
import logging

logging.basicConfig(
  level=logging.WARNING,
  format='%(asctime)s | %(filename)s:%(lineno)s | %(levelname)s: %(message)s',
  filename='app.log'
)
logging.debug('New Run')

### Variables ###

# Files

configPath = 'config.json' # Path to config file

# Control

spt = 1/4 # Second per tick
tick = 0 # Time ticker
tickTime = time.time() # Time tick started for spt

start = time.time() # Start time
tickStart = time.time() # Start time for tick
actualTps = 0 # Actual ticks per second for info

# Calculation

piFrac = fractions.Fraction(0, 1) # Fraction for storing pi approximation
piDec = decimal.Decimal('0') # Decimal representation of pi approximation
piDecPrev = decimal.Decimal('0') # Old decimal representation of pi approximation

method = '' # Method used for calculating pi

digitStabilities = [] # Array of how recently a digit changed 
# 0 is most stable, starts at threshold and subtracts
stabilityThreshold = 8 # How long a digit has to stay the same to be considered stable
digitBuffer = 16 # Digits calculated after last consecutive stable digit
stableDigits = 0 # Number of consecutive stable digits
digits = 16 # Number of digits to calculate to

piNumerator = 0 # piFrac numerator for some calculations
piDenominator = 0 # piFrac denominator for some calculations

### Functions ###

# File

def readConfig(): # Read config file
  
  # Variables
  
  global spt
  
  global method
  global stabilityThreshold
  global digitBuffer
  global digits
  
  # Read Files
  
  with open(configPath, 'r') as file: data = json.loads(file.read())
  
  # Set variables
  
  spt = 1 / data['tps']
  
  method = data['method']
  stabilityThreshold = data['stabilityThreshold']
  digitBuffer = data['digitBuffer']
  digits = data['digitBuffer'] # Initial value
  

# Calculation

def GregoryLeibniz(n):
  
  global piFrac
  
  piFrac += fractions.Fraction(
    ((-1) ** n) * 4,
    2 * n + 1
  )
  
  #logging.debug(piFrac)
  

def BaileyBorweinPlouffe(n):
  
  global piFrac
  
  piFrac += (
    fractions.Fraction(1,16 ** n) * (
      fractions.Fraction(4, 8 * n + 1) -
      fractions.Fraction(2, 8 * n + 4) -
      fractions.Fraction(1, 8 * n + 5) -
      fractions.Fraction(1, 8 * n + 6)
    )
  )
  

def RandomCircle(n):
  
  global piFrac
  global piNumerator
  global piDenominator
  
  x = random.random()
  y = random.random()
  
  num = 0 # Numerator
  
  if math.sqrt(x ** 2 + y ** 2) <= 1: # Within circle
    num = 4 # Numerator += 4
  
  
  piNumerator += num # Add
  piDenominator += 1 # Iterations
  
  piFrac = fractions.Fraction(
    piNumerator,
    piDenominator
  ) # Set
  

def EulersNumber(n):
  
  global piFrac
  
  piFrac += fractions.Fraction(
    1,
    math.factorial(n)
  )
  

def AperyConstant(n):
  
  global piFrac
  
  piFrac += fractions.Fraction(
    1,
    n ** 3
  )
  

def GoldenRatio(n):
  
  global piFrac
  
  if piFrac.numerator == 0:
    piFrac = fractions.Fraction(1, 1)
    return
  
  piFrac = 1 + fractions.Fraction(
    piFrac.denominator,
    piFrac.numerator
  )
  

def GoldenRatioFibonacci(n):
  
  global piFrac
  global piNumerator
  global piDenominator
  
  fib = piNumerator + piDenominator
  piDenominator = piNumerator
  piNumerator = fib
  
  if piNumerator == 0: piNumerator = 1
  if piDenominator == 0: piDenominator = 1
  
  piFrac = fractions.Fraction(
    piNumerator,
    piDenominator
  )
  

def GoldenRatioLucas(n):
  
  global piFrac
  global piNumerator
  global piDenominator
  
  fib = piNumerator + piDenominator
  piDenominator = piNumerator
  piNumerator = fib
  
  if piNumerator == 0: piNumerator = 1
  if piDenominator == 0: piDenominator = 2
  
  piFrac = fractions.Fraction(
    piNumerator,
    piDenominator
  )
  

# Decimal / Digit

def digitStr(string): # Returns string with only numeric values
  
  out = ''
  
  for char in string:
    if char.isnumeric():
      out += char
    
  
  return out
  

def getWholeDigits(string): # Returns number of digits before decimal
  
  out = 0
  
  for char in string:
    if char.isnumeric():
      out += 1
    elif char == '.':
      break
  
  return out
  

def getStableDigits(stabilities): # Returns how many digits are consecutively stable
  
  out = 0
  
  for stab in stabilities:
    if stab == 0:
      out += 1
    else:
      break
  
  return out
  

def generateDigitStabilities(dec, decPrev):
  
  global digitStabilities
  
  # Digit Strings
  
  decDigits = digitStr(str(dec))
  decDigitsPrev = digitStr(str(decPrev))
  
  # Lengthen
  
  for i in range(len(decDigits) - len(decDigitsPrev)):
    decDigitsPrev += '0'
  
  for i in range(len(decDigits) - len(digitStabilities)):
    digitStabilities.append(stabilityThreshold)
  
  # Check
  
  for i in range(len(decDigits)):
    
    if(decDigits[i] == decDigitsPrev[i]): # Match 
      
      digitStabilities[i] = max(0, digitStabilities[i] - 1) # -1, min 0
      
    else: # Else
      
      digitStabilities[i] = stabilityThreshold # Reset
      
    
  

# Rendering

def hue(x, fMin = 0, fMax = 255): # Returns hue color
  
  # Variables
  
  fRange = fMax - fMin # Function range
  
  # RGB
  
  # Based off of:
  # f(x) = -| ( ( x + n r ) % 6r ) -3r | + 2r + m
  #   where: 
  #     "n" depends on wether its red, green, or blue:
  #       red: -3
  #       green: 1
  #       blue: -1
  #     "r" is range ( max - min )
  #     "m" is min
  # f(x) is clamped to min and max: max( min( f(x), max ), min ) 
  
  red = x - ( 3 * fRange ) # Subtract 3 Range
  red = red % ( 6 * fRange ) # Mod 6 Range
  red = red - ( 3 * fRange ) # Subtract 3 Range
  red = -abs(red) # - abs
  red = red + ( 2 * fRange ) # Add 2 Range
  red = red + fMin # Add min
  red = min( red, fMax ) # min
  red = max( red, fMin ) # max
  red = str(int(red)) # Str of int
  
  green = x + ( fRange ) # Add 1 Range
  green = green % ( 6 * fRange ) # Mod 6 Range
  green = green - ( 3 * fRange ) # Subtract 3 Range
  green = -abs(green) # - abs
  green = green + ( 2 * fRange ) # Add 2 Range
  green = green + fMin # Add min
  green = min( green, fMax ) # min
  green = max( green, fMin ) # max
  green = str(int(green)) # Str of int
  
  blue = x - ( fRange ) # Subtract 1 Range
  blue = blue % ( 6 * fRange ) # Mod 6 Range
  blue = blue - ( 3 * fRange ) # Subtract 3 Range
  blue = -abs(blue) # - abs
  blue = blue + ( 2 * fRange ) # Add 2 Range
  blue = blue + fMin # Add min
  blue = min( blue, fMax ) # min
  blue = max( blue, fMin ) # max
  blue = str(int(blue)) # Str of int
  
  # Return
  
  return '\033[38;2;' + red + ';' + green + ';' + blue + 'm'
  

def render():
  
  screen = '' # What to print
  
  # Title
  
  screen += '(C) 2026 KaliBasenji42 - GPL v2 | Keyboard Interrupt to Quit [Ctrl + C]\n'
  
  # Pi
  
  piStr = '' # String for pi
  
  index = 0 # Index for \/
  
  for char in str(piDec):
    
    if char.isnumeric():
      
      stability = digitStabilities[index]
      
      hueVal = 2 * 255 # Green
      hueVal -= (stability / stabilityThreshold) * (2 * 255) # Stability 0-1 * Green (Green - Red)
      
      if stability == 0: hueVal = 3 * 255 # Cyan
      
      piStr += hue(hueVal) # Color
      
      piStr += char # Character
      
      piStr += '\033[0m' # Reset
      
      index += 1 # Iterate
      
    
    else: # Not number
      
      piStr += char # Add
      
    
  
  screen += piStr + '\n'
  
  # Info
  
  screen += '\033[94mTick: ' + str(tick) + ' | '
  screen += '' + str(round(time.time() - start, 4)) + ' s | '
  screen += str(round(actualTps, 4)) + ' tps\033[0m\n'
  
  screen += '\033[95mStable Digits: ' + str(stableDigits) + '\033[0m\n'
  
  # Clear and Print
  
  os.system('clear') # Clear
  
  print(screen, end='') # Print Screen
  

### Main Loop ###

# Pre-Loop

readConfig()

# Main Definition

def main():
  
  # Global Variables
  
  global spt
  global tick
  global tickTime
  global start
  global tickStart
  global actualTps
  
  global piFrac
  global piDec
  global piDecPrev
  global digitStabilities
  global digits
  global stableDigits
  
  # Main Loop
  
  start = time.time() # Start time
  
  while True:
    
    ### Clock ###
    
    tickStart = time.time() # Start of tick
    
    tick += 1 # Iterate time ticker
    
    elapsed = time.time() - tickTime # Time since last frame
    time.sleep(max(0.001, spt - elapsed)) # Pause
    tickTime = time.time() # Update frame time
    
    ### Calculate ###
    
    # Function Calls
    
    if(method == 'Gregory–Leibniz'):
      GregoryLeibniz(tick-1)
    elif(method == 'Bailey–Borwein–Plouffe'):
      BaileyBorweinPlouffe(tick-1)
    elif(method == 'Random Circle'):
      RandomCircle(tick)
    elif(method == "Euler's Number"):
      EulersNumber(tick-1)
    elif(method == "Apéry's Constant"):
      AperyConstant(tick)
    elif(method == 'Golden Ratio'):
      GoldenRatio(tick)
    elif(method == 'Golden Ratio-Fibonacci'):
      GoldenRatioFibonacci(tick)
    elif(method == 'Golden Ratio-Lucas'):
      GoldenRatioLucas(tick)
    
    # Decimal
    
    decimal.getcontext().prec = digits # Set precision
    
    piDecPrev = piDec # Prev
    piDec = decimal.Decimal(piFrac.numerator) / decimal.Decimal(piFrac.denominator) # New
    
    generateDigitStabilities(piDec, piDecPrev)
    stableDigits = getStableDigits(digitStabilities)
    
    digits = stableDigits - getWholeDigits(str(piDec)) + digitBuffer # Re-calculate digit precision
    
    #logging.debug('Frac: ' + str(piFrac))
    #logging.debug('Dec: ' + str(piDec))
    #logging.debug('Stabilities: ' + str(digitStabilities))
    #logging.debug('Digits: ' + str(digits))
    
    ### Render ###
    
    try: render()
    except KeyboardInterrupt: # Exit
      
      logging.info('Keyboard Interrupt') # Logging
      print('\033[92m\nKeyboard Interrupt - Exiting\033[0m')
      quit()
      
    except: logging.exception('Rendering Error')
    
    actualTps = 1 / (time.time() - tickStart) # Actual ticks per second
    
  

# Try Wrapper

try:
  main()
except KeyboardInterrupt: # Exit
  
  logging.info('Keyboard Interrupt') # Logging
  print('\033[92m\nKeyboard Interrupt - Exiting\033[0m')
  quit()
  
except Exception as e:
  
  logging.exception('Fatal Error') # Log
  
  # Error message
  print('\033[97;41mFatal Error\033[0m')
  
