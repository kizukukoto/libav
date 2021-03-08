from sys import platform
from ctypes import c_uint
from .common import register

LIBAVDEVICE = 'avdevice'

if platform == 'win32':
  LIBRARY = register(LIBAVDEVICE)
else:
  LIBRARY = register('lib%s' % LIBAVDEVICE)

avdevice_version = LIBRARY.avdevice_version
LIBRARY.avdevice_version.argtypes = None
LIBRARY.avdevice_version.restype = c_uint
