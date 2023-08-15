#pip install qrcode[pil]

import qrcode

file_name = 'ccn_2023_poster'
path = f"https://akazemian.github.io/research/{file_name}.pdf"

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(path)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it
img.save(f"{file_name}.png")
