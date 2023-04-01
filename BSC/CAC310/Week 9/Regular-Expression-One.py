story = "5 silly monkeys jumping on the bed, one fell off and bonked his head. 4 silly monkeys tumbling on the bed, one fell off and bonked his head. 3 silly monkeys rolling on the bed, one fell off and bonked his head. 2 silly monkeys eating on the bed, one fell off and bonked her head. 1 silly monkeys dancing on the bed, one fell off and bonked her head."

# regex code to get a list all of the numbers and a list of all the phrases within the story below. I want two separate lists.\

def getNumbers():
    '''
    for i in story.split():
        if i.isdigit():
            print(i)
    '''
    return [i for i in story.split() if i .isdigit()]

def getPhrases():
    '''
    for i in story.split():
        if i.isalpha():
            print(i)
    '''
    return [i for i in story.split() if i.isalpha()]


print(getNumbers())
print(getPhrases())

getNumbers = [i for i in story.split() if i.isdigit()]
getPhrases = [i for i in story.split() if i.isalpha()]
print(getNumbers)
print(getPhrases)
