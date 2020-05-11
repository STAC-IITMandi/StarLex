import math
import numpy as np
import sympy as sp
from sympy import *
from vpython import *
from sympy.interactive import printing
printing.init_printing(use_latex=True)


class stellar:
    # lumin- luminousity,rad-radius,mas-mass,st-surface temperature,t-time
    def __init__(self, lumin, rad, mas, tim, stemp):
        self.lumin = lumin
        self.rad = rad
        self.mas = mas
        self.tim = tim
        self.stemp = stemp

    def star(self):
        scene = canvas()
        scene.autoscale = False
        sphere(
            pos=vector(
                0,
                0,
                0),
            texture="https://i.imgur.com/1nVWbbd.jpg",
            radius=self.rad)
        sphere(
            color=color.white,
            opacity=chem1.k,
            radius=self.rad,
            shininess=10000)


class chemcom:
    def __init__(self, k, q, d):
        self.k = k
        self.q = q
        self.d = d


def massatr(k):
    r = sp.Symbol('r')
    m = sp.Function('m')(r)
    diffeq = Eq(m.diff(r) - 4 * 3.14 * r * r * chem1.d, 0)
    sol = dsolve(diffeq, m).rhs
    constants = solve([sol.subs(r, 0), 0])
    ans = sol.subs(constants)
    f = lambdify(r, ans, "math")
    return(f(k))


def pressure(k):
    r = sp.Symbol('r')
    p = sp.Function('p')(r)
    g = 6.7 * math.pow(10, -11)
    diffeq = Eq(p.diff(r) + (32 * g * math.pi * (chem1.d) * r) / 3, 0)
#     display(diffeq)
    sol = dsolve(diffeq, p).rhs
#     display(sol)
    constants = solve([sol.subs(r, k), 0])
    ans = sol.subs(constants)
    f = lambdify(r, ans, "math")
    return(f(k))


def luminousity(k):
    r = sp.Symbol('r')
    l = sp.Function('l')(r)
    diffeq = Eq(l.diff(r) - 4 * 3.14 * r * r * chem1.q * chem1.d, 0)
#     display(diffeq)
    sol = dsolve(diffeq, l).rhs
#     display(sol)
    constants = solve([sol.subs(r, 0)])
    ans = sol.subs(constants)
#     display(ans)
    f = lambdify(r, ans, "math")
    return(f(k))


def temperature(k):
    r = sp.Symbol('r')
    t = sp.Function('t')(r)
    a = 7.57 * math.pow(10, -16)
    c = 3 * math.pow(10, 8)
    de = chem1.d
    diffeq = Eq(t.diff(r) + (3 * chem1.k * de * de *
                             chem1.q) / (4 * a * c * t * t * t))
#     display(diffeq)
    sol = dsolve(diffeq, t)[3].rhs
#     display(sol)
    constants = solve([sol.subs(r, k), 0])
    ans = sol.subs('C1', k)
#     display(ans)
    f = lambdify(r, ans, "math")
    return(f(k))

# inputs


k = float(input("Enter opacity"))
q = float(input("Enter energy transfer"))
d = float(input("Enter mean density"))
chem1 = chemcom(k, q, d)

# star class
r = float(input("Enter radius"))
l = luminousity(r)
m = massatr(r)
time = float(input("enter time"))
t = temperature(r)
star1 = stellar(l, r, m, time, t)
# display star model
star1.star()
