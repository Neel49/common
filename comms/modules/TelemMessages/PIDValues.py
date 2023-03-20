"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class PIDValues(object):
    __slots__ = ["P", "I", "D"]

    __typenames__ = ["double", "double", "double"]

    __dimensions__ = [None, None, None]

    def __init__(self):
        self.P = 0.0
        self.I = 0.0
        self.D = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(PIDValues._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">ddd", self.P, self.I, self.D))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != PIDValues._get_packed_fingerprint():
            raise ValueError("Decode error")
        return PIDValues._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = PIDValues()
        self.P, self.I, self.D = struct.unpack(">ddd", buf.read(24))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if PIDValues in parents: return 0
        tmphash = (0x573f2de20d48e523) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if PIDValues._packed_fingerprint is None:
            PIDValues._packed_fingerprint = struct.pack(">Q", PIDValues._get_hash_recursive([]))
        return PIDValues._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", PIDValues._get_packed_fingerprint())[0]

