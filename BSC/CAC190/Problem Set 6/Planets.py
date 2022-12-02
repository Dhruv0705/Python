# Dhruv Patel
# CAC 190
# 11/27/2022
# Problem 17 Planets

class Planet:

    # Defining Name, Radius, Mass, Distance
    def __init__(self,Name,Radius,Mass,Distance):
        self.name = Name
        self.radius = Radius
        self.mass = Mass
        self.distance = Distance 
    
    # Function to compute gravity of a planet
    def Gravity(self):

        GravityFormula = 6.67 * 10**-11
        Gravity = (GravityFormula * self.mass)/(self.radius**2)
        return Gravity

    # Function to return the distance from sun
    def DistanceFromSun(self):
        return self.distance
    
    # Function to return the name of the planet
    def PlanetName(self):
        return self.name
    
    # Function to print out all detail of plant
    def PlanetDetail(self):
        print('Name:',self.name)
        print('Radius:',self.radius)
        print('Mass:',self.mass)
        print('Gravity:',self.Gravity())
        print('Distance from sun:',self.distance)

# Testing Code
if __name__=='__main__':
    Earth = Planet('Earth',3958.8,(5.972 * 10**24),3)
    print(Earth.Gravity())
    Earth.PlanetDetail()

