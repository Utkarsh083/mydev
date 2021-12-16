import qrcode
a="8840354059@ybl"
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
#qr.add_data(a)
img = qrcode.make(a)
img.save("payment1.png")
print(img)

