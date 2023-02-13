# Built In Function - Comment, Range, Slice
class BuiltInFunction:
    def Comment():
        # Comment:
        # To Comment: # abc
        # To Comment All Lines: Highlight, ( CTRL + / )
        # To Comment Multiline string : ''' abc '''
        ''
    # Range Function
    def Range():
        # range(start, stop, step)
        # start: optional (default = 0), inclusive. (start index)
        # stop: required. exclusive. (end index-1)
        # step: optional (default =1). (skip by:)
        # the range function returns a list of numbers that range from zero to one less than the parameter
        range1 = range(10)
        rangeList = list(range(1,10,2))
        print(range1)
        print(rangeList)
    Range()

    def Len():
        # len() function takes a list as a parameter and returns the number of elements in the list
        # tells us the number of elements of any set or sequence.
        def LenString():
            greet = 'Hello Bob'
            print(len(greet))
        LenString()

        def LenList():
            x = [1,2,'joe', 99]
            print(len(x))

            nums = [1,3,51,12,9,72,15]
            print(len(nums))
        LenList()
    Len()

    def MaxMinSumAverage():
        nums = [3,41,12,9,74,15]

        # prints the length of list
        print(len(nums))

        # finds the max
        print(max(nums))

        # finds the min
        print(min(nums))

        # Addds all numbers in list
        print(sum(nums))

        # Adds all numbers and divide by length
        print(sum(nums) /len(nums))
    MaxMinSumAverage()

    def Split():
        # Split breaks a string into parts and produces a list of strings.
        # Can access a poarticular word or loop through all of the wrords. 

        abc = 'with three words'

        # will split each space into an appended list
        stuff = abc.split()
        print(stuff)

        # prints the length of the list
        print(len(stuff))

        # print the first string within the list 
        print(stuff[0])
        
        # For loop to print each word within list in a separate line
        for w in stuff:
            print(w)
    Split()

    def Replace():
        # Replace will replace each word selected inputted to the replacement word selected. 
        str = "hi guys, I am dhruv, hi hi"
        word_to_replace = input("Enter the word to replace: ")
        word_replacement = input("Enter the word replacement: ")
        print(str.replace(word_to_replace, word_replacement))
    #Replace()

    class Slice:
        def Slice():
            # Slice(start, end, step)
            # Start - Specifying which position to start slicing. Default 0
            # end - Which position to end slicing
            # step - Optional. Step of the slicing.
            
            #returns a slice object.
            #slice() 
            # contains indices (0, 1, 2)
            result1 = slice(3)
            print(result1)

            # contains indices (1, 3)
            result2 = slice(1, 5, 2)
            print(slice(1, 5, 2))
        Slice()

        def SliceSubString():
            py_string = 'Python'

            # stop = 3
            # contains 0, 1 and 2 indices
            slice_object = slice(3) 
            print(py_string[slice_object])  # Pyt

            # start = 1, stop = 6, step = 2
            # contains 1, 3 and 5 indices
            slice_object = slice(1, 6, 2)
            print(py_string[slice_object])   # yhn
        SliceSubString()

        def SliceNegitiveIndex():
            py_string = 'Python'

            # start = -1, stop = -4, step = -1
            # contains indices -1, -2 and -3
            slice_object = slice(-1, -4, -1)

            print(py_string[slice_object])   # noh
        SliceNegitiveIndex()

        def SliceSubListNSubTuple():
            py_list = ['P', 'y', 't', 'h', 'o', 'n']
            py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

            # contains indices 0, 1 and 2
            slice_object = slice(3)
            print(py_list[slice_object]) # ['P', 'y', 't']

            # contains indices 1 and 3
            slice_object = slice(1, 5, 2)
            print(py_tuple[slice_object]) # ('y', 'h') 
        SliceSubListNSubTuple()

        def SliceIndex():
            # Alternative for slice object
            # variable = [start:stop:step]

            py_string = 'Python'

            # contains indices 0, 1 and 2
            print(py_string[0:3])  # Pyt

            # contains indices 1 and 3
            print(py_string[1:5:2]) # yh
        SliceIndex() 
    
    class Sorted:
        ''
