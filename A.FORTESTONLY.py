import numpy as np

# Polynomial coefficients from your output
coeff = [-2.22145007e-03, 2.86877478e+00, -1.44010647e+03, 3.09429677e+05,
         2.80557785e+05, -1.44236741e+10, 3.09773433e+12, -2.85398341e+14,
         1.02267078e+16]

# Unit aliases for consistent 2-character keys
a = {'thou':'th', 'th':'th', 'inch':'in', 'in':'in', 'foot':'ft', 'ft':'ft',
     'yard':'yd', 'yd':'yd', 'chain':'ch', 'ch':'ch', 'furlong':'fu', 'fur':'fu',
     'mile':'mi', 'mi':'mi', 'league':'le', 'lea':'le'}

# Function to compute x as sum of ord() of first two characters
def get_x(unit):
    s = unit[:2]  # Get alias (e.g., 'yard' -> 'yd')
    return ord(s[0]) + ord(s[1])

# Polynomial evaluation
def eval_poly(x, coeff):
    return np.polyval(coeff, x)

# Read input
n, a, _, b = input().split()

# Compute conversion factors
ca = eval_poly(get_x(a), coeff)
cb = eval_poly(get_x(b), coeff)

# Compute and output result
print(int(int(n) * ca / cb))