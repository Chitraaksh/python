from PIL import Image

def site_qr():
 try:
    img = Image.open("Site.png")  # Replace with your image path
    img.show()
 except FileNotFoundError:
    print("Image file not found. Please check the path.")
