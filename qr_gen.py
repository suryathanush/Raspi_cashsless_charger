import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)
qr.add_data('qrmech.be')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# for y in range(len(img)*2):                   # Scaling the bitmap by 2
#     for x in range(len(img[0])*2):            # because my screen is tiny.
#         value = not img[int(y/2)][int(x/2)]   # Inverting the values because
#         print(value, end="")            # black is `True` in the matrix.
#     print("\n")
# #oled.show()
rgb_img = img.convert("RGB")

img.save("qr.png")

print(rgb_img.mode)