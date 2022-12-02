# Dhruv Patel
# CAC 190
# 11/27/2022
# Problem 16 Minimum

import Calculator

testList = []
for i in range(5):
    testList.append(int(input('Please enter a number: ')))

print('Sum:', Calculator.Add(testList))
print('Difference:', Calculator.Subtract(testList))
print('Maximum:', Calculator.Highest(testList))
print('Minimum:', Calculator.Smallest(testList))


    