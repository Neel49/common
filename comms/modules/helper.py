"""
Autogenerated helper functions
"""

from . import TelemMessages


def decode_msg(buf):
    """
    Returns message class based on header type
    """

    raw_data = buf.getbuffer().tobytes()
    if raw_data[3] == 0x0:
        return TelemMessages.JetsonOdometryData()._decode_one(buf)
    elif raw_data[3] == 0x1:
        return TelemMessages.JetsonMovementRequest()._decode_one(buf)
    elif raw_data[3] == 0x2:
        return TelemMessages.JetsonRelativeMovementCommand()._decode_one(buf)
    elif raw_data[3] == 0x3:
        return TelemMessages.JetsonLandingInitiationCommand()._decode_one(buf)
    elif raw_data[3] == 0x4:
        return TelemMessages.GroundStationWaypoints()._decode_one(buf)
    elif raw_data[3] == 0x5:
        return TelemMessages.GroundStationDisarm()._decode_one(buf)
    elif raw_data[3] == 0x6:
        return TelemMessages.GroundStationPIDValues()._decode_one(buf)
    elif raw_data[3] == 0x7:
        return TelemMessages.GroundStationData()._decode_one(buf)
    elif raw_data[3] == 0x8:
        return TelemMessages.GroundStationPIDSetResponse()._decode_one(buf)
    else:
        return None


def message_picker(i: int):
    """
    Returns message class based on modulus
    """

    message = i % 9
    if message == 0x0:
        return TelemMessages.JetsonOdometryData()
    elif message == 0x1:
        return TelemMessages.JetsonMovementRequest()
    elif message == 0x2:
        return TelemMessages.JetsonRelativeMovementCommand()
    elif message == 0x3:
        return TelemMessages.JetsonLandingInitiationCommand()
    elif message == 0x4:
        return TelemMessages.GroundStationWaypoints()
    elif message == 0x5:
        return TelemMessages.GroundStationDisarm()
    elif message == 0x6:
        return TelemMessages.GroundStationPIDValues()
    elif message == 0x7:
        return TelemMessages.GroundStationData()
    elif message == 0x8:
        return TelemMessages.GroundStationPIDSetResponse()
    else:
        return None
