import random

red = [i for i in range(1, 34)]
blue = [i for i in range(1, 17)]
redResult = []
blueResult = []

for i in range(6):
    pick = red[random.randint(0, 32-i)]
    redResult.append(pick)
    red.remove(pick)
print(red)

pick = blue[random.randint(0, 15)]
blueResult.append(pick)
blue.remove(pick)
print(blue)

print("Result:")
print(sorted(redResult))
print(sorted(blueResult))