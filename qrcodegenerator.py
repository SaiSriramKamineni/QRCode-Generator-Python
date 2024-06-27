import qrcode
from PIL import Image

# Define the data to be encoded in the QR code
data = "https://github.com/SaiSriramKamineni"

# Create a QRCode object with specified parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,  # Increase box size for a larger QR code
    border=4,     # Smaller border for a more compact QR code
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code with a more attractive color scheme
img = qr.make_image(fill_color="darkblue", back_color="skyblue")

# Save the image to a file
img.save("github.png")