class Operation:
    def Operation():
        # Operators:
        # Addition: + 
        # Subtraction: -
        # Multipliocation *
        # Exponent: **
        # Division: /
        # Floor Division: //
        # Remainder: %
        x = 5
        quotient = x // 2
        remainder = x % 2
        print("Quotient is ", quotient)
        print("Remainder is ", remainder)
    Operation()

    def Fee():
        # You need to pay 4535 tuition fee for the next semester.
        # The college is giving you a 10% discount.
        # How much do you have to pay?
        fee = 4535
        discount_percent = 10
        discount_amount = (discount_percent /100) * fee
        discounted_fee = fee - discount_amount
        print("Fee after discount ", discounted_fee)
    Fee()
# Conditional Function: If/Elif , Try/Except
class ConditionalStep:
    class IFELIF():
        def IfElif():
            # If statment will continue once statement is false. 
            # Elif Statement will stop at the first element that is true will not run if the previouse statement is true (Must have an else statement.)
            # Only one will execture if there is multiple elif statement if all if/elif is false will skip to else statement.
            x = 5
            print(x , "is: ")
            if x == 5:
                print("Equals to 5")
            if x > 4:
                print("Greater then 4")
            if x >= 5:
                print("Greater than or equals to 5")
            elif x < 6 : print("Less than 6")
            elif x <= 5:
                print("Less than or Equal to 5")
            else:
                x!= 6
                print("Not equal to 6")
        IfElif()
    
    class TryExcept():
        def TryExcept():
            # When the first conversion fails - it drops into the except: clause and the program continues.
            astr = 'Hello Dhruv'
            try:
                istr = int(astr)
            except:
                istr = -1
            print('First', istr)

            astr = '123'
            try:
                istr = int(astr)
            except:
                istr = -1
            print('Second', istr)
        TryExcept()    

    class Parameters():
        class PrintGreetings:
            # A Parameter is a variable which we use in the function definition.
            # It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.
            # lang is the parameter in this case.
            def PrintGreetings(lang):
                if lang == 'es':
                    print("Hola")
                elif lang == 'fr':
                    print("Bonjour")
                else:
                    print("Hello")
            PrintGreetings('es')
            PrintGreetings('us')

            # Return Values will return a value to be used as the value of the funciton call in the calling expression.
            def ReturnGreetings(lang1):
                if lang1 == 'esp':
                    return 'Hola'
                elif lang1 == 'fra':
                    return 'Bonjour'
                else:
                    return 'Hello'
            print(ReturnGreetings('esp'), 'Brian')
            print(ReturnGreetings('usa'), 'Gleen')

        class ReturnAddTwo():
            # Return int Values returning the added variable
            def ReturnAddtwo(a,b):
                added = a + b
                return added

            x = ReturnAddtwo( 3, 5)
            print (x)
