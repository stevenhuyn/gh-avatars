from gh_avatars import Avatar

ava = Avatar(
    background='#f2f1f2',  # HEX-color string only
    resolution=21, # Width of pixel grid
    size=500  # Multiple of resolution
)

image = ava.generate(
    nick='chicken',
)

image.show()
