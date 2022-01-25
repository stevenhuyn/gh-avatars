from gh_avatars import Avatar

ava = Avatar(
    size=120,  # Multiple of 12
    background='#f2f1f2'  # HEX-color string only
)

image = ava.generate(
    nick='mdpanf',
    color='#084C61'  # HEX-color string only
)

image.show()
