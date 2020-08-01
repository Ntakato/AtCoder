import math
a, b, x = (int(i) for i in input().split())
t = 2 * (b/a - x/(a*a*a))
z = math.atan(b/a)
rad = math.atan(t)

if(rad <= z):
    deg = math.degrees(rad)
else:
    rad = math.atan((a*b*b)/(2*x))
    deg = math.degrees(rad)
print(deg)
