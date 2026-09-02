# PiCalc - Calculation Module
# Copyright (C) 2026 KaliBasenji42

# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# License: ../LICENSE.md
# GPL v2: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
# KaliBasenji42's Github: https://github.com/KaliBasenji42

# Imports

import fractions
import random
import math

# Variables

piFrac = fractions.Fraction(0, 1) # Fraction for storing pi approximation
piNumerator = 0 # piFrac numerator for some calculations
piDenominator = 0 # piFrac denominator for some calculations

# Calculation
# Note that n starts at 1

def GregoryLeibniz(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    ((-1) ** n) * 4,
    2 * n + 1
  )
  

def BaileyBorweinPlouffe(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += (
    fractions.Fraction(1,16 ** n) * ( # Add fraction
      fractions.Fraction(4, 8 * n + 1) -
      fractions.Fraction(2, 8 * n + 4) -
      fractions.Fraction(1, 8 * n + 5) -
      fractions.Fraction(1, 8 * n + 6)
    )
  )
  

def RandomCircle(n, args=[]):
  
  global piFrac # 0/1
  global piNumerator # 0
  global piDenominator # 0
  
  x = random.random() # Random x
  y = random.random() # Random y
  
  num = 0 # Numerator
  
  if math.sqrt(x ** 2 + y ** 2) <= 1: # Within circle
    num = 4 # Numerator += 4
  
  
  piNumerator += num # Add
  piDenominator += 1 # Iterations
  
  piFrac = fractions.Fraction( # Set fraction
    piNumerator,
    piDenominator
  )
  

def EulersNumber(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    math.factorial(n)
  )
  

def GoldenRatio(n, args=[]):
  
  global piFrac # 0/1
  
  if piFrac.numerator == 0: # If 0...
    piFrac = fractions.Fraction(1, 1) # Set to 1
    return # Exit
  
  piFrac = 1 + fractions.Fraction( # 1 + reciprocal of previous
    piFrac.denominator,
    piFrac.numerator
  )
  

def GoldenRatioFibonacci(n, args=[]):
  
  global piFrac # 0/1
  global piNumerator # 0
  global piDenominator # 0
  
  fib = piNumerator + piDenominator # Find Fibonacci iteration
  piDenominator = piNumerator # Denominator is previous Fibonacci
  piNumerator = fib # Numerator is new Fibonacci
  
  if piNumerator == 0: piNumerator = 1 # Start value
  if piDenominator == 0: piDenominator = 1 # Start value
  
  piFrac = fractions.Fraction( # Set fraction
    piNumerator,
    piDenominator
  )
  

def GoldenRatioLucas(n, args=[]):
  
  global piFrac # 0/1
  global piNumerator # 0
  global piDenominator # 0
  
  fib = piNumerator + piDenominator # Find Lucas iteration
  piDenominator = piNumerator # Denominator is previous Lucas
  piNumerator = fib # Numerator is new Lucas
  
  if piNumerator == 0: piNumerator = 1 # Start value
  if piDenominator == 0: piDenominator = 2 # Start value
  
  piFrac = fractions.Fraction( # Set fraction
    piNumerator,
    piDenominator
  )
  

def ln2(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    (-1) ** (n + 1),
    n
  )
  

def ln2BBP(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  if n == 0: # If start (prevent division by 0)
    piFrac = fractions.Fraction(2, 3) # Set to 2/3
    return # Exit
  
  piFrac += ( # Add fraction
    fractions.Fraction(1,2) *
    fractions.Fraction(1,16 ** n) * (
      fractions.Fraction(1, 2 * n) +
      fractions.Fraction(1, 4 * n + 1) +
      fractions.Fraction(1, 8 * n + 4) +
      fractions.Fraction(1, 16 * n + 12)
    )
  )
  

def root2(n, args=[]):
  
  n = n - 2 # Start at -1
  
  global piFrac # 0/1
  
  if n == -1: # If start (prevent multiplication by 0)
    piFrac = fractions.Fraction(1, 1) # Set to 1
    return # Exit
  
  piFrac = piFrac * fractions.Fraction( # Product fraction
    (4 * n + 2) ** 2,
    (4 * n + 1) * (4 * n + 3)
  )
  

def root2TaylorEuler(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    math.factorial(2 * n + 1),
    (2 ** (3 * n + 1)) * (math.factorial(n) ** 2)
  )
  

def ErdosBorweinConstant(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    (2 ** n) - 1
  )
  

def ErdosBorweinConstant2(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  if n == 0: # If start (+1)
    piFrac = fractions.Fraction(1, 1) # Set to 1
    return # Exit
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    (2 ** n) * ((2 ** n) - 1)
  )
  

def LiouvillesConstant(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    10 ** math.factorial(n)
  )
  

def CatalansConstant(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    - ((-4096) ** n) * (45136 * n ** 4 - 57184 * n ** 3 + 21240 * n ** 2 - 3160 * n + 165) * (math.factorial(2 * n) ** 6) * (math.factorial(3 * n) ** 3),
    1024 * (n ** 3) * ((2 * n - 1) ** 3) * (math.factorial(n) ** 3) * (math.factorial(6 * n) ** 3)
  )
  

def CahensConstant(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  global piDenominator # 0
  
  if n == 0: # If start
    piDenominator = 2 # Initiate Sylvester's sequence
  
  else: # Iterate Sylvester's sequence
    piDenominator = piDenominator * (piDenominator - 1) + 1
  
  piFrac += fractions.Fraction( # Add fraction
    (-1) ** n,
    piDenominator - 1
  )
  

def FavardConstant(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    (2 * n + 1) ** 2
  )
  

def ProuhetThueMorseConstant(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  t = bin(n).count('1') % 2 # Prouhet-Thue-Morse sequence
  
  piFrac += fractions.Fraction( # Add fraction
    t,
    2 ** (n + 1)
  )
  

def PaperfoldingConstant(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    8 ** (2 ** n),
    (2 ** (2 ** (n + 2))) - 1
  )
  

def ReciprocalPowers(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    n ** n
  )
  

def HarmonicNumber(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    n
  )
  

# Calculation Functions
# These take an x value

def RiemannZeta(n, args=[]):
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    n ** args[0]
  )
  

def RiemannZetaFibonacci(n, args=[]):
  
  global piFrac # 0/1
  global piNumerator # 0
  global piDenominator # 0
  
  fib = piNumerator + piDenominator # Find Fibonacci iteration
  piDenominator = piNumerator # Denominator is previous Fibonacci
  piNumerator = fib # Numerator is new Fibonacci
  
  if piNumerator == 0: piNumerator = 1 # Start value
  if piDenominator == 0: piDenominator = 1 # Start value
  
  piFrac += fractions.Fraction( # Add fraction
    1,
    piDenominator ** args[0]
  )
  

def DirichletBeta(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    (-1) ** n,
    (2 * n + 1) ** args[0]
  )
  

def Exponential(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    args[0] ** n,
    math.factorial(n) * (args[1] ** n)
  )
  

def Sine(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    ((-1) ** n) * (args[0] ** (2 * n + 1)),
    math.factorial(2 * n + 1) * (args[1] ** (2 * n + 1))
  )
  

def Cosine(n, args=[]):
  
  n = n - 1 # Start at 0
  
  global piFrac # 0/1
  
  piFrac += fractions.Fraction( # Add fraction
    ((-1) ** n) * (args[0] ** (2 * n)),
    math.factorial(2 * n) * (args[1] ** (2 * n))
  )
  
