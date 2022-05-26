from gh_avatars import Avatar

ava = Avatar(
    background='#f2f1f2',  # HEX-color string only
    resolution=7, # Width of a cell in pixels
    size=350  # Size of rendered image in pixels
)

image = ava.generate(
    nick="coodemonster2002",
    # color="color" # Use to specify exact color
)

image.show()

image.save("gravatar.png")