# Loop Iteration Function: WhileLoop , ForLoop 
class LoopsNIteration:
    class RepeatedSteps():
        class WhileLoop():
            # While Loops run continously until the test condition evaluates to false
            # If the test condition of the loop is never false, the loop runs infinitely.
            def WhileLoopTakeOff():
                n = 5
                while n > 0:
                    print(n)
                    n = n -1
                print('Blastoff!')
            WhileLoopTakeOff()

            def WhileLoopMultiplication(number):
                
                # Counter value
                count = 1
                
                # While the count is less then 10 until the loop runs 10 times will keep calculating the program until the while is no longer true.
                while count <=10:
                    product = number * count
                    print(number, "x", count, "=", product)
                    count = count + 1
                return number
            WhileLoopMultiplication(6)

            class WhileTrue():
                def WhileTrue(): 
                    # Infinite Loop that will continue until user print 'done' which will break out of the infinite loop
                    # Continue statment will not print and will return back to the first input line. Asking the user to reinput a input.
                    # Break statment will exit the loop. Once the user enters done will exit the while loop.
                    while True:
                        line = input('> ')
                        if line[0] == '#':
                            continue
                        if line == 'done':
                            break
                        print(line)
                    print('Done!')
                #WhileTrue()

                def WhileTrueAverage():
                    #total = 0
                    #count = 0
                    numlist=list()
                    while True:
                        inp = input("Enter a number: ")
                        
                        # once user types 'done' the loop will break to the out of the loop to the calculation. 
                        if inp == 'done' : 
                            break
                        value = float(inp)
                        # append each value to the list
                        numlist.append(value)
                        #total = total + value
                        #count = count + 1
                    #average = total/ count
                    # calculate the sum and the total length of the list and calculate the average
                    average = sum(numlist) / len(numlist)
                    print('Average: ', average)
                #WhileTrueAverage()

            def WhileLoopString():
                fruit = 'bannana'
                index = 0
                while index < len(fruit):
                    letter = fruit[index]
                    print(index, letter)
                    index = index + 1
            WhileLoopString()
        class ForLoop():
            def ForLoop():
                # i Is the index that will iliterate thorugh each statement or array or list. can be renamed
                for i in [5,4,3,2,1]:
                    print(i)
                print('Blastoff!')
            ForLoop()

            def ForLoopSet():
                print('Before')
                for thing in [9, 41, 12, 3, 74, 15]:
                    print(thing)
                print('After')
            ForLoopSet()

            def ForLoopFinding_Largest_Number():
                largest_so_far = -1
                print('Largest So far: ', largest_so_far)
                for the_num in [9,41,12,3,72,15]:
                    if the_num > largest_so_far:
                        # Sets the greater number as the_num new variable iliterating through set that the program has seen so far. 
                        largest_so_far = the_num
                    print("Largest Number so far:" , largest_so_far , "Looking at", the_num)
                    if the_num != largest_so_far:
                        print(the_num, "Is not the largest")
                print('New Largest Number in Set: ', largest_so_far)
            ForLoopFinding_Largest_Number()

            def ForLoopSmallest():
                smallest = None
                print("Smallest Number: ")
                for value in [9, 41, 12, 3, 74, 15]:
                    if smallest is None:
                        smallest = value
                    elif value < smallest:
                        smallest = value
                    print(smallest, value)
                print('Smallest Number: ', smallest)
            ForLoopSmallest()

            def ForLoopCounter():
                counter = 0
                print('Counter = ', counter)
                for i in [9,41,12,3,74,15]:
                    counter = counter + 1 
                    print(counter, i)
                print('Total Number of sets: ', counter)
            ForLoopCounter()

            def ForLoopSumming():
                counter = 0
                sumSet = [9,41,12,3,74,15]
                print('Total Sum =', counter)
                for i in sumSet:
                    counter = counter + i
                    print(i, "+")
                print('Total Sum =', counter)
            ForLoopSumming()

            def ForLoopAverage():
                # Empty variable
                count = 0
                sum = 0 
                print("Sum , Average: ", count, sum)
                for value in [9,41,12,3,74,15]:

                    # Adds counter + 1 each loop
                    count = count + 1

                    # Adds index of value to sum
                    sum = sum + value
                    print (count, sum, value)
                print("New Sum , Average ", "length: ", count , "sum: ", sum , "average", sum/count)
            ForLoopAverage()

            def ForLoopFiltering():
                print("Filtering: ")
                for value in [9,41,12,3,74,15]:
                    if value > 20:
                        print('Large Number Value:', value)
                print('Filtered: ')
            ForLoopFiltering()

            def ForLoopBoolean():
                found = False
                print('Found?', found)
                for value in [9,41,12,3,74,15]:
                    if value ==3:
                        found = True
                    print (found, value)
                print('Found?', found)
            ForLoopBoolean()

            def ForLoopString():
                fruit = 'banana'
                for letter in fruit:
                    print(letter)
            ForLoopString()

            def ForLoopStringCount():
                word = 'banana'
                count = 0
                for letter in word:
                    if letter == 'a':
                        count = count + 1
                print("Word", letter, "occurs" , count, "times")
            ForLoopStringCount()    
# Reading Files
class ReadingFiles:
    def OpenFile():
        #handle = open(#filename, #mode)
        # returns a handle use to manipulate the file
        # filename is a string
        # mode is optional and should be 'r' to read or 'w' to write to the file            
        fhand = open('filename.txt')
        print(fhand)  

    def CountingLinesInFile():
        fhand = open('filename.txt')
        count = 0
        for line in fhand:
            count = count + 1
        print('Line CountL ', count)
    # Counts line within a file

    def SearchingThroughFile():
        # rstrip() removes all whitespaces from the right-hand side newline is considered "whiteline" and is being stripped
        # Single space output
        fhand = open ('filename.txt.')
        for line in fhand:
            line - line.rstrip()
            if line.startswith("From: ") :
                print(line)
    
    def SkippingThroughFile():
        # Can also conveniently skip a line by using the continue statement.
        fhand = open('filename.txt')
        for line in fhand:
            line - line.rstrip()
            if not line.startswith('From: '):
                continue
            print(line)
    
    def PromptFileName():
        # Ask the user to enter a file name that will output counted lines for each inputted file name
        fname = input('Enter the file name:')
        try:
            fhand = open(fname)
        except:
            print ('File cannot be opened:', fname)

            # Will terminate the entire program with no traceback. Stop executing caused but incorrect input.
            quit()
        
        count = 0
        for line in fhand:
            if line.startswith('Subject:'):
                count = count + 1
        print ('There were,', count, 'subject lines in', fname)
