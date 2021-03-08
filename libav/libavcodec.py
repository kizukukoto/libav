from sys import platform
from ctypes import ( c_int,
                     c_uint,
                     POINTER )
from .header.dictionary import AVDictionary
from .header.frame import AVFrame
from .header.codec import AVCodec, AVCodecContext, AVPacket, AVCodecParameters
from .common import register

LIBAVCODEC = 'avcodec'

if platform == 'win32':
  LIBRARY = register(LIBAVCODEC)
else:
  LIBRARY = register('lib%s' % LIBAVCODEC)

# av_init_packet
av_init_packet =LIBRARY.av_init_packet
LIBRARY.av_init_packet.argtypes = [ POINTER(AVPacket) ]
LIBRARY.av_init_packet.restype = None

# av_packet_alloc
av_packet_alloc = LIBRARY.av_packet_alloc
LIBRARY.av_packet_alloc.argtypes = None
LIBRARY.av_packet_alloc.restype = POINTER(AVPacket)

# av_packet_unref
av_packet_unref = LIBRARY.av_packet_unref
LIBRARY.av_packet_unref.argtypes = [ POINTER(AVPacket) ] 
LIBRARY.av_packet_unref.restype = None

# avcodec_alloc_context3
avcodec_alloc_context3 = LIBRARY.avcodec_alloc_context3
LIBRARY.avcodec_alloc_context3.argtypes = [ POINTER(AVCodec) ]
LIBRARY.avcodec_alloc_context3.restype = POINTER(AVCodecContext)

# avcodec_find_decoder
avcodec_find_decoder = LIBRARY.avcodec_find_decoder
LIBRARY.avcodec_find_decoder.argtypes = [ c_int ]
LIBRARY.avcodec_find_decoder.restype = POINTER(AVCodec)

# avcodec_flush_buffers
avcodec_flush_buffers = LIBRARY.avcodec_flush_buffers
LIBRARY.avcodec_flush_buffers.argtypes = [ POINTER(AVCodecContext) ]
LIBRARY.avcodec_flush_buffers.restype = None

# avcodec_free_context
avcodec_free_context = LIBRARY.avcodec_free_context
LIBRARY.avcodec_free_context.argtypes = [ POINTER(POINTER(AVCodecContext)) ]
LIBRARY.avcodec_free_context.restype = None

# avcodec_open2
avcodec_open2 = LIBRARY.avcodec_open2
LIBRARY.avcodec_open2.argtypes = [ POINTER(AVCodecContext),
                                   POINTER(AVCodec), 
                                   POINTER(POINTER(AVDictionary)) ]
LIBRARY.avcodec_open2.restype = c_int

# avcodec_parameters_to_context
avcodec_parameters_to_context = LIBRARY.avcodec_parameters_to_context
avcodec_parameters_to_context.argtypes = [ POINTER(AVCodecContext),
                                           POINTER(AVCodecParameters) ]
avcodec_parameters_to_context.restype = c_int

# avcodec_receive_frame
avcodec_receive_frame = LIBRARY.avcodec_receive_frame
LIBRARY.avcodec_receive_frame.argtypes = [ POINTER(AVCodecContext),
                                           POINTER(AVFrame) ]
LIBRARY.avcodec_receive_frame.restype = c_int

# avcodec_send_packet
avcodec_send_packet = LIBRARY.avcodec_send_packet
LIBRARY.avcodec_send_packet.argtypes = [ POINTER(AVCodecContext),
                                         POINTER(AVPacket) ]
LIBRARY.avcodec_send_packetrestype = c_int

# avcodec_version
avcodec_version = LIBRARY.avcodec_version
LIBRARY.avcodec_version.argtypes = None
LIBRARY.avcodec_version.restype = c_uint
