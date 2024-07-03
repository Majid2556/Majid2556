import qrcode
data = "barnamenevisinia"
img = qrcode.make(data)
img.save("MyQRCode.png")