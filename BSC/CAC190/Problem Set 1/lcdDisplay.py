#Dhruv Patel
#CAC 190
#9/12/2022
#Problem 1 LCD Display

# Dictonary for positing screen
lcdDictionary = {
    '0': ['top','both','blank','both','bottom'],
    '1': ['blank','right','blank','right','blank'],
    '2': ['top','right','middle','left','bottom'],
    '3': ['top','right','middle','right','bottom'],
    '4': ['blank','both','middle','right','blank'],
    '5': ['top','left','middle','right','bottom'],
    '6': ['top', 'left', 'middle','both','bottom'],
    '7': ['top', 'right', 'blank', 'right', 'blank'],
    '8': ['top', 'both', 'middle', 'both', 'bottom'],
    '9': ['top', 'both', 'middle', 'right', 'blank']
    }

# Prints horizontal dashes depending on size
def horizontal(size):
    return ' '+'-'*size+' '
    
# Prints vertical lines on the left depending on size
def verticalLeft(size):
    return '|'+' '*(size+1)

# Prints vertical lines towards the right depending on size
def verticalRight(size):
    return ' '*(size+1) + '|'

# Prints vertical lines for both sides depending on size
def verticalboth(size):
    return '|'+' '*size+'|'

# Skips dashes and lines
def blank(size):
    return ' '*(size+2)

# Main class to display screen dashes and lines thorough size and output.     
def main():

    # Input value
    value = input()
    
    # Loops through untill entered 00
    while value != '00':

        # Represent dashed to print with lcdDictonary
        lcdScreenDisplay = ['','','','','']

        # split input into size and numbers 
        values = value.split()

        # Size value will be in the first slot
        size = int(values[0])

        # Number value will be placed after a space
        numbers = values[1]
        i = 0
        while i < 5:
            for num in numbers:
                lcdScreen = lcdDictionary[num] 
                if lcdScreen[i] == 'top' or lcdScreen[i] == 'middle' or lcdScreen[i] == 'bottom':
                    lcdScreenDisplay[i] = lcdScreenDisplay[i]+horizontal(size)
                elif lcdScreen[i] == 'blank':
                    lcdScreenDisplay[i] = lcdScreenDisplay[i]+blank(size)
                elif lcdScreen[i] == 'left':
                    lcdScreenDisplay[i] = lcdScreenDisplay[i]+verticalLeft(size)
                elif lcdScreen[i] == 'right':
                    lcdScreenDisplay[i] = lcdScreenDisplay[i]+verticalRight(size)
                else:
                    lcdScreenDisplay[i] = lcdScreenDisplay[i]+verticalboth(size)
            i+=1
        
        # Aligns horizontal and vertical dashed together to match with the size in range of screen display
        # Note: Did find Dr.Wagner sheet as reference for positioning. 
        variable1 = lcdScreenDisplay[1]
        variable3 = lcdScreenDisplay[3]
        for i in range(size-1):
            lcdScreenDisplay[1] = lcdScreenDisplay[1]+'\n'+ variable1
            lcdScreenDisplay[3] = lcdScreenDisplay[3]+ '\n'+ variable3
         
        for val in lcdScreenDisplay:
            print(val)
        value = input() 
        
    # Ends loop once entered 00.
    else:
        print("Done")
        
    
main()