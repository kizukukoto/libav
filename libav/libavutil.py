from sys import platform
from ctypes import ( c_int, c_int64,
                     c_uint,
                     c_char_p,
                     POINTER )
from .header.dictionary import AVDictionary, AVDictionaryEntry
from .header.frame import AVFrame
from .header.rational import AVRational
from .common import register

LIBAVUTIL = 'avutil'

if platform == 'win32':
  LIBRARY = register(LIBAVUTIL)
else:
  LIBRARY = register('lib%s' % LIBAVUTIL)

# av_dict_alloc
def av_dict_alloc():
    return POINTER(AVDictionary)()
    
# av_dict_free
av_dict_free = LIBRARY.av_dict_free
LIBRARY.av_dict_free.argtypes = [ POINTER(POINTER(AVDictionary)) ]
LIBRARY.av_dict_free.restype = None

# av_dict_get
av_dict_get = LIBRARY.av_dict_get
LIBRARY.av_dict_get.argtypes = [ POINTER(AVDictionary),
                                 c_char_p,
                                 POINTER(AVDictionaryEntry),
                                 c_int]
LIBRARY.av_dict_get.restype = POINTER(AVDictionaryEntry)

# av_dict_set
av_dict_set = LIBRARY.av_dict_set
LIBRARY.av_dict_set.argtypes = [ POINTER(POINTER(AVDictionary)),
                                 c_char_p,
                                 c_char_p,
                                 c_int]
LIBRARY.av_dict_set.restype = c_int
                                 
# av_frame_alloc
av_frame_alloc = LIBRARY.av_frame_alloc
LIBRARY.av_frame_alloc.argtypes = None
LIBRARY.av_frame_alloc.restype = POINTER(AVFrame)

# av_frame_free
av_frame_free = LIBRARY.av_frame_free
LIBRARY.av_frame_free.argtypes = [ POINTER(POINTER(AVFrame)) ]
LIBRARY.av_frame_free.restype = None

# av_frame_unref
av_frame_unref = LIBRARY.av_frame_unref
LIBRARY.av_frame_unref.argtypes = [ POINTER(AVFrame) ]
LIBRARY.av_frame_unref.restype = None

# av_log_get_level
av_log_get_level = LIBRARY.av_log_get_level
LIBRARY.av_log_get_level.argtypes = None  
LIBRARY.av_log_get_level.restype = c_int

# av_log_set_level
av_log_set_level = LIBRARY.av_log_set_level
LIBRARY.av_log_set_level.argtypes = [ c_int ]   
LIBRARY.av_log_set_level.restype = None

# av_rescale_q
av_rescale_q = LIBRARY.av_rescale_q
LIBRARY.av_rescale_q.argtypes = [ c_int64,
                                  AVRational,
                                  AVRational ]
LIBRARY.av_rescale_q.restype = c_int64
        
# avutil_version             
avutil_version = LIBRARY.avutil_version
LIBRARY.avutil_version.argtypes = None
LIBRARY.avutil_version.restype = c_uint