# Lists
class Lists:
    # append
    # count
    # extend
    # index
    # insert
    # pop
    # remove
    # reverse
    # sort
    def List():
        # [] = list
        # Collection that allows us to put many values in a single "variable" 
        friends = [ 'Joseph', 'Glenn', 'Sally']
        carryon = ['socks,' 'shirt', 'perfume']
        Color = ['red', 'yellow', 'blue']
        ListWithinAList = [1,3,[5,6], 7, 8]
        print (Color)
        print (ListWithinAList)
        for friend in friends:
            print('Happy New Year', friend)
        print('Done')
    List()
    
    def ListSlice():
        t = [9,41,12,3,74,15]

        # starts at length 1 stops at length 3 
        print(t[1:3])

        # prints all in list stops at length 4
        print(t[:4])

        # start length 3 prints rest
        print(t[3:])

        # no slice operations
        print(t[:])
    ListSlice()

    def ListAppend():
        # Append Can create an empty list and then add elements using the append method
        # list starys in order and new elements are added at the end of the list
        stuff = list()
        stuff.append('book')
        stuff.append(99)
        print(stuff)
        stuff.append('cookie')
        print(stuff)
    ListAppend()
    
    def ListSort():
        # A list can be sorted ie. change its order
        # the sort method "sorts yourself" in changing its order
        friends = ['Joseph', 'Glenn', 'Sally']
        friends.sort()
        print(friends)
        print(friends[1])
    ListSort()            

# Dictionary
class Dictionary:
    # A list is a linear collection of values that stay in order
    # A dictionary is a "bag" of values each with its own label
    # Dictionary are python most powerful data collection
    # Dictionaries allow us to do fast databases-like operation

    def Collection():
        # In a collection we can put more than one value in it and carry them all around in one convenient package.
        # A bunch of values in a single 'variable'
        # Dictonaries assign a variable to a value in a printed key that can be readjusted in changing the value of the set key.
        purse = dict()
        purse ['money'] = 12
        purse ['candy'] = 3
        purse ['tissues'] = 75
        purse['candy'] = purse['candy'] + 2
        print (purse)
    Collection()

    def ComparingListNDictionaries():
    # Dictionaries are like lists except that they use keys (orange) instead of number to look values 
        def List():
            lst = list()
            lst.append(21)
            lst.append(183)
            lst[0] = 23
            print(lst)
        List()
        def Dict():
            Dictonary = dict()
            Dictonary ['age'] = 21
            Dictonary ['course'] = 182
            Dictonary ['age]'] = 23
            print(Dictonary)
        Dict()
    ComparingListNDictionaries()

    def DictionaryLiterals():
        # Dictonaries literals uses {} and have a list of key:value pair
        # You can make an empty dictionary using empty curly braces
        DictonaryLiterals = { 'chuck': 1, 'fred' : 42, 'jan': 100} 
        print(DictonaryLiterals)
        EmptyDictionary = {}
        print (EmptyDictionary)
    DictionaryLiterals()

    def DefiniteLoopsNDictionaries():
        # Even though dictionaries are not stored in order, we can write a for loop that goes through
        # all the  keys in a dictionary and look up the value
        counts = { 'chuck': 1, 'fred' : 42, 'jan': 100}
        for key in counts:
            print(key, counts[key])
    DefiniteLoopsNDictionaries()

    def RetrievingKeysNValues():
        # Turn Dictionary into a list
        Dictionary = { 'chuck': 1, 'fred' : 42, 'jan': 100}
        print(list(Dictionary))
        
        # Only print the keys using the keys() method
        print(Dictionary.keys())

        # Only print the values using the values() method
        print(Dictionary.values())

        # Prints both items() method Also known as a tuple
        print(Dictionary.items()) 
    RetrievingKeysNValues()

    class Counting:

        def GetMethod():
            # The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there. get()
            counts = dict()
            names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
            for name in names:
                # can use get() provide a default value of zero when the key is not yet in the dictionary- and then add one as it loops through the [names] adding a value of 1 repeating each multiple within list
                counts[name] = counts.get(name, 0) + 1
            print(counts)
        GetMethod()

    class CountingWordsInText:

        def CountingPattern():
            # The general pattern to count the words in a line of text is to split the line into words
            # Then loop though the words and use a dictionary to track the count of each word independently. 
            counts = dict()
            print('Enter a line of text: ')
            
            line = input('')

            # Splits each inputted line into each key
            words = line.split()
            print('Words:', words)

            print('Counting...')
            for word in words:

                # Adds 1 for each duplicated word in words
                counts[word] = counts.get(word,0) + 1
            print('Counts', counts)
        CountingPattern()
