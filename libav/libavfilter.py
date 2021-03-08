from sys import platform
from ctypes import c_uint
from .common import register

LIBAVFILTER = 'avfilter'

if platform == 'win32':
  LIBRARY = register(LIBAVFILTER)
else:
  LIBRARY = register('lib%s' % LIBAVFILTER)

avfilter_version = LIBRARY.avfilter_version
LIBRARY.avfilter_version.argtypes = None
LIBRARY.avfilter_version.restype = c_uint
