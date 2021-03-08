from sys import platform
from ctypes import c_uint
from .common import register

LIBSWRESAMPLE = 'swresample'

if platform == 'win32':
  LIBRARY = register(LIBSWRESAMPLE)
else:
  LIBRARY = register('lib%s' % LIBSWRESAMPLE)

swresample_version = LIBRARY.swresample_version
LIBRARY.swresample_version.argtypes = None
LIBRARY.swresample_version.restype = c_uint
