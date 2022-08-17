class VariableByteInteger:
    """MQTT VariableByteInteger helper class"""

    _MULTIPLIER = 1 << 7
    _MAX_BYTES = 3
    _MAX_VALUE = 0xfffffff

    @classmethod
    def encode(cls, value: int) -> bytes:
        """Encode integer value to a VariableByteInteger.

        Encodes an integer value to a VariableByteInteger according to the mqtt-v5.0
        specification. Given value must be an integer within the 0-268435455 (0x0-0xfffffff) range.

        Args:
            value: An integer value to encode

        Returns:
            A bytes object containing the encoded integer value as a VariableByteInteger.

        Raises:
            ValueError: An error occurred when given an invalid value.
        """
        if not isinstance(value, int):
            raise ValueError(f"invalid value type '{type(value)}'; must be an integer")
        if not 0 <= value <= cls._MAX_VALUE:
            raise ValueError(f"value out of valid range: {value} not between 0 and 268435455")
        data = bytearray()

        while value > 0 or len(data) == 0:
            encoded = int(value % cls._MULTIPLIER)
            value //= cls._MULTIPLIER

            if value > 0:
                encoded |= cls._MULTIPLIER

            data.append(encoded)

        return bytes(data)

    @classmethod
    def decode(cls, data: bytes) -> int:
        """Decode VariableByteInteger to an integer.

        Decodes a VariableByteInteger to an integer according to the mqtt-v5.0
        specification. Givien data length must not exceed 4 bytes.

        Args:
            data: A bytes object to decode.

        Returns:
            An integer value decoded from the passed VariableByteInteger.

        Raises:
            ValueError: An error occurred when a malformed VariableByteInteger is given.
        """
        value = 0
        multiplier = 1
        for encoded in data:
            value += (encoded & (cls._MULTIPLIER - 1)) * multiplier

            if multiplier > cls._MULTIPLIER ** cls._MAX_BYTES:
                raise ValueError("malformed VariableByteInteger")

            multiplier *= cls._MULTIPLIER

            if encoded & cls._MULTIPLIER == 0:
                break

        return value
