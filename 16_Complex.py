# complex(x,y) : x real part, y: imaginary part : x + yJ

a = complex(1, 2)
b = 1 + 2j
print(a == b)
print(a.real, a.imag, type(a.real), type(a.imag))

c = a.conjugate()
print(c)

print(a, b)
print(a + b, a - b, a * b, a / b)

a = 0.1j
print(f"{a.imag:.20f}")

print(a + a + a == 0.3j)
print(f"{(a + a + a).imag: .25f}")
print(f"{(0.3j).imag: .25f}")

import math
import cmath  # for complex numbers

a = 1 + 2j
print(cmath.sqrt(a))

# rectangular to polar
a = 1 + 1j
print(cmath.phase(a))
print(cmath.pi / 4)

print(abs(a))

# polar to rect format
print(cmath.rect(math.sqrt(2), math.pi / 4))

# euler identity e^(i*pi) + 1 =0
RHS = cmath.exp(complex(0, cmath.pi)) + 1
print(RHS == 0)
print(cmath.isclose(RHS, 0))
print(cmath.isclose(RHS, 0, abs_tol=0.0001))
