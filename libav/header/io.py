from ctypes import ( c_int,
                     c_void_p,
                     CFUNCTYPE, Structure )

class AVIOContext(Structure): pass

class AVIOInterruptCB(Structure):
    _fields_ = [
        ('callback', CFUNCTYPE(c_int, c_void_p)),
        ('opaque', c_void_p)
    ]