from math import floor
from random import random
import pycountry


def randInt(a, b):
    return a + floor(random() * (b - a))