# Tuples
class Tuples:
    # Tuples are another kind of sequence that functions much like a list
    # They have elements which are indexed starting at 0
    # Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
    def Tuples():
        AllTupleFunction = tuple()
        # ['count', 'index']
        dir(AllTupleFunction)
        

        y = (1,9,2)
        print("Max: " , max(y))
        for iter in y:
            print(iter)
    Tuples()

    def TuplesAssignment():
        # Can use tuple on the left-hand side of an assignment statement
        # we can omit the parentheses
        (x, y) = (4, 'fred')
        print(y)

        (a,b) = (99,25)
        print(a)
    TuplesAssignment()

    def TuplesVSDictionary():
        d = dict()
        d['csev'] = 2
        d['cwen'] = 4

        # Loops through k and value : key is csev value is 2 that is set to the key. and prints
        for (k,v) in d.items():
            print(k,v)
        
        t = d.items()
        print(t)
    TuplesVSDictionary()

    class SortingListsOFTuples:
        def SortingTuplesByKey():
            # We can sort a list of tuples to get a sorted version of a dictionary
            # Need to sort the dictionary by the key using items() and sorted() function
            Dictionary = {'a' : 10, 'b' : 1, 'c' : 22}
            Dictionary.items()

            # We sort the dictionary by the key using teh items() method and sorted() function
            sorted(Dictionary.items())

            # For loop to print key and value in a new line sorted
            for k, v in sorted(Dictionary.items()):
                print(k , v)
        SortingTuplesByKey()

        def SortingTuplesByValues():
            Dictionary = {'a' : 10, 'b' : 1, 'c' : 22}
            Temp = list()
            
            # For loop to append values and keys in order to the list
            for k , v in Dictionary.items():
                Temp.append((v, k ))
            print(Temp)

            # Sorts by value by descending order
            Temp = sorted(Temp, reverse=True)
            print(Temp)
        SortingTuplesByValues()

        def SortingTuplesOneLine():
            Dictionary = {'a' : 10, 'b' : 1, 'c' : 22}
            print(sorted([(value,key) for key,value in Dictionary.items()], reverse=True))
        SortingTuplesOneLine()

    print("______________________________________________________")
    
    class MostCommonWord:
        def MostCommonWordInFile():
            print("Top 10 Common Words:")

            fhand = open('txt/romeo-full.txt')
            counts = dict()
            for line in fhand:
                words = line.split()
                for word in words:
                    counts[word] = counts.get(word, 0 ) + 1

            lst = list()

            # Loops through key and value within dictionary
            for key, val in counts.items():
                NewTuple = (val,key)
                lst.append(NewTuple)
            
            # Sorts by value by descending order
            lst = sorted(lst, reverse=True)

            # Loops through most 10 
            for val, key in lst[:10] : 
                print(key , val)
        MostCommonWordInFile()

    print("______________________________________________________")

