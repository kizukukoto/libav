from ctypes import ( c_int, c_int64,
                     c_uint, c_uint8, 
                     c_char,
                     c_double, c_ubyte,
                     c_size_t,
                     c_void_p, c_char_p,
                     POINTER, CFUNCTYPE, Structure )
from .codec import AVCodec, AVCodecContext, AVCodecParameters, AVCodecParserContext, AVPacket, AVPacketSideData
from .io import AVIOContext, AVIOInterruptCB
from .dictionary import AVDictionary
from .rational import AVRational
from .util import AVClass
    
MAX_REORDER_DELAY = 16
    
class AVChapter(Structure): pass

class AVFormatInternal(Structure): pass

class AVIndexEntry(Structure): pass

class AVInputFormat(Structure): 
    _fields_ = [
        ('name', c_char_p)
    ]            
class AVOutputFormat(Structure): pass

class AVPacketList(Structure): pass

class AVProbeData(Structure):
    _fields_ = [
        ('filename', c_char_p),
        ('buf', POINTER(c_ubyte)),
        ('buf_size', c_int),
        ('mime_type', c_char_p)
    ]

class AVProgram(Structure): pass
   
class AVStreamInfo(Structure):
    _fields_ = [
        ('last_dts', c_int64),
        ('duration_gcd', c_int64),
        ('duration_count', c_int),
        ('rfps_duration_sum', c_int64),
        ('duration_error', POINTER(c_double * 2 * (30*12+30+3+6))),
        ('codec_info_duration', c_int64), 
        ('codec_info_duration_fields', c_int64), 
        ('frame_delay_evidence', c_int), 
        ('found_decoder', c_int), 
        ('last_duration', c_int64), 
        ('fps_first_dts', c_int64), 
        ('fps_first_dts_idx', c_int), 
        ('fps_last_dts', c_int64), 
        ('fps_last_dts_idx', c_int), 
     ]

class AVStreamInternal(Structure): pass
     
class AVStream(Structure):
    _fields_ = [
        ('index', c_int),
        ('id', c_int),
        ('codec', POINTER(AVCodecContext)),
        ('priv_data', c_void_p),
        ('time_base', AVRational),
        ('start_time', c_int64),
        ('duration', c_int64),
        ('nb_frames', c_int64),
        ('disposition', c_int),
        ('discard', c_int),
        ('sample_aspect_ratio', AVRational),
        ('metadata', POINTER(AVDictionary)),
        ('avg_frame_rate', AVRational),
        ('attached_pic', AVPacket),
        ('side_data', POINTER(AVPacketSideData)),
        ('nb_side_data', c_int),
        ('event_flags', c_int),
        ('r_frame_rate', AVRational),
        ('recommended_encoder_configuration', c_char_p),
        ('codecpar', POINTER(AVCodecParameters)),
        ('info', POINTER(AVStreamInfo)),
        ('pts_wrap_bits', c_int),
        ('first_dts', c_int64),
        ('cur_dts', c_int64),
        ('last_IP_pts', c_int64),
        ('last_IP_duration', c_int),
        ('probe_packets', c_int),
        ('codec_info_nb_frames', c_int),
        ('need_parsing', c_int),
        ('parser', POINTER(AVCodecParserContext)),
        ('last_in_packet_buffer', POINTER(AVPacketList)),
        ('probe_data', AVProbeData),
        ('pts_buffer', c_int64 * (MAX_REORDER_DELAY+1)),
        ('index_entries', POINTER(AVIndexEntry)),
        ('nb_index_entries', c_int),
        ('index_entries_allocated_size', c_uint),
        ('stream_identifier', c_int),
        ('interleaver_chunk_size', c_int64),
        ('interleaver_chunk_duration', c_int64),
        ('request_probe', c_int),
        ('skip_to_keyframe', c_int),
        ('skip_samples', c_int),
        ('start_skip_samples', c_int64),
        ('first_discard_sample', c_int64),
        ('last_discard_sample', c_int64),
        ('nb_decoded_frames', c_int),
        ('mux_ts_offset', c_int64),
        ('pts_wrap_reference', c_int64),
        ('pts_wrap_behavior', c_int),
        ('update_initial_durations_done', c_int),
        ('pts_reorder_error', c_int64 * (MAX_REORDER_DELAY+1)),
        ('pts_reorder_error_count', c_uint8 * (MAX_REORDER_DELAY+1)),
        ('last_dts_for_order_check', c_int64),
        ('dts_ordered', c_uint8),
        ('dts_misordered', c_uint8),
        ('inject_global_side_data', c_int),
        ('display_aspect_ratio', AVRational),
        ('internal', POINTER(AVStreamInternal))
    ] 
    
