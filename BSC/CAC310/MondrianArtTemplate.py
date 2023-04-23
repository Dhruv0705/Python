# Dhruv Patel
# 4/21/2023
# CAC 310 Project 2 Mondrian Art
# Created by Ben Stephenson (ben.stephenson@ucalgary.ca)
#
#  Draw random "art" in a Mondrian style
#
import tkinter as tk
import random

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

#
# TODO: 
# Select a color randomly
#

def randomColor():
  R = random.randint(0,255)
  G = random.randint(0,255)
  B = random.randint(0,255)
  return "#%02x%02x%02x" % (R, G, B)

#
# TODO:
# Split the region both vertically and horizontally
# Invoke mondrian on all four quadrants

# Function to split both vertically and horizontally
def split_both(x, y, w, h, canvas):

  # Randomly select a point to split the region for both horizontal and vertical
  horizontal_split_point = random.randrange(33, 68) / 100
  vertical_split_point = random.randrange(33, 68) / 100

  # Calculate the width and height of the four quadrants
  left_width = round(horizontal_split_point * w)
  right_width = w - left_width
  top_height = round(vertical_split_point * h)
  bottom_height = h - top_height

  # Invoke mondrian on all four quadrants
  mondrian(x, y, left_width, top_height, canvas)
  mondrian(x + left_width, y, right_width, top_height, canvas) 
  mondrian(x, y + top_height, left_width, bottom_height, canvas) 
  mondrian(x + left_width, y + top_height, right_width, bottom_height, canvas)


  

#
# TODO:
# Split so that the regions are side by side
# Invoke mondrian on both halves
#

# Function to split horizontally
def split_horizontal(x, y, w, h, canvas):

  # Randomly select a point to split the region horizontally
  horizontal_split_point = random.randrange(33, 68) / 100

  # Calculate the width of the two halves
  left_width = round(horizontal_split_point * w)
  right_width = w - left_width

  # Invoke mondrian on both halves
  mondrian(x, y, left_width, h, canvas)
  mondrian(x + left_width, y, right_width, h, canvas)
    


#
# TODO:
# Split so that one region is above the other
# Invoke mondrian on both halves
#

# Function to split vertically
def split_vertical(x, y, w, h, canvas):

  # Randomly select a point to split the region vertically
  vertical_split_point = random.randrange(33, 68) / 100

  # Calculate the top and bottom height of the two halves
  top_height = round(vertical_split_point * h)
  bottom_height = h - top_height

  # Invoke mondrian on both halves
  mondrian(x, y, w, top_height, canvas)
  mondrian(x, y + top_height, w, bottom_height, canvas) 



#
# TODO: 
# Use recursion to draw "art" in a Mondrian style
# This is the algorithm in the project description
#

# Function to draw "art" in a Mondrian style
def mondrian(x, y, w, h, canvas):
    
  # Base case
  if w > WIDTH / 2 and h > HEIGHT / 2:
    split_both(x, y, w, h, canvas)

  # Recursive case to split horizontally
  elif w > WIDTH / 2:
    split_horizontal(x, y, w, h, canvas)

  # Recursive case to split vertically
  elif h > HEIGHT / 2:
    split_vertical(x, y, w, h, canvas)

  # Recursive case to split both horizontally and vertically if the region is large enough
  else:  

    # Randomly select a point to split the region for both horizontal and vertical
    horizontal_split_point = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * w) + 1, SPLIT_LOW + 1))
    vertical_split_point = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * h) + 1,  SPLIT_LOW + 1))
      
    # Split both horizontally and vertically if the region is large enough
    if horizontal_split_point < w and vertical_split_point < h:
      split_both(x, y, w, h, canvas)

    # Split horizontally if the region is large enough
    elif horizontal_split_point < w:
      split_horizontal(x, y, w, h, canvas)
      
    # Split vertically if the region is large enough
    elif vertical_split_point < h:
      split_vertical(x, y, w, h, canvas)

    # Draw a rectangle if the region is too small to split
    else:
      color = randomColor()
      canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline="black", width=3)


  
#
# Main method - driver of the program
#

def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, WIDTH, HEIGHT, canvas)
  tk.mainloop()

main()
