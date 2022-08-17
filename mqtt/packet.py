class MQTTPacket:
    _HEADER_SIZE = 2

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

    @property
    def length(self):
        return self._HEADER_SIZE + self._size()

    def _size() -> int:
        return 0

class Connect(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x01
        self._flags = 0

class ConnnectACK(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x02
        self._flags = 0

class Publish(MQTTPacket):
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

class PublishACK(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x04
        self._flags = 0

class PublishReceived(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x05
        self._flags = 0

class PublishRelease(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x06
        self._flags = 0b0010

class PublishComplete(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x07
        self._flags = 0

class Subscribe(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x08
        self._flags = 0b0010

class SubscribeACK(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x09
        self._flags = 0

class Unsubscribe(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0a
        self._flags = 0b0010

class UnsubscribeACK(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0b
        self._flags = 0

class PingRequest(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0c
        self._flags = 0

class PingResponse(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0d
        self._flags = 0

class Disconnect(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0e
        self._flags = 0

class Auth(MQTTPacket):
    def __init__(self):
        super().__init__()
        self._type = 0x0f
        self._flags = 0
