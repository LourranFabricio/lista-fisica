M = 19891*(10**3)
G = 66738*(10**-11)

def calculaL2(v2):
    return (v1T*l1T)/v2

def semiEixoMaior(l1,l2):
    return (1/2*(l1+l2))

def bhaskara(v1,l1):
    a = 1
    b = -((2*G*M)/(v1*l1))
    c = -((v1**2)-((2*G*M)/l1))

    delta = (b**2) - 4*a*c
    x1 = (-b) + ((delta**(1/2))/2*a)
    x2 = (-b) - ((delta**(1/2))/2*a)
    if(x1>x2): return x2
    else: return x1

#Valores da terra
v1T = 30287*(10**4)
l1T = 14710*(10**11)

v2T = bhaskara(v1T,l1T)
l2T = (calculaL2(v2T))
a = semiEixoMaior(l1T, l2T)

print(v2T)
print(l2T)
print(a)