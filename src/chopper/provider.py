import abc
from itertools import cycle

from .annotations import abstatic


class Provider(abc.ABC):

    @abstatic
    def nice_name():
        return None

    @abstatic
    def is_supporting(uri):
        return False

    @abstatic
    def max_chunk_size():
        return 0 # kbyte(s)
    
    @abstatic
    def trottle():
        return 0 # second(s)

    @abstatic
    def upload(content):
        return None

    @abstatic
    def download(uri):
        return None

class TrottlingException(Exception):
    pass