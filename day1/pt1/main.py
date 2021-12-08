#!/bin/python

with open("input.txt", "r") as file:
    data = file.readlines()
    newData = []
    for num in data:
        newData.append(int(num.strip()))
    print(newData)

    count = 0

    for i in range(1,len(newData)):
        if newData[i] > newData[i-1]:
            count += 1

    print(count)



