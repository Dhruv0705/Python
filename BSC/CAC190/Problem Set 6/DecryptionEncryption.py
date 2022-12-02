# Dhruv Patel
# CAC 190
# 11/27/2022
# Problem 18 Encryption

# Function to Permute Alphabet
def PermuteAlphabet(TextPhrase):

    # Empty Dictionary
    EncryptedAlphabet = {}
    
    # Plain text form
    PlainText = 'thequickbrownfoxjumpsoverthelazydog'
    
    # For index of the length of TextPhrase:
    for i in range(len(TextPhrase)):
        
        
        EncryptedAlphabet[TextPhrase[i]]=PlainText[i]
    
    # Return Dictionary
    return EncryptedAlphabet



# Ask User To input number of TestCases
TestCases = int(input("Please Enter Number Of Test Cases: "))

# Empty List
TestsCasesList = []

# Input for blank line
BlankLine = input()

# For index of each TestCases
for i in range(TestCases):

    # Empty List
    lines = []
    line = input()

    # While Loop will keep running as long as there the user press enter
    while line != '':

        # Append each line to list
        lines.append(line)

        # Re ask User to input
        line = input()
        
    # appends line list to TestCaseList
    TestsCasesList.append(lines)

# Empty List to store
DecryptedList = []

# For loop through test cases in TestCaseList
for TestCases in TestsCasesList:

    # Gathers dictionary of lines entered 
    TestDictionary = {}

    # For index of range of length of TestCases
    for i in range(len(TestCases)):


        # Split the length of each index letter in testcase to set to the phrase length variable to find wordcount
        TextPhraseLength = len(TestCases[i].split())

        # Replace each index of i with string space
        TextPhraseLetters = TestCases[i].replace(' ','')

        # If the text phrase length is == 9 and the length of the Text phrase is equal to 35 then:
        if TextPhraseLength == 9 and len(TextPhraseLetters)==35:
            
            # Set The text dictionary to decrypt the letters entered
            TestDictionary = PermuteAlphabet(TextPhraseLetters)
    
    # Created A New Decrypted List
    NewDecryptedList = []

    # for each line in testcases:
    for line in TestCases:

        # Set TextPhrase to empty string
        TextPhrase = ''

        # For each letter in line:
        for letter in line:

            # If the letter contains a space
            if letter == ' ':

                # Set the text phrase as reconsider space string
                TextPhrase += ' '
            
            # Else if false
            else:

                # set the Text phrase to decrypt the letter
                print('No Solution.')
        
        # Appends each Text Phrase to the new list
        NewDecryptedList.append(TextPhrase)
        
    # Appends entire phrase to the decrypted list
    DecryptedList.append(NewDecryptedList)

# For each text phrase within the decrypted list
for TextPhrases in DecryptedList:

    # For each line in text phrase
    for line in TextPhrases:

        # print each line 
        print(line)  
    
    # output program
    print()


   
            
    


