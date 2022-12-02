#Dhruv Patel
#CAC 190
#9/12/2022
#Problem 2 Poker Hands


import re

# Class to compare and validate deck in hand. 
def validateHand(playershand):
    if re.match(r'^[2-9tajqk]{5}$', playershand) and not re.match(r'^(.)\1\1\1\1$', playershand):
        return True
    else:
        return False

def validateSuits(playershand):
    if re.match(r'^[dhsc]{5}$', playershand):
        return True
    else:
        return False

# Class for playershand and suits value to determine the values within the hand and calculate points
def defineHand(playershand, suits):
    sortedHand = ''.join(sorted(playershand))
    highCardValues = ['a', 'k', 'q', 'j', 't', '9', '8', '7']
    points = 0

    # Sorted Hands are Straight Flush
    if re.match(r'2345a|23456|34567|45678|56789|6789t|789jt|89jqt|9jkqt|ajkqt', sortedHand) and re.match(r'^(.)\1\1\1\1$', suits):
        points = 22
        return points

    # Sorted Hands are Four of a Kind
    if re.match(r'.*(.)\1\1\1.*', sortedHand):
        points = 21
        return points

    # Players hands are Full House
    if len(set(playershand)) == 2:
        # return 'Full House'
        points = 20
        return points

    # Sorted Hands are flush
    if re.match(r'.*(.)\1\1\1\1.*', suits):
        # return 'Flush'
        points = 19
        return points

    # Sorted Hands are straight
    if re.match(r'2345a|23456|34567|45678|56789|6789t|789jt|89jqt|9jkqt|ajkqt', sortedHand):
        # return 'Straight'
        points = 18
        return points
        
    # Sorted Hands are three of a pair
    if re.match(r'.*(.)\1\1.*', sortedHand):
        # return 'Three of a Kind'
        points = 17
        return points

    # Sorted Hands are two paris
    if len(set(playershand)) == 3:
        # return 'Two Pair'
        points = 16
        return points

    # Sorted Hands are a pair
    if re.match(r'.*(.)\1.*', sortedHand):
        # return 'Pair'
        points = 15
        return points

    # Else Every other card is classified as high card
    else:
        for hands in highCardValues:
            if hands in playershand:
                points = hands
                break

        # loops through high card values string and adds them to the points.  
        if points=='t':
            points = 10
        if points=='j':
            points = 11
        if points=='q':
            points = 12
        if points=='k':
            points = 13
        if points=='a':
            points = 14
        return int(points)

# Class for validating which player has the highest points per value of suits and card.
def deterWinner(player1HandCardValue, player2HandCardValue, player1HandSuitValue, player2HandSuitValue):
    if validateHand(player1HandCardValue) and validateSuits(player1HandSuitValue) and validateHand(player2HandCardValue) and validateSuits(player2HandSuitValue):
        # Calculates player 1 and player 2 value
        player1 = defineHand(player1HandCardValue, player2HandSuitValue)
        player2 = defineHand(player2HandCardValue, player2HandSuitValue)

        # If player 1 has more points then player 2 player 1 win. 
        if player1 > player2:
            return "Player 1 WINS"

        # If player 2 has more points then player 1 then player 2 wins.
        if player1 < player2:
            return "Player 2 WINS"

        #Else its a Tie.    
        else:
            return "TIE"
    else:
        return 'Invalid hand entry'
    

# Main function will ask for player 1 and player 2 poker hand input to deside upon the winner between the two. 
def main():

    # Input player 1 and player 2 cards
    player1Hand = input("Enter Player 1 hand: ").lower()
    player2Hand = input("Enter Player 2 hand: ").lower()

    # Splits each cards in players hand
    player1HandDeck = player1Hand.split(" ")
    player2HandDeck = player2Hand.split(" ")

    # Displays the split cards within in an empty string of each players hand value
    player1HandCardValue = ""
    player1HandSuitValue = ""
    player2HandCardValue = ""
    player2HandSuitValue = ""
    
    for i in player1HandDeck:
        player1HandCardValue += i[0]
    
    for j in player1HandDeck:
        player1HandSuitValue += j[1]
        
    for i in player2HandDeck:
        player2HandCardValue += i[0]
    
    for j in player2HandDeck:
        player2HandSuitValue += j[1]
            
    print(deterWinner(player1HandCardValue, player2HandCardValue, player1HandSuitValue, player2HandSuitValue))

main()