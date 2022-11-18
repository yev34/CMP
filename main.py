from cmath import sin, sqrt
from re import X
from scipy import integrate 
import math
eps = 0.001
a=0.4
b=1.2
n=8
def f1(x): 
    return (2*x+0.5)*sin(x)
def simpson(a,b,n): 
    h = (b - a) / n 
    integr = f1(a) + f1(b) 
    for i in range(1,n): 
        k = a + i*h 
        if i%2 == 0: 
            integr += 2 * f1(k) 
        else: 
            integr += 4 * f1(k) 
    integr *= h/3 
    return integr 
if abs(simpson(0.4,1.2,2*8) -simpson(0.4,1.2,8))/ 15. <= eps: 
   print("Simpsone method:",round (simpson(0.4,1.2,8), 5)) 
v,err = integrate.quad(f1,0.4,1.2,)#Перевірка 
print("Check for the simpsone method= ",round(v, 5)) 



