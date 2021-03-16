a = 5
b = 3124

power = 0
while a**power <= b:
    power += 1

print(str(a) + " to the power of " + str((power - 1)) + " is the closest number to " + str(b))
