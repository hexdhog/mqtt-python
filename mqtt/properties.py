from typing import Tuple
from primitive import VariableByteInteger

class PacketProperty:
    def __init__(self):
        self._id = 0
        self._value = None

    def encode(self) -> bytes:
        """Encode packet property to a bytes object.

        Returns:
            A bytes object containing the encoded packet property.
        """
        return bytes()

    def decode(self, data: bytes, offset: int = 0) -> int:
        """Decode a packet property from a bytes object.

        Decodes the packet property from a bytes object and loads the decoded
        content.

        Args:
            data: A bytes object containing the encoded packet property.
            offset: An integer indicating the start index of encoded packet property inside the bytes object.

        Returns:
            An integer indicating the number of bytes read.
        """
        return 0

    @classmethod
    def decode(cls, data: bytes, offset: int = 0) -> Tuple[object, int]:
        """Decode a packet property from a bytes object.

        Decodes the packet property from a bytes object and creates a new object
        instance with the decoded values.

        Args:
            data: A bytes object containing the encoded packet property.
            offset: An integer indicating the start index of encoded packet property inside the bytes object.

        Returns:
            A tuple with a new PacketProperty instance and the number of bytes read.
        """
        obj = cls()
        size = obj.decode(data, offset)
        return obj, size

class PayloadFormatIndicator(PacketProperty):
    def __init__(self):
        self._id = 0x01

class MessageExpiryInterval(PacketProperty):
    def __init__(self):
        self._id = 0x02

class ContentType(PacketProperty):
    def __init__(self):
        self._id = 0x03

class ResponseTopic(PacketProperty):
    def __init__(self):
        self._id = 0x08

class CorrelationData(PacketProperty):
    def __init__(self):
        self._id = 0x09

class SubscriptionIdentifier(PacketProperty):
    def __init__(self):
        self._id = 0x0b

class SessionExpiryInterval(PacketProperty):
    def __init__(self):
        self._id = 0x11

class AssignedClientIdentifier(PacketProperty):
    def __init__(self):
        self._id = 0x12

class ServerKeepAlive(PacketProperty):
    def __init__(self):
        self._id = 0x13

class AuthenticationMethod(PacketProperty):
    def __init__(self):
        self._id = 0x15

class AuthenticationData(PacketProperty):
    def __init__(self):
        self._id = 0x16

class RequestProblemInformation(PacketProperty):
    def __init__(self):
        self._id = 0x17

class WillDelayInterval(PacketProperty):
    def __init__(self):
        self._id = 0x18

class RequestResponseInformation(PacketProperty):
    def __init__(self):
        self._id = 0x19

class ResponseInformation(PacketProperty):
    def __init__(self):
        self._id = 0x1a

class ServerReference(PacketProperty):
    def __init__(self):
        self._id = 0x1c

class ReasonString(PacketProperty):
    def __init__(self):
        self._id = 0x1f

class ReceiveMaximum(PacketProperty):
    def __init__(self):
        self._id = 0x21

class TopicAliasMaximum(PacketProperty):
    def __init__(self):
        self._id = 0x22

class TopicAlias(PacketProperty):
    def __init__(self):
        self._id = 0x23

class MaximumQoS(PacketProperty):
    def __init__(self):
        self._id = 0x24

class RetainAvailable(PacketProperty):
    def __init__(self):
        self._id = 0x25

class UserProperty(PacketProperty):
    def __init__(self):
        self._id = 0x26

class MaximumPacketSize(PacketProperty):
    def __init__(self):
        self._id = 0x27

class WildcardSubscriptionAvailable(PacketProperty):
    def __init__(self):
        self._id = 0x28

class SubscriptionIdentifierAvailable(PacketProperty):
    def __init__(self):
        self._id = 0x29

class SharedSubscriptionAvailable(PacketProperty):
    def __init__(self):
        self._id = 0x2a
