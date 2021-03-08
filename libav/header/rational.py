from ctypes import ( c_int,
                     Structure )

class AVRational(Structure):
    _fields_ = [
        ('num', c_int),
        ('den', c_int)
    ]