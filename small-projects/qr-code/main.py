import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=None,   # auto-size
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,  # it's the default minimum for this
)
qr.add_data("https://github.com/jubayed-02")
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    fill_color="black",
    back_color="white",

)
img.save("qr.png")
print("Saved qr.png")
