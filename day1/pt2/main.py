#!/bin/python

with open("input.txt", "r") as file:
    data = file.readlines()
    newData = []
    for num in data:
        newData.append(int(num.strip()))

# 1998th is last


sums = []
for i in range(0, len(newData)):  # Indexes of newData
    if not i == len(newData)-2:
        sums.append(sum([ newData[i], newData[i+1], newData[i+2] ]))
    else:
        break

count = 0

for y in range(1, len(sums)):
    if sums[y] > sums[y-1]:
        count += 1

print(y)
print(count)
