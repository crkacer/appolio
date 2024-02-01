import unittest
import pyseto
from pyseto import Key
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appolio.settings")

# Configure Django settings
import django
django.setup()
class TestPaseto(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_paseto = self.test_paseto()

    def test_paseto(self):

        base_dir = settings.BASE_DIR
        private_file = "private_key.pem"
        public_file = "public_key.pem"

        with open(os.path.join(base_dir, private_file)) as key_file:
            private_key = Key.new(4, "public", key_file.read())
        token = pyseto.encode(
            private_key,
            payload=b'{"data": "this is a signed message", "exp": "2022-01-01T00:00:00+00:00"}',
            footer=b"This is a footer",  # Optional
            implicit_assertion=b"xyz",  # Optional
        )

        with open(os.path.join(base_dir, public_file)) as key_file:
            public_key = Key.new(4, "public", key_file.read())
        decoded = pyseto.decode(public_key, token, implicit_assertion=b"xyz")

        assert (
            decoded.payload
            == b'{"data": "this is a signed message", "exp": "2022-01-01T00:00:00+00:00"}'
        )
        assert decoded.footer == b"This is a footer"
        assert decoded.version == "v4"
        assert decoded.purpose == "public"