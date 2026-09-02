<style>
  img {max-height: 32rem;}
  body {background-color: rgb(32, 32, 32); color: rgb(240, 240, 240);}
  pre {white-space: pre; overflow-x: scroll; line-height: 1.2em}
</style>

# General

This a python project that uses python's decimal and fractions to calculate Pi and other irrational numbers with many different methods. This program was made for a Linux environment.  

Equations from [wikipedia.com](https://en.wikipedia.org/wiki/List_of_mathematical_constants).  

# File Structure

<pre>
.
├── app.log <i>- Log file</i>
├── config.json <i>- Config file</i>
├── LICENSE.md <i>- GPL v2 License</i>
├── __main__.py <i>- Main script</i>
├── README.md <i>- This file</i>
└── save.json <i>- Default save file</i>
</pre>

# Methods

### GregoryLeibniz

Infinite sum that converges onto pi, π.  

$π = \sum_{k=0}^∞ \dfrac{(-1)^k}{2k + 1}$  

### BaileyBorweinPlouffe

Infinite sum that converges onto pi, π. Converges much quicker than the method above.  

$π = \sum_{n=0}^∞ \left( \dfrac{1}{16^n} \left( \dfrac{4}{8n + 1} - \dfrac{2}{8n + 4} - \dfrac{1}{8n + 5} - \dfrac{1}{8n + 6} \right) \right)$  

### RandomCircle

Monte Carlo method that converges onto pi by generating a random x and y value between 0 and 1, and calculating wether the point (x, y) falls within a circle of radius one centered on the origin. If the point does fall within the circle: 4 is added to the numerator. No matter the outcome 1 is always added to the denominator.  

$x = $`random.random()`  
$y = $`random.random()`  

if $\sqrt{x^2 + y^2} ≤ 1$: numerator $+= 4$  
denominator $+= 1$  

### EulersNumber

Infinite sum that converges onto Euler's Number, $e$.  

$e = \sum_{n=0}^∞ \dfrac{1}{n!}$  

### ReciprocalEulersNumber

Infinite sum that converges onto the Reciprocal of Euler's Number.  

$\dfrac{1}{e} = \sum_{n=0}^∞ \dfrac{1}{(-1)^n n!}$  

### GoldenRatio

Infinite algorithm that converges onto the Golden Ratio, ρ.  

$ρ_{i+1} = 1 + \dfrac{1}{ρ_i}$  

Where $ρ_{i+1}$ is the next iteration of ρ.  

### GoldenRatioFibonacci

Fraction that converges onto the Golden Ratio, ρ, using the Fibonacci sequence.  

$ρ = \lim_{n \to ∞} \dfrac{F_{n+1}}{F_n}$  

Where $F_n$ is the $n\text{'th}$ number of the Fibonacci sequence.  

The part of the Fibonacci sequence being used is $1, 1, 2, 3, 5 ... F_n$ (initial 0 skipped). Where $F_n = F_{n-2} + F_{n-1}$. This is calculated by initially setting the numerator to 1 and the denominator to 1. A temporary value `fib` is set to the numerator + the denominator. Then the denominator is set to the numerator. The numerator then is set to `fib`.  

### GoldenRatioLucas

Fraction that converges onto the Golden Ratio, ρ, using the Lucas sequence.  

$ρ = \lim_{n \to ∞} \dfrac{L_{n+1}}{L_n}$  

Where $L_n$ is the $n\text{'th}$ number of the Lucas sequence.  

The Lucas sequence being $2, 1, 3, 4, 7 ... L_n$. Where $L_n = L_{n-2} + L_{n-1}$. This is calculated by initially setting the numerator to 1 and the denominator to 2. This is calculated the exact same way as the Fibonacci method above, but with initial values of $2, 1$ instead of $1, 1$.    

### ln2

Infinite sum that converges onto the natural log of 2, $\ln(2)$.  

$\ln(2) = \sum_{n=1}^∞ \dfrac{(-1)^{n+1}}{n}$  

### ln2BBP

Bailey-Borwein-Plouffe method for calculating natural log of 2, $\ln(2)$. Converges much quicker than method above.  

$\ln(2) = \dfrac{2}{3} + \dfrac{1}{2} \sum_{n=1}^∞ \left( \dfrac{1}{16^n} \left( \dfrac{1}{2n} - \dfrac{1}{4n + 1} - \dfrac{1}{8n + 4} - \dfrac{1}{16n + 12} \right) \right)$  

### root2

Infinite product that converges onto the square root of 2, √2.  

$\sqrt{2} = \prod_{n=0}^∞ \dfrac{(4n + 2)^2}{(4n + 1)(4n + 3)}$  

### root2TaylorEuler

Infinite sum that converges onto the square root of 2, √2. Above method with a Taylor series then an Euler Transform applied. Converges quicker than above method.  

$\sqrt{2} = \sum_{n=0}^∞ \dfrac{(2n + 1)!}{2^{3n + 1}(k!)^2}$  

### ErdosBorweinConstant

> Laggy  

Infinite sum that converges onto the Erdős-Borwein Constant, $E$.  

$E = \sum_{n=1}^∞ \dfrac{1}{2^n - 1}$  

### ErdosBorweinConstant2

> Laggy  

Infinite sum that converges onto the Erdős-Borwein Constant, $E$. Based on above method, converges quicker.  

$E = 1 + \sum_{n=1}^∞ \dfrac{1}{2^n (2^n - 1)}$  

### LiouvillesConstant

> **Very laggy!**  

Infinite sum that converges onto the Liouville's Constant, $L$.  

$L = \sum_{n=1}^∞ \dfrac{1}{10^{n!}}$  

### CatalansConstant

> Slightly Laggy  

Infinite sum that converges onto Catalan's Constant, $G$. Based on Dirichlet Beta of 2, converges quicker.  

$G = β(2) = -\dfrac{1}{1024} \sum_{n=1}^∞ \dfrac{(-4096)^n (45136n^4 - 57184n^3 + 21240n^2 - 3160n + 165) (2n)!^6 (3n)!^3}{n^3 (2n - 1)^3 n!^3 (6n)!^3}$  

### CahensConstant

> **Very laggy!**  

Infinite sum that converges onto Cahen's Constant, $C$.  

$C = \sum_{n=0}^∞ \dfrac{(-1)^n}{s_n - 1}$  

Where $s_n$ is the $n$'th number in the Sylvester's sequence:  

$s_0 = 2$  
$s_{i+1} = s_i (s_i - 1) + 1$  

### FavardConstant

Infinite sum that converges onto Favard Constant, $K_2$.  

$K_2 = \sum_{n=0}^∞ \dfrac{1}{(2n + 1)^2}$  

### ProuhetThueMorseConstant

Infinite sum that converges onto Prouhet-Thue-Morse Constant, $τ$.  

$τ = \sum_{n=0}^∞ \dfrac{t_n}{2^{n+1}}$  

$t_n$ is the $n$'th value of the Prouhet-Thue-Morse sequence.  

$t_n$ is determined by the number of 1's in the base 2 representation of $n$:  
If the number of 1's is odd $t_n = 1$  
Else (number of 1's is even) $t_n = 0$  

### PaperfoldingConstant

> **Very laggy!**  

Infinite sum that converges onto the Paperfolding Constant, $P$.  

$P = \sum_{n=0}^∞ \dfrac{8^{2^n}}{2^{2^{n+2}}-1}$  

## Functions

These methods take `methodArguments` (below `method` in config).  

### RiemannZeta

Infinite sum that converges onto the Riemann Zeta function given 1 argument $x$, $ζ(x)$.  

$ζ(x) = \sum_{n=1}^∞ \dfrac{1}{n^x}$  

If $x = 2$, it calculates Basel's Number.  
If $x = 3$, it calculates Apéry's Constant.  

### DirichletBeta

Infinite sum that converges onto the Dirichlet Beta function given 1 argument $x$, $β(x)$.  

$β(x) = \sum_{n=0}^∞ \dfrac{(-1)^n}{(2n+1)^x}$  

If $x = 2$, it calculates Catalan's Constant, $G$.  
