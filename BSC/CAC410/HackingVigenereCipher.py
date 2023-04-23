'''
Dhruv Patel
4/23/23
CAC 410
Hacking Vigenere Cipher

1. What attack did you choose and why (please include technical explanations as well as subjective)?
   I went with chapter 21 dictionary attack because it was the easiest to understand and implement.
   I also chose this attack because it was the most efficient and effective from the attacks I read about.
2. Was the attack successful? 
    Yes, the attack was successful. I was able to decrypt the message and the class message.
3. How long did the attack take? Do you think it was efficient?
    The attack took about 3 minutes. I think it was efficient because it was able to decrypt the message in a short amount of time.
       but it could be more efficient if it was able to decrypt the message in a shorter amount of time the nested for loop could be improved.
'''
# Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, vigenereCipher, pyperclip

def main():

    # input cipherText to hack
    cipherText = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    
    # hack the cipherText
    hackedMessage = hackVigenere(cipherText)

    # if hacking was successful, the decrypted message will be displayed
    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

    # if hacking was not successful, the user will be notified
    else:
        print('Failed to hack encryption.')

# hackVigenere() will attempt to hack the Vigenere cipher by trying every possible key
def hackVigenere(cipherText):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    # loop through every possible key
    for word in words:

        # remove the newline character from the end of the word
        word = word.strip()

        # attempt to decrypt the cipherText with the current key
        decryptedText = vigenereCipher.decryptMessage(word, cipherText)

        # if the decrypted text is English, display it to the user
        if detectEnglish.isEnglish(decryptedText):
            # Check with user to see if the decrypted key has been found:
            print()
            print('Possible encryption hack:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            # if the user enters D, the program will end
            if response.strip().upper().startswith('D'):
                return decryptedText
            

if __name__ == '__main__':
    main()




