from gh_avatars import Avatar

ava = Avatar(
    background='#f2f1f2',  # HEX-color string only
    resolution=12, # Width of pixel grid
    size=500  # Multiple of resolution
)

image = ava.generate(
    nick='mdpanf',
    color='#084C61'  # HEX-color string only
)

image.show()
