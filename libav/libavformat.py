from sys import platform
from ctypes import ( c_int, 
                     c_uint,
                     c_int64,
                     c_char_p,
                     POINTER )
from .header.dictionary import AVDictionary
from .header.format import AVFormatContext, AVInputFormat, AVStream
from .header.frame import AVFrame
from .header.codec import AVCodec, AVPacket
from .header.rational import AVRational
from .common import register

LIBAVFORMAT = 'avformat'

if platform == 'win32':
  LIBRARY = register(LIBAVFORMAT)
else:
  LIBRARY = register('lib%s' % LIBAVFORMAT)

# av_find_best_stream
av_find_best_stream = LIBRARY.av_find_best_stream
LIBRARY.av_find_best_stream.argtypes = [ POINTER(AVFormatContext),
                                         c_int,
                                         c_int,
                                         c_int,
                                         POINTER(POINTER(AVCodec)),
                                         c_int ]
LIBRARY.av_find_best_stream.restype = c_int                  

# av_guess_frame_rate
av_guess_frame_rate = LIBRARY.av_guess_frame_rate
LIBRARY.av_guess_frame_rate.argtypes = [ POINTER(AVFormatContext),
                                         POINTER(AVStream),
                                         POINTER(AVFrame) ]
LIBRARY.av_guess_frame_rate.restype = AVRational

# av_read_frame
av_read_frame = LIBRARY.av_read_frame
LIBRARY.av_read_frame.argtypes = [ POINTER(AVFormatContext),
                                   POINTER(AVPacket) ]
LIBRARY.av_read_frame.restype = c_int

# av_seek_frame
av_seek_frame = LIBRARY.av_seek_frame
LIBRARY.av_seek_frame.argtypes = [ POINTER(AVFormatContext),
                                   c_int,
                                   c_int64,
                                   c_int ] 
LIBRARY.av_seek_frame.restype = c_int

# avformat_find_stream_info
avformat_find_stream_info = LIBRARY.avformat_find_stream_info
LIBRARY.avformat_find_stream_info.argtypes = [ POINTER(AVFormatContext),
                                               POINTER(POINTER(AVDictionary)) ]
LIBRARY.avformat_find_stream_info.restype = c_int

# avformat_alloc_context
avformat_alloc_context = LIBRARY.avformat_alloc_context
LIBRARY.avformat_alloc_context.argtypes = None
LIBRARY.avformat_alloc_context.restype = POINTER(AVFormatContext)
          
# avformat_close_input
avformat_close_input = LIBRARY.avformat_close_input
LIBRARY.avformat_close_input.argtypes = [ POINTER(POINTER(AVFormatContext)) ]
LIBRARY.avformat_close_inputrestype = None
          
# avformat_open_input
avformat_open_input = LIBRARY.avformat_open_input
LIBRARY.avformat_open_input.argtypes = [ POINTER(POINTER(AVFormatContext)), 
                                         c_char_p, 
                                         POINTER(AVInputFormat), 
                                         POINTER(POINTER(AVDictionary)) ]
LIBRARY.avformat_open_input.restype = c_int
                                         
# avformat_version            
avformat_version = LIBRARY.avformat_version
LIBRARY.avformat_version.restype = c_uint
LIBRARY.avformat_version.argtypes = None
