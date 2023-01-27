import qrcode

def qris(url,save):
    qr_code = qrcode.make(url)
    qr_code.save(save)
    try:
        qr = qrcode.QRCode(version=1,
                error_correction=qrcode.ERROR_CORRECT_H,
                box_size=30,border=1)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",back_color = "white" )
        img.save(save)
    except ValueError:
        print("there was an error")
    print("Successful")
url = input("Input your URL: \n")
save = input("Input your title of image and type of image\nExample: (image.jpg): \n")

qris(url,save)
