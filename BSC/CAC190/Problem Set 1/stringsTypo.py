#Dhruv Patel
#CAC 190
#9/12/2022
#Problem 3 String Typos

# Class to translate typos to the corrected string
def translate(typoString):
    # Define original keybard layout
    string = '1234567890qwertyuiopasdfghjklzxcvbnm,. '
    
    # Define typo text
    typo = '234567890-wertyuiop[sdfghjkl;xcvbnm,./ '
    
    # Define an empty string to hold the newly formed, correctedString string
    correctedString = ''
    
    #Loop through the typoPhrase from the user
    for letters in typoString:

        #Find the position of the letter in the typo string
        position = typo.index(letters)
        
        #Grab the letter in that position in the original alphabet and stores the value within the string
        correctedString += string[position]
    
    #Return correctedString string
    return correctedString

# Class for user to enter pharse and output translated correctedString string to user
def main():
    userPhrase = input('Enter phrase: ').lower()
    print(translate(userPhrase).upper())

main()
        