import random as r

def func():
	v = 5
	return v 
v= func()
print(v)

chance = 0.05

number = 10000
misses = 0
atacks = 0
for i in range(number):
	v=r.randit(1,number)
	if v <= chance*munber:
	misses += 1 
else:
	attacks += 1 

print("misses", str(misses/nummber*100) + %)
print("attacks", str(attacks/number))