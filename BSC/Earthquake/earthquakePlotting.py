# Dhruv Patel
# 9/12/2022
# CAC 350
# Earthquake Data

import matplotlib.pyplot as plt
import numpy as np


# open file
earthquakes = open('all_month.csv','r')

# headerline - reads and throw a way
earthquakes.readline()

#lists of data - date, count, depth, magnitude, location, type, error, and source. 
dateDict = {}
dates = []
counts = []
depths = []
magnitudes = []
magType = []
place = []
type = []
depthError =[]
locationSource = []


# Read the file, one line at a time and store the data
for aline in earthquakes: 
    values = aline.split(',')
    dateOccurred = values[0][0:10]

  # Determine if date is already in dictionary
  
    if dateOccurred not in dateDict:

    # Add the date and set count to one
        dateDict[dateOccurred] = 1
    else: 

    # Find value in dictionary and add one
        dateDict[dateOccurred] += 1

  #
    dates.append(dateOccurred)
    depths.append(float(values[3]))  
    magnitudes.append(float(values[4]))
  

# Want to plot dates vs. counts
# Need to store in lists
datesOccurred = sorted(dateDict.keys())
for d in datesOccurred:
  counts.append(dateDict[d])

# Find date of max and min magnitude 
maxMag = max(magnitudes)
pos = magnitudes.index(maxMag)
maxDate = dates[pos]

minMag = min(magnitudes)
pos = magnitudes.index(minMag)
minDate = dates[pos]



# Add a vertical line for max mag date
pos2 = datesOccurred.index(maxDate)

plt.axvline(pos2, color='red')
plt.plot(datesOccurred, counts)
# plt.show()
plt.savefig('myplot.png')



# Notes/ Report: 

# I was able to plot the max and min through code from other projects but was unable to find the median and mean and the perdcentilies throgh the program.
# I can try to work on this more after meeting next day but I was able to find the rest of the report manualy. 

# The average magnitude in ml is 1.664963ml
# The MAX was 7.7
# The MIN was -1.31
# The Median was 1.41
# The Mean was 1.89999998
# The 25th Percentile was -1.27
# The 75th Percentile was 7.7

# The highest magnitude is 7.7 in the 75th percentile near 100% percentile and it is located in southeaset of the Loyalty Islands in the US. 
# The lowest magnitude is -1.31 under the 25th percentile it is located Northwest of Karluk alaska in the US.

# The histograms were ploteed through the plate. 


