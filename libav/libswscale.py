from sys import platform
from ctypes import ( c_int, 
                     c_uint, c_uint8,
                     c_double,
                     POINTER )
from .header.scale import SwsContext, SwsFilter
from .common import register

LIBSWSCALE = 'swscale'

if platform == 'win32':
  LIBRARY = register(LIBSWSCALE)
else:
  LIBRARY = register('lib%s' % LIBSWSCALE)

# sws_alloc_context
sws_alloc_context = LIBRARY.sws_alloc_context
LIBRARY.sws_alloc_context.argtypes = None
LIBRARY.sws_alloc_context.restype = POINTER(SwsContext)

# sws_freeContext
sws_freeContext = LIBRARY.sws_freeContext
LIBRARY.sws_freeContext.argtypes = [ POINTER(SwsContext) ]
LIBRARY.sws_freeContext.restype = None

# sws_getCachedContext
sws_getCachedContext = LIBRARY.sws_getCachedContext
LIBRARY.sws_getCachedContext.argtypes = [ POINTER(SwsContext),
										  c_int, 
										  c_int, 
										  c_int, 
										  c_int, 
										  c_int, 
										  c_int, 
										  c_int, 
										  POINTER(SwsFilter), 
										  POINTER(SwsFilter), 
										  POINTER(c_double) ]
LIBRARY.sws_getCachedContext.restype = POINTER(SwsContext)

# sws_scale
sws_scale = LIBRARY.sws_scale
LIBRARY.sws_scale.argtypes = [ POINTER(SwsContext),
							   POINTER(POINTER(c_uint8)),
							   POINTER(c_int),
							   c_int, 
							   c_int,
							   POINTER(POINTER(c_uint8)),
							   POINTER(c_int) ]
LIBRARY.sws_scale.restype = c_int

# swscale_version                    
swscale_version = LIBRARY.swscale_version
LIBRARY.swscale_version.argtypes = None
LIBRARY.swscale_version.restype = c_uint
