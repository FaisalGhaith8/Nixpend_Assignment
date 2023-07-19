import qrcode
from qrcode.image.pure import PyPNGImage
    
def generate_qr(data,name):
    img = qrcode.make(data, image_factory=PyPNGImage)
    img.save(f"{name}.png")
    return