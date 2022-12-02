# Dhruv Patel
# CAC 190
# 11/27/2022
# Problem 17 Planets

import Planets

# Function to sort list by Planet name
def SortByName(PlanetList):

    # Created empty list
    SortedNameList = []
    
    # While the length of the planet list is not less then 0:
    while len(PlanetList)>0:

        # Sets Temp as first planet within PlantName class
        Temp = PlanetList[0].PlanetName()
        
        # Counter
        TempPlanet = 0

        # For planet in range of length of planet list:
        for Planet in range(len(PlanetList)):

            # Loops through planet list from Planet name and as long as its greater then temp or before continue:
            if PlanetList[Planet].PlanetName()<Temp:

                # set temp to new planet name
                Temp = PlanetList[Planet].PlanetName()
                
                # Set TempPlanet to current planet index
                TempPlanet = Planet

        # Appends each loop to the sorted list
        SortedNameList.append(PlanetList[TempPlanet])

        # Removes temp planet created in begging
        PlanetList.remove(PlanetList[TempPlanet])
    
    # Returns the new sorted list
    return SortedNameList

# Function to sort list by distance from sun
def SortByDistance(PlanetList):

    # Creates a empty list to store later
    SortedDistanceList = []

    # While the length of the PlanetList Is less then 0 Continue:
    while len(PlanetList)>0:

        # Store Temp variable as the first list from the distance from sun category
        Temp = PlanetList[0].DistanceFromSun()

        # Sets value to 0 as counter
        TempPlanet = 0

        # For each planet in range of the planet list:
        for Planet in range(len(PlanetList)):

            # If the PlanetPosition distance form sun is value is less then Temp value then:
            if PlanetList[Planet].DistanceFromSun()<Temp:

                # Set the temp value to the current planet
                Temp = PlanetList[Planet].DistanceFromSun()

                # Sets the temp Planet to the current planet
                TempPlanet = Planet
        
        # Appends the PlanetPosition gathered from loop to the sorted list
        SortedDistanceList.append(PlanetList[TempPlanet])

        # removes TempPosition
        PlanetList.remove(PlanetList[TempPlanet])
    
    # Return Sorted List
    return SortedDistanceList        

# Main function to run all calculation       
def main():
    Mercury = Planets.Planet('Mercury',1516,(3.285*10**23),1)
    Venus = Planets.Planet('Venus',3760.4,(4.867*10**24),2)
    Earth = Planets.Planet('Earth',3958.8,(5.972 * 10**24),3)
    Mars = Planets.Planet('Mars',2106.1,(6.39*10**23),4)
    Jupiter = Planets.Planet('Jupiter',43441,(1.898*10**27),5)
    Saturn = Planets.Planet('Saturn',36184,(5.683 * 10**26),6)
    Uranus = Planets.Planet('Uranus',15759,(8.681 * 10**25),7)
    Neptune = Planets.Planet('Neptune',15299,(1.024 * 10**26),8)
    Pluto = Planets.Planet('Pluto',738.38,(1.30900 * 10**22),9)
    
    # Lists of Planets
    PlanetList = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
    
    # Prints out the sorted order by planets name
    print('\nSorted Order By Planets Name:')
    PlanetList = SortByName(PlanetList)
    for planet in PlanetList:
        planet.PlanetDetail()
    
    # Prints out the sorted list by planet distance from sun
    print('\nSorted Order By Distance From Sun:')
    PlanetList = SortByDistance(PlanetList)
    for planet in PlanetList:
        planet.PlanetDetail()


main()