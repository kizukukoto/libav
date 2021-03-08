from sys import platform
from ctypes import c_uint
from .common import register

LIBPOSTPROC = 'postproc'

if platform == 'win32':
  LIBRARY = register(LIBPOSTPROC)
else:
  LIBRARY = register('lib%s' % LIBPOSTPROC)

postproc_version = LIBRARY.postproc_version
LIBRARY.postproc_version.argtypes = None
LIBRARY.postproc_version.restype = c_uint
