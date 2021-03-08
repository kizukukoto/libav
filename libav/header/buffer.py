from ctypes import ( c_int, 
                     c_uint8,
                     POINTER, Structure )

class AVBuffer(Structure):
    _fields_ = [
        ('data', POINTER(c_uint8)),
        ('size', c_int),       
    ]  
	
class AVBufferRef(Structure):
    _fields_ = [
        ('buffer', POINTER(AVBuffer)),
        ('data', POINTER(c_uint8)),
        ('size', c_int)
    ]