class AVFormatContext(Structure): pass
AVFormatContext._fields_ = [
        ('av_class', POINTER(AVClass)),
        ('iformat', POINTER(AVInputFormat)),
        ('oformat', POINTER(AVOutputFormat)),
        ('priv_data', c_void_p),
        ('pb', POINTER(AVIOContext)),
        ('ctx_flags', c_int),
        ('nb_streams', c_uint),
        ('streams', POINTER(POINTER(AVStream))),
        ('url', c_char_p),
        ('start_time', c_int64),
        ('duration', c_int64),
        ('bit_rate', c_int64),
        ('packet_size', c_uint),
        ('max_delay', c_int),
        ('flags', c_int),
        ('probesize', c_int64),
        ('max_analyze_duration', c_int64),
        ('key', POINTER(c_uint8)),
        ('keylen', c_int),
        ('nb_programs', c_uint),
        ('programs', POINTER(POINTER(AVProgram))),
        ('video_codec_id', c_int),
        ('audio_codec_id', c_int),
        ('subtitle_codec_id', c_int),
        ('max_index_size', c_uint),
        ('max_picture_buffer', c_uint),
        ('nb_chapters', c_uint),
        ('chapters', POINTER(POINTER(AVChapter))),
        ('metadata', POINTER(AVDictionary)),
        ('start_time_realtime', c_int64),
        ('fps_probe_size', c_int),
        ('error_recognition', c_int),
        ('interrupt_callback', AVIOInterruptCB),
        ('debug', c_int),
        ('max_interleave_delta', c_int64),
        ('strict_std_compliance', c_int),
        ('event_flags', c_int),
        ('max_ts_probe', c_int),
        ('avoid_negative_ts', c_int),
        ('ts_id', c_int),
        ('audio_preload', c_int),
        ('max_chunk_duration', c_int),
        ('max_chunk_size', c_int),
        ('use_wallclock_as_timestamps', c_int),
        ('avio_flags', c_int),
        ('duration_estimation_method', c_uint),
        ('skip_initial_bytes', c_int64),
        ('correct_ts_overflow', c_uint),
        ('seek2any', c_int),
        ('flush_packets', c_int),
        ('probe_score', c_int),
        ('format_probesize', c_int),
        ('codec_whitelist', c_char_p),
        ('format_whitelist', c_char_p),
        ('internal', POINTER(AVFormatInternal)),
        ('io_repositioned', c_int),
        ('video_codec', POINTER(AVCodec)),
        ('audio_codec', POINTER(AVCodec)),
        ('subtitle_codec', POINTER(AVCodec)),
        ('data_codec', POINTER(AVCodec)),
        ('metadata_header_padding', c_int),
        ('opaque', c_void_p),
        ('control_message_cb', CFUNCTYPE(c_int, 
            POINTER(AVFormatContext), c_int, c_void_p,
            c_size_t)),
        ('output_ts_offset', c_int64),
        ('dump_separator', POINTER(c_uint8)),
        ('data_codec_id', c_int),
        ('protocol_whitelist', c_char_p),
        ('io_open', CFUNCTYPE(c_int, 
            POINTER(AVFormatContext), 
            POINTER(POINTER(AVIOContext)),
            c_char_p, c_int,
            POINTER(POINTER(AVDictionary)))),
        ('io_close', CFUNCTYPE(None, 
            POINTER(AVFormatContext), POINTER(AVIOContext))),
        ('protocol_blacklist', c_char_p),
        ('max_streams', c_int)
        ]    
