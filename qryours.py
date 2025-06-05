import qrcode
data = input("Enter Your's Link to Convert QRCode")
qr=qrcode.make(data)
qr.save("qrcode.png")
print("Your's QRCode Generated Success !")
