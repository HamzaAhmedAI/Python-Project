import qrcode

data = "Don't forget to subscribe to my channel!"

qr = qrcode.QRCode(version =1, box_size=10, border=5)
# Create a QR code object with specified version, box size, and border size 

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")

img.save('C:/Users/Lucifer_2.0/OneDrive/Pictures/New folder/qrcode1.png')

