v1 = [1, 2, 3]
v2 = [2, 3, 4]
skalarSoucet = 0
norm = 0

"""
for i in range(len(v2)):
    print( v1[i] * v2[i] )    
    skalarSoucet = skalarSoucet + v1[i] * v2[i]
print(skalarSoucet)
# Vysledek by mel byt 20
"""

for j in range(len(v2)):
    norm = norm + (v1[j]**2)+(v2[j]**2)
norm**0.5
print(norm)