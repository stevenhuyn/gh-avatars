from gh_avatars import Avatar

ava = Avatar(
    background='#f2f1f2',  # HEX-color string only
    resolution=14, # Width of pixel grid
    size=350  # Multiple of resolution
)

image = ava.generate(
    nick='coolguy',
    # color='#084C61'  # HEX-color string only
)

image.show()

image.save("gravatar.png")
