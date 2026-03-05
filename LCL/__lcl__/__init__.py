from os import symlink as __sym_link__
from os.path import dirname as __get_dir__
from PyPInclude import lib as __lib__
from time import time as __time__
from random import random as __random__

__all__ = []

__lib_pw__ = hash(str(__time__() + __random__()))