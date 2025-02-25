"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

from .. import TelemMessages



class GroundStationPIDValues(object):
    __slots__ = ["header", "controller", "axis", "values"]

    __typenames__ = ["TelemMessages.Header", "byte", "byte", "TelemMessages.PIDValues"]

    __dimensions__ = [None, None, None, None]

    def __init__(self):
        self.header = TelemMessages.Header()
        self.header.flag = 0x7e
        self.header.type = 0x6
        self.header.length = bytes([ 0x0, 0x1a ])
        self.controller = 0
        self.axis = 0
        self.values = TelemMessages.PIDValues()

    def encode(self):
        buf = BytesIO()
        buf.write(GroundStationPIDValues._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == TelemMessages.Header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">BB", self.controller, self.axis))
        assert self.values._get_packed_fingerprint() == TelemMessages.PIDValues._get_packed_fingerprint()
        self.values._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != GroundStationPIDValues._get_packed_fingerprint():
            raise ValueError("Decode error")
        return GroundStationPIDValues._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = GroundStationPIDValues()
        self.header = TelemMessages.Header._decode_one(buf)
        self.controller, self.axis = struct.unpack(">BB", buf.read(2))
        self.values = TelemMessages.PIDValues._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if GroundStationPIDValues in parents: return 0
        newparents = parents + [GroundStationPIDValues]
        tmphash = (0x2652137388cd0657+ TelemMessages.Header._get_hash_recursive(newparents)+ TelemMessages.PIDValues._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if GroundStationPIDValues._packed_fingerprint is None:
            GroundStationPIDValues._packed_fingerprint = struct.pack(">Q", GroundStationPIDValues._get_hash_recursive([]))
        return GroundStationPIDValues._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", GroundStationPIDValues._get_packed_fingerprint())[0]

