# Github avatars generator

Nick | gxp3lP (rnd)                           | non3kF (rnd)                          | mdpanf                           | Steio                          |
---- |----------------------------------------|---------------------------------------|----------------------------------|--------------------------------|
Ava  | ![example1](./examples/example_1.png)  | ![example2](./examples/example_2.png) | ![mdpanf](./examples/mdpanf.png) | ![Steio](./examples/Steio.png) | 

## Usage

### Install packages

`pip install -r requirements.txt`

### Create random avatar

```python
from gh_avatars import Avatar

ava = Avatar()
image = ava.generate()

image.save('file.png', 'PNG')
```

### Create nick-based avatar with params

```python
from gh_avatars import Avatar

ava = Avatar(
    background='#f2f1f2',  # HEX-color string only
    resolution=12, # Width of pixel grid
    size=120  # Multiple of resolution
)

image = ava.generate(
    nick='Steio',
    color='#084C61'  # HEX-color string only
)

image.save('Steio.png', 'PNG')
```

## Params

Avatar | size                   | background             |
-------|------------------------|------------------------|
Val    | **int** multiple of 12 | **str** back hex color |

generate() | nick    | color                   |
-----------|---------|-------------------------|
Val        | **str** | **str** block hex color |
