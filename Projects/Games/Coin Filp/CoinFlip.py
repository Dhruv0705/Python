import random

HeadsCounter = 0
TailsCounter = 0

for i in range(100):
    Flip = random.randint(0,1)
    if (Flip == 1):
        HeadsCounter += 1
        TailsCounter += 1

print(f"Heads: {HeadsCounter}")
print(f"Tails: {TailsCounter}")