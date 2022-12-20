class BigONotation:

    # Take an input of n and return the sum of the numbers from 0 to n
    class ReturnSumOfNum:
        def Sum1(n):
            Sum = 0
            for x in range(n+1):
                Sum += x
            return Sum
        Sum1(5)

        def Sum2(n):
            return (n*(n+1))/2
        Sum2(5)

