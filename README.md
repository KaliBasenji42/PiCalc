<style>
  img {max-height: 32rem;}
  body {background-color: rgb(32, 32, 32); color: rgb(240, 240, 240);}
  pre {white-space: pre; overflow-x: scroll; line-height: 1.2em}
</style>

# General

This a python project that uses python's decimal and fractions to calculate Pi and other irrational numbers with many different methods. This program was made for a Linux environment.  

Equations from [wikipedia.com](https://wikipedia.com).  

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

**Gregory-Leibniz:**  

Infinite sum that converges onto π.  

$\sum_{k=0}^∞ \dfrac{(-1)^k}{2k + 1}$  

**Bailey-Borwein-Plouffe:**  

Infinite sum that converges onto π.  

$\sum_{n=0}^∞ \left( \dfrac{1}{16^n} \left( \dfrac{4}{8n + 1} - \dfrac{2}{8n + 4} - \dfrac{1}{8n + 5} - \dfrac{1}{8n + 6} \right) \right)$  

**Random Circle:**  

Monte Carlo method that converges onto π by generating a random x and y value between 0 and 1, and calculating wether the point (x, y) falls within a circle of radius one centered on the origin. If the point does fall within the circle: 4 is added to the numerator. No matter the outcome 1 is always added to the denominator.  

$x = \text{random.random()}$  
$y = \text{random.random()}$  

$\text{if } \sqrt{x^2 + y^2} ≤ 1: \text{numerator } += 4$  
$\text{denominator } += 1$  

**Euler's Number:**  

Infinite sum that converges onto Euler's Number, $e$.  

$e = \sum_{n=0}^∞ \dfrac{1}{n!}$  

**Apéry's Constant:**  

Infinite sum that converges onto Apéry's Constant.  

$ζ(3) = \sum_{n=1}^∞ \dfrac{1}{n^3}$  

**Golden Ratio:**  

Infinite algorithm that converges onto the Golden Ratio, ρ:  

$ρ_{i+1} = 1 + \dfrac{1}{ρ_i}$  

Where $ρ_{i+1}$ is the next iteration of ρ.  

**Golden Ratio-Fibonacci:**  

Fraction that converges onto the Golden Ratio, ρ, using the Fibonacci sequence.  

$ρ = \lim_{n \to ∞} \dfrac{F_{n+1}}{F_n}$  

Where $F_n$ is the $n\text{'th}$ number of the Fibonacci sequence.  

The part of the Fibonacci sequence being used is $1, 1, 2, 3, 5 ... F_n$ (initial 0 skipped). Where $F_n = F_{n-2} + F_{n-1}$. This is calculated by initially setting the numerator to 1 and the denominator to 1. A temporary value `fib` is set to the numerator + the denominator. Then the denominator is set to the numerator. The numerator then is set to `fib`.  

**Golden Ratio-Lucas:**  

Fraction that converges onto the Golden Ratio, ρ, using the Lucas sequence.  

$ρ = \lim_{n \to ∞} \dfrac{L_{n+1}}{L_n}$  

Where $L_n$ is the $n\text{'th}$ number of the Lucas sequence.  

The Lucas sequence being $2, 1, 3, 4, 7 ... L_n$. Where $L_n = L_{n-2} + L_{n-1}$. This is calculated by initially setting the numerator to 1 and the denominator to 2. This is calculated the exact same way as the Fibonacci method above, but with initial values of $2, 1$ instead of $1, 1$.    

