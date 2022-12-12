import random
import string
def rgb_color_gen():
    item = range(0, 256)
    a = tuple(random.choice(item) for _ in range(3))
    print(a)
rgb_color_gen()
