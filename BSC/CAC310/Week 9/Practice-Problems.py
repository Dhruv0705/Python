# Dhruv Patel
# 3/31/2021
# CAC310
# Dr. Wagner

nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# 1. Find all of the numbers from 1–1000 that are divisible by 8

def DivisibleBy8():
    '''
    for i in nums: 
        if i % 8 == 0:
            print(i)
    '''
    return [i for i in nums if i % 8 == 0]
print(DivisibleBy8())

# 2. Find all of the numbers from 1–1000 that have a 6 in them

def Contains6():
    '''
        for i in nums:
            if '6' in str(i):
                print(i)
    
    '''
    return [i for i in nums if '6' in str(i)]

print(Contains6())

# 3. Count the number of spaces in a string

def CountSpaces():
    '''
        count = 0 
        for i in string:
            if i == ' ':
                count += 1
    '''
    return len([i for i in string if i == ' '])

print(CountSpaces())

# 4. Remove all of the vowels in a string [make a list of the non-vowels]

def RemoveVowels():
    '''
        vowels = ['a','e','i','o','u']
        for i in string:
            if i not in vowels:
                print(i)
    '''
    return [i for i in string if i not in ['a','e','i','o','u']]

print(RemoveVowels())

# 5. Find all of the words in a string that are less than 4 letters

def LessThan4():
    '''
        for i in string.split():
            if len(i) < 4:
                print(i)
    '''
    return [i for i in string.split() if len(i) < 4]

print(LessThan4())


# 6. Use a dictionary comprehension to count the length of each word in a sentence.

def CountLength():
    '''
        for i in string.split():
            print(i, len(i))
    '''
    return {i:len(i) for i in string.split()}

print(CountLength())


# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

def DivisibleBy2to9():
    '''
        for i in nums:
            for j in range(2,10):
                if i % j == 0:
                    print(i)
    '''
    return [i for i in nums for j in range(2,1001) if i % j == 0]

print(DivisibleBy2to9())

# 8. For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

def HighestSingleDigit():
    '''
        for i in nums:
            for j in range(2,10):
                if i % j == 0:
                    print(j)
    '''
    return [j for i in nums for j in range(2,1001) if i % j == 0]

print(HighestSingleDigit())

# 9. Write a recursive solution to determine if a string is a palindrome.

def IsPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and IsPalindrome(string[1:-1])
    
print(IsPalindrome('racecar'))
print(IsPalindrome('hello'))