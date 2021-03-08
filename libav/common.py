from os import environ, scandir
from ctypes import CDLL
from ctypes.util import find_library

def register(name):
    if environ.get('LIBAV_PATH',None):
        for file in scandir(environ.get('LIBAV_PATH',None)):
            if file.name.startswith(name): 
               library = CDLL('%s/%s' % (environ.get('LIBAV_PATH',None).replace('\\','/'),file.name))
    else:
    	library = CDLL(find_library(name))
    if library._name is None:
    	raise TypeError("CDLL type '{}' found while loading {}".format(library._name,name))
    return library