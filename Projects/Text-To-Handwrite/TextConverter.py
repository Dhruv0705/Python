import pywhatkit

Text = input("Enter Text To Generate To Handwriting: ")
SaveAs = input("Save As: ")

pywhatkit.text_to_handwriting(Text, SaveAs + ".png", [255,0,0])
print(" END ")