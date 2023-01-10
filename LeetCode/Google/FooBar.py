'''
There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording
    it over the poor minions who are stuck with more boring IDs. To quell the unrest. Commander Lambda has tasked
    you with reassigning everyone new randoms IDs based on complexity foolproof since. Command Lambda has concatenated
    the prime number in a single long string: "235711317192329..." Now every minion must draw a number from a hat.
    That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits
    in the string. So if a minions draws "3", their ID number will be "71113". Help the commander assign these IDs by
    writing a function solution(n) which takes in the starting index n of Lambda string of all primes, and returns the 
    next five digits in the string. Commander Lambda has a lots of minions, so the value of n will always be between 0 and 1000

    Cannot use Imports
    Sieve of Eratosthenes only need the square root of total integers to find all prime numbers eliminating all multiples of itself
'''

def solution(n):

    # Find the length of the prime string needed
    StringLength = n+5

    # Find the maximum integer needed to find all primes
    MaxInt = int(StringLength * (5000/2465) + 475)  

    # Initialize a boolean list to determine if the index is prime
    NumberSet = [True] * MaxInt

    # Set the first two elements to be not prime
    NumberSet[0] = NumberSet[1] = False

    # Loop through the number set, if a number is prime, mark all its multiples as not prime
    for number, IsPrime in enumerate(NumberSet):
        if IsPrime and number <= (MaxInt**(1/2)):
            for multiple in range(number**2, MaxInt, number):
                NumberSet[multiple] = False
    
    # Convert the prime boolean list to a string, with primes being represented as their corresponding integer
    PrimeString = "".join([str(x) for x,y in enumerate(NumberSet) if y])

    # Return the section of the prime string needed
    return PrimeString[n:n+5]



def solution4(n):

    # Find the length of the prime string needed
    str_len = n + 5

    # Find the maximum integer needed to find all primes
    maxInt = int(str_len * (5000/2465) + 475)

    # Initialize a boolean list to determine if the index is prime
    numberSet = [True] * maxInt

    # Set the first two elements to be not prime
    numberSet[0] = numberSet[1] = False

    # Find the square root of the maximum
    sqrt_maxInt = maxInt ** (1/2)

    # Set number variable to 2
    number = 2

    # While the number is less than or equal to the square root of maxInt
    while number <= sqrt_maxInt:

        # For every multiple of the number, starting from number**2, in the range up to maxInt, set the corresponding element in numberSet to False
        for multiple in range(number**2, maxInt, number):
            numberSet[multiple] = False

        # Find the next number in numberSet that is True and greater than the current number
        number = next(i for i, _ in enumerate(numberSet) if i > number and _)

    # Create a string of all the prime numbers in numberSet by joining the string versions of the indices of True elements
    prime_str = ''.join(str(x) for x,y in enumerate(numberSet) if y)

    # Return a substring of prime_str starting at index n and ending at index str_len
    return prime_str[n:str_len]


'''
To check runtime
'''
import time
start = time.time()

for n in range(10000):
    solution(n)
print(f'{time.time()-start} second')

for k in range(10000):
    solution4(n)
print(f'{time.time()-start} second')


