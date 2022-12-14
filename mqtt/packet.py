from typing import Tuple
from primitive import VariableByteInteger

class ControlPacket:
    def __init__(self):
        self._type = 0
        self._flags = 0
        self._length = 0

    @property
    def type(self):
        return self._type

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, value):
        self._flags = value

    def _size(self) -> int:
        return 0

    def encode(self) -> bytes:
        """Encode packet to a bytes object.

        Returns:
            A bytes object containing the encoded packet.
        """
        data = bytearray()
        data.append(self._type << 4 | self._flags)
        data += VariableByteInteger.encode(self._size())
        return bytes(data)

    def decode(self, data: bytes, offset: int = 0) -> int:
        """Decode a packet from a bytes object.

        Decodes the packet from a bytes object and loads the decoded
        content.

        Args:
            data: A bytes object containing the encoded packet.
            offset: An integer indicating the start index of encoded packet inside the bytes object.

        Returns:
            An integer indicating the number of bytes read.
        """
        start = offset
        self._type = data[offset] >> 4 & 0xf0
        self._flags = data[offset] & 0x0f
        offset += 1
        self._length, size = VariableByteInteger.decode(data, offset)
        offset += size
        return offset - start

    @classmethod
    def decode(cls, data: bytes, offset: int = 0) -> Tuple[object, int]:
        """Decode a packet from a bytes object.

        Decodes the packet from a bytes object and creates a new object
        instance with the decoded values.

        Args:
            data: A bytes object containing the encoded packet.
            offset: An integer indicating the start index of encoded packet inside the bytes object.

        Returns:
            A tuple with a new ControlPacket instance and the number of bytes read.
        """
        obj = cls()
        size = obj.decode(data, offset)
        return obj, size

class Connect(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x01
        self._flags = 0

class ConnnectACK(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x02
        self._flags = 0

class Publish(ControlPacket):
    _DUPLICATE_SHIFT = 3
    _DUPLICATE_MASK = 0b1

    _QOS_SHIFT = 1
    _QOS_MASK = 0b11

    _RETAIN_SHIFT = 0
    _RETAIN_MASK = 0b1

    def __init__(self):
        super().__init__()
        self._type = 0x03
        self._flags = 0

    @property
    def duplicate(self):
        return self._flags >> self._DUPLICATE_SHIFT & self._DUPLICATE_MASK

    @duplicate.setter
    def duplicate(self, value):
        self._flags = (self._flags & ~(self._DUPLICATE_MASK << self._DUPLICATE_SHIFT)) | (1 if value else 0 << self._DUPLICATE_SHIFT)

    @property
    def qos(self):
        return self._flags >> self._QOS_SHIFT & self._QOS_MASK

    @qos.setter
    def qos(self, value):
        self._flags = (self._flags & ~(self._QOS_MASK << self._QOS_SHIFT)) | (1 if value else 0 << self._QOS_SHIFT)

    @property
    def retain(self):
        return self._flags >> self._RETAIN_SHIFT & self._RETAIN_MASK

    @retain.setter
    def retain(self, value):
        self._retain = (self._retain & ~(self._RETAIN_MASK << self._RETAIN_SHIFT)) | (1 if value else 0 << self._RETAIN_SHIFT)

class PublishACK(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x04
        self._flags = 0

class PublishReceived(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x05
        self._flags = 0

class PublishRelease(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x06
        self._flags = 0b0010

class PublishComplete(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x07
        self._flags = 0

class Subscribe(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x08
        self._flags = 0b0010

class SubscribeACK(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x09
        self._flags = 0

class Unsubscribe(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0a
        self._flags = 0b0010

class UnsubscribeACK(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0b
        self._flags = 0

class PingRequest(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0c
        self._flags = 0

class PingResponse(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0d
        self._flags = 0

class Disconnect(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0e
        self._flags = 0

class Auth(ControlPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0f
        self._flags = 0
