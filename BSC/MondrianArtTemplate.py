#Created by Ben Stephenson (ben.stephenson@ucalgary.ca)
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

def split_both(x, y, w, h, canvas):
  hsp = random.randrange(33, 68) / 100
  vsp = random.randrange(33, 68) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, left_width, top_height, canvas)
  mondrian(x + left_width, y, right_width, top_height, canvas) 
  mondrian(x, y + top_height, left_width, bottom_height, canvas) 
  mondrian(x + left_width, y + top_height, right_width, bottom_height, canvas)


  

#
# TODO:
# Split so that the regions are side by side
# Invoke mondrian on both halves
#
def split_horizontal(x, y, w, h, canvas):
  hsp = random.randrange(33, 68) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  mondrian(x, y, left_width, h, canvas)
  mondrian(x + left_width, y, right_width, h, canvas)
    


#
# TODO:
# Split so that one region is above the other
# Invoke mondrian on both halves
#
def split_vertical(x, y, w, h, canvas):

  vsp = random.randrange(33, 68) / 100
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, w, top_height, canvas)
  mondrian(x, y + top_height, w, bottom_height, canvas) 



#
# TODO: 
# Use recursion to draw "art" in a Mondrian style
# This is the algorithm in the project description
#
def mondrian(x, y, w, h, canvas):
    if w > WIDTH / 2 and h > HEIGHT / 2:
      split_both(x, y, w, h, canvas)
    elif w > WIDTH / 2:
      split_horizontal(x, y, w, h, canvas)
    elif h > HEIGHT / 2:
      split_vertical(x, y, w, h, canvas)
    else:  
      hsplit = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * w) + 1, SPLIT_LOW + 1))
      vsplit = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * h) + 1,  SPLIT_LOW + 1))
      if hsplit < w and vsplit < h:
        split_both(x, y, w, h, canvas)
      elif hsplit < w:
        split_horizontal(x, y, w, h, canvas)
      elif vsplit < h:
        split_vertical(x, y, w, h, canvas)
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