class RegularExpressions:
    # Provides a concise and flexible means for matching strings of text, such as:
    # Particular characters, words, or patterns of characters.
    # A regular expression is written in a formal language that can be interpreted bny a regular expression processor. 
    # Must Import regular expression library "import.re"
    print("REGULAR EXPRESSION")
    def RegularExpressionQuickGuide():


        '''REGULAR EXPRESSION QUICK GUIDE'''
        ''' 
        ^        Matches the beginning of a line
        $        Matches the end of the line
        .        Matches any character
        \s       Matches whitespace
        \S       Matches any non-whitespaces character
        *        Repeats a character zero or more times
        *?       Repeats a character zero or more times (non-greedy)
        +        Repeats a character one or more times
        +?       Repeats a character one or more times (non-greedy)
        [aeiou]  Matches a single character in the listed set
        [^XYZ]   Matches a single character not in the listed set
        [a-z0-9] The set of characters can include a range
        (        Indicates where string extraction is to start
        )        Indicates where string extraction is to end

        '''
    
    # re.findall() extract portions of a string that match your regular expression, similar to a combination of find() and slicing
    def ReSearch():
        # re.search() see if a string matches a regular expression, similar to using the find() method for string
        print("RE.SEARCH()")
        import re
        hand = open('txt/mbox-short.txt')
        for line in hand:

            # Strips each line into words on each line to illiterate. 
            line = line.rstrip()

            # re.search is like startswith() line is what we are searching, from: is what we are looking for to print
            if re.search('From:' , line):
                print(line)
    ReSearch()

    class ReFindall:
        def ReFindall():
            print("RE.FINDALL()")
            # Matching and Extracting Data
            # re.search() returns a True/False depending on wheatear the string matches the regular expression
            # re.findall() extracts t he matching strings 
            import re 
            x = " My 2 favorite number are 19 and 42"
            y = re.findall('[0-9]+' , x)
            print(y)
        ReFindall()
        
        def GreedyMethod():
            # The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string
            # Greedy Method : ^F - First character in the match .+ Last character in the match
            import re
            x = 'From: Using the : character'
            y = re.findall('^F.+:' , x)
            print(y)
        GreedyMethod()

        def NonGreedyMethod():
            # Non - Greedy Method : ^F - First character in the match .+? very first Last character in the match 
            import re
            x = 'From: Using the : character'
            y = re.findall('^F.+?:', x)
            print(y)
        NonGreedyMethod()

        def FineTunningStringExtraction():
            import re
            x = 'From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
            y = re.findall('\S+@\S+' , x)
            print(y)    
        FineTunningStringExtraction()

        class SpamConfidence():
            import re
            hand = open('txt/mbox.txt')
            numlist = list()
            for line in hand:
                line = line.rstrip()
                stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)' , line )
                if len(stuff) != 1 : continue
                num = float(stuff[0])
                numlist.append(num)
            print('Maximum: ', max(numlist))


class StringParsing:
    # find() can locate the position as well as can extract a host name - using find and string slicing
    def SplitPattern():
        data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
        
        # Finds the position of the first @
        atpos = data.find('@')
        print(atpos)

        # prints the first space after position 21
        sppos = data.find(' ', atpos)
        print(sppos)

        # Host = starts at line 22 and stops at line 31 with slice
        host = data[atpos+1 : sppos]
        print(host)
    SplitPattern()

    def DoubleSplitPattern():
        line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

        # Splits each spaces into list
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        print(pieces[1])
    DoubleSplitPattern()

class NetworkedPrograms:
    class TransportControlProtocol:
        # TCP Built on top of IP (Internet Protocol)
        # handles flow control using a transmit window
        # TCP PORT NUMBERS:
        # A port is an application-specific or process-specific software communications endpoint
        # Allows multiple networked applications to coexist on the same server
        # Can solve problems like Application Protocols such as mail and World Wide Web. (www)
        ''
    class CommonTCPPort:
        # Telnet (23) - Login
        # SSH (22) - Secure Login
        # HTTP (80) 
        # HTTPS (443) Secure
        # SMTP (25) - Mail
        # IMAP (143/220/993) - Mail Retrieval
        # POP (109/110) - Mail Retrieval
        # DNS (53) = Domain Name
        # FTP (21) - File Transfer
        # Sometimes we see the port number in the URL if running a "non-standard" port
        ''
    def SocketInPython():
        # Built in support for TCP Socket
        import socket
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect(('data.pr4e.org', 80))
        cmd = 'GET http://data/pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
        mysocket.send(cmd)

        while True:
            data = mysocket.recv(512)
            if (len(data) < 1):
                break
            print(data.decode())
        mysocket.close()

