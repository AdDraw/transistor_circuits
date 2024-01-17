## Example 2.5 body Effect on Vt
from math import sqrt, log,e
import numpy as np

vt = 26e-3
Vsb = 0.6
Vt0 = 0.3
q = 1.602e-19
eo = 8.85e-17
esi = 11.7 * eo
eox = 3.9 * eo
Na = 8e17
ni = 1.45e10
tox = 10.5e-10

def ln(x):
  return log(x,e)

y = (tox/eox) * sqrt(2*q*esi*Na)

print(f"y: {y}")

surface_pot = 2*vt*ln(Na/ni)

print(f"surface potential: {surface_pot}")

print(f"Vt+bodyeff: {y*(sqrt(surface_pot+Vsb) -sqrt(surface_pot))}")
# print(sqrt(0.4))