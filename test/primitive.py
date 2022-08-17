from unittest import TestCase

from mqtt.primitive import VariableByteInteger

class VariableByteIntegerTests(TestCase):
    def test_encode_decode(self):
        with self.assertRaises(ValueError):
            VariableByteInteger.encode("")
        with self.assertRaises(ValueError):
            VariableByteInteger.encode(-1)
        with self.assertRaises(ValueError):
            VariableByteInteger.encode(0x10000000)

        for value in range(0, 0x10000000, 0xfffffff // 0x7f):
            encoded = VariableByteInteger.encode(value)
            decoded, _ = VariableByteInteger.decode(encoded)
            assert value == decoded