class ObjectOrientedProgramming:
    # A program is made up of many cooperating objects
    # A program is made up of one or more objects working together - objects make use of each other's capabilities
    # A object is a bit of self-contained code and data
    # A key aspect of the object approach is to break the problem into smaller understandable parts ( divide and conquer)
    # Objects have boundaries that allow us to ignore un-needed detail
    class ObjectDefinition:
        # Class - a template (class Dog):
        # Attribute - A variable within a class
        # Method or Message - A defined capability of a class - (bark())
        # Field or attribute - A bit of data in a class - length
        # Object or Instance - A particular instance of a class - (Lassie)
        # Constructor - Coded that runs when an object is created
        # Inheritance - The ability to extend a class to make a new class
        ''
        class Terminology:
            def Class():
                # A pattern (exemplar) of a class. The class of Dog defines all possible dogs by listing the characteristics and behaviors they can have;
                # The objects Lassie is one particular dog, with particular versions of the characteristic. A Dog has fur; Lassie has brown-and-white fur.
                ''
            def Instance():
                # One can have an instance of a class or particular object. The instance is the actual object created at runtime. In programmer jargon , the lassie object is an instance of the Dog class.
                # The set of values of the attributes of a particular object is called its state. the object consists of state and the behavior that defined the object class.
                ''
            def Method():
                # An objects abilities. In languages, methods are verbs. Lassie, being a Dog, has the ability to bark. so bark() is one of Lassies methods. She may have others methods as well,
                # For example sit() or eat() or walk() or save_timmy(). Within the program, using a method usually affects only one particular objects; all Dogs can bark, but you need only one particular dog to do the barking. 
                ''
    # Method for making PartyAnimal object.
    class PartyAnimal:

        # Each PartyAnimal object has a bit of data
        x = 0

        # Each PartyAnimal object has a bit of code.
        def party(self):
            self.x = self.x + 1
            print("So Far", self.x)

    # Construct a PartyAnimal object and store in an 
    an = PartyAnimal()

    # Tell the an object to run the party() code within it.
    an.party()
    an.party()
    an.party()
    
    print('Type', type(an))
    print('Dir', dir(an))

    class ObjectLifecycle:
        class Constructor:
            # The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created
            # The constructor and destructor are optional
            # The constructor is typically used to set up variables. The destructor is seldom used.
            # In OOP, a constructor in a class is a special block of statements called when an object is created
            class PartyAnimal1:
                x = 0
                def __init__(self):
                    print("I am constructed")
                def party(self):
                    self.x = self.x + 1
                    print('So far', self.x)
                
                def __del__(self):
                    print("I am destructured", self.x)

            an = PartyAnimal1()
            an.party()
            an.party()
            an = 42
            print('an contains', an)
        class Inheritance:
            # When making a new class - we can reuse an existing class and inherit all the capabilities of an existing class and add our own to make a new class.
            # Another form of store and reuse
            # Write once - reuse multiple times
            # The new class(child) has all the capabilities of the old class(parent)
            ''
            class ExtendClass:
                class PartyAnimal:
                    x = 0
                    name = ""
                    def __init__(self, nam):
                        self.name = nam
                        print(self.name, "constructed")

                    def Party(self):
                        self.x = self.x + 1
                        print(self.name, "party count", self.x)
                
                # FootballFan is a class which extends PartyAnimal holding all of capabilities of PartyAnimal and more. 
                class FootballFan(PartyAnimal):
                    points = 0
                    def Touchdown(self):
                        self.points = self.points + 7
                        self.Party()
                        print(self.name, "points", self.points)
                Sally = PartyAnimal("Sally")
                Sally.Party()

                Jim = FootballFan("Jim")
                Jim.Party()
                Jim.Touchdown()

class Databases:
    class RelationalDatabasesNSQLite:
        # Relational Databases model data by storing rows and columns in tables.
        # The power of the relational database lies in its ability to efficiently retrieve data from
        # Tables and in particular where there are multiple tables and the relationship between those tables involved in the query.

        # TERMINOLOGY
        # Database - Contains many tables
        # Relation (tables) - Contains tuples and attributes
        # Tuple (row) - A set of filed that general's represent an "object" like a person or a music track
        # Attribute (columns or fields) - O-ne of possible many elements of data corresponding to the object represented by the row. 

        # SQL (Structured Query Language ) - language we use to issue command to the database
            # Create a table
            # Retrieve data
            # insert data
            # Delete data

        # WEB APPLICATION W/ DATABASES
            # Application Developer - Builds the logic fot he application, the look and feel of the application - monitors the application for problems
            # Database Administrator - Monitor and adjusts the databases and the program runs in production
            # Database Model (Database Schema) - is the structure or format of a database, described in a formal language supported by the database management system.
                # Application of a data model when used in conjunction with a database management system. 
                # Three major Database Management System in wide use
                    # Oracle - Large, commercial, enterprise - scale, very very tweakable
                    # MySql - Simpler but very fast and scalable commercial open source. 
                    # SqlServer - From Microsoft (Access)
        ''

                    
            
                



