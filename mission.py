import random

small=bool(random.randint(0,1))
green=bool(random.randint(0,1))
if green:
    if small:
        print("pea")
    else:
        print("watermelon")
else:
    if small:
        print("cherry")
    else:
        print("pumpkin")
