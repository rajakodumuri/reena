import os
import random

callList = os.listdir("Calls\\")

randomCall = random.choice(callList)

print(randomCall)

os.system("start Calls\\"+ randomCall)

# for call in callList:
# 	print(call)
