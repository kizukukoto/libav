from ctypes import ( c_int, c_int64,
                     c_uint8, c_uint64,
                     c_size_t,
                     c_void_p, c_char_p,
                     POINTER, Structure )
from .rational import AVRational
from .buffer import AVBufferRef
from .dictionary import AVDictionary

AV_NUM_DATA_POINTERS = 8

class AVFrameSideData(Structure): pass

class AVFrame(Structure): 
    _fields_ = [
        ('data', POINTER(c_uint8) * AV_NUM_DATA_POINTERS),
        ('linesize', c_int * AV_NUM_DATA_POINTERS),
        ('extended_data', POINTER(POINTER(c_uint8))),
        ('width', c_int),
        ('height', c_int),
        ('nb_samples', c_int),
        ('format', c_int),
        ('key_frame', c_int),
        ('pict_type', c_int),
        ('sample_aspect_ratio', AVRational),
        ('pts', c_int64),
        ('pkt_dts', c_int64),
        ('coded_picture_number', c_int),
        ('display_picture_number', c_int),
        ('quality', c_int),
        ('opaque', c_void_p),
        ('repeat_pict', c_int),
        ('interlaced_frame', c_int),
        ('top_field_first', c_int),
        ('palette_has_changed', c_int),
        ('reordered_opaque', c_int64),
        ('sample_rate', c_int),
        ('channel_layout', c_uint64),
        ('buf', POINTER(AVBufferRef) * AV_NUM_DATA_POINTERS),
        ('extended_buf', POINTER(POINTER(AVBufferRef))),
        ('nb_extended_buf', c_int),
        ('side_data', POINTER(POINTER(AVFrameSideData))),
        ('nb_side_data', c_int),
        ('flags', c_int),
        ('color_range', c_int),
        ('color_primaries', c_int),
        ('color_trc', c_int),
        ('colorspace', c_int),
        ('chroma_location', c_int),
        ('best_effort_timestamp', c_int64),
        ('pkt_pos', c_int64),
        ('pkt_duration', c_int64),
        ('metadata', POINTER(AVDictionary)),
        ('decode_error_flags', c_int),
        ('channels', c_int),
        ('pkt_size', c_int),
        ('hw_frames_ctx', POINTER(AVBufferRef)),
        ('opaque_ref', POINTER(AVBufferRef)),
        ('crop_top', c_size_t),
        ('crop_bottom', c_size_t),
        ('crop_left', c_size_t),
        ('crop_right', c_size_t),
        ('private_ref', POINTER(AVBufferRef)),
    ]
