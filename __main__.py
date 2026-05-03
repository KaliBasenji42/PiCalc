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
import fractions
import decimals
import logging

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s | %(filename)s:%(lineno)s | %(levelname)s: %(message)s',
  filename='app.log'
)
logging.debug('New Run')

### Variables ###

# Files

configPath = 'config.json' # Path to config file

# Control

run = True # Run Main Loop
spc = 1/4 # Second per Calculation
tick = 0 # Time ticker
calcTime = time.time() # Time calc started for spc

# Calculation

piFrac = fractions.Fraction() # Fraction for storing pi approximation
piDec = decimals.Decimal('0') # Decimal representation of pi approximation
piDecPrev = decimals.Decimal('0') # Old decimal representation of pi approximation

method = '' # Method used for calculating pi

digitStabilities = [] # Array of how recently a digit changed
stabilityThreshold = 8 # How long a digit has to stay the same to be considered stable
digitBuffer = 16 # Digits calculated after last consecutive stable digit

### Functions ###

# File

def readConfig(): # Read config file
  
  # Variables
  
  global spc
  
  global method
  global stabilityThreshold
  global digitBuffer
  
  # Read Files
  
  with open(configPath, 'r') as file: data = json.loads(file.read())
  
  # Set variables
  
  spc = 1 / data['cps']
  
  method = data['method']
  stabilityThreshold = data['stabilityThreshold']
  digitBuffer = data['digitBuffer']
  

# Calculation


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
  
  screen += '(C) 2026 KaliBasenji42 - GPL v2 | Keyboard Interrupt to quit [ctrl + C]' # Title
  
  screen += hue(0)
  
  screen += 'Time: ' + ticker + '\n' # Info
  
  os.system('clear') # Clear
  
  print(screen, end='') # Print Screen
  

### Main Loop ###

def main():
  
  # Global Variables
  
  global run
  global spc
  global tick
  global calcTime
  
  global piFrac
  global piDec
  global piDecPrev
  global digitStabilities
  
  # Main Loop
  
  while run:
    
    # Clock
    
    tick += 1 # Iterate time ticker
    
    elapsed = time.time() - calcTime # Time since last frame
    time.sleep(max(0, spc - elapsed)) # Pause
    calcTime = time.time() # Update frame time
    
    # Calculate
    
    
    
    # Render
    
    render()
    
  

# Try: Wrapper

try:
  main()
except Exception as e:
  
  logging.exception('Fatal Error') # Log
  
  # Error message
  print('\033[97;41mFatal Error\033[0m')
  
