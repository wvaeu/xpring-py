# Stubs for fastecdsa.tests.test_signature_encoding (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..encoding.der import DEREncoder, InvalidDerSignature
from unittest import TestCase

class TestSignatureEncoding(TestCase):
    def test_encode_der_signature(self) -> None: ...
    def test_decode_der_signature(self) -> None: ...
