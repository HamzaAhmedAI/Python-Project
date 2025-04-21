from pyzbar.pyzbar import decode
from PIL import Image


img = Image.open('C:/Users/Lucifer_2.0/OneDrive/Pictures/New folder/qrcode1.png')
# Open the image file

result = decode(img)

print(result[0].data.decode('utf-8'))
# Decode the QR code data   