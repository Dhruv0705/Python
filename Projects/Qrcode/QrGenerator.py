'''
This program is generating a QR code image file using the qrcode library. 
    It takes in a link as input and prompts the user to name the file they want to save the QR code image as. 
    The QR code is generated with a version of 1, error correction level of 'H', box size of 10, and a border of 4. 
    The QR code is filled with white color and the background is black. The QR code image is then saved as a .png file 
    with the name specified by the user.
'''

import qrcode
from PIL import ImageFile

# Creating a QR code object with the following parameters:
    # version: version of the QR code, default is 1
    # error_correction: level of error correction, default is 'ERROR_CORRECT_L'
    # box_size: size of the box in pixels, default is 10
    # border: width of the border in boxes, default is 4

QR = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

# Adding data to the QR code object
QR.add_data(input("Enter link to generate QR code: "))

# Asking the user to enter the name to save the file as
SaveFile = input("Save As: ")

# Fitting the data into the QR code object
QR.make(fit=True)

# Creating the image of the QR code with the specified color parameters
Img = QR.make_image(fill_color='White', back_color='Black')

# Saving the image of the QR code with the specified file name
Img.save(f"{SaveFile}.png")