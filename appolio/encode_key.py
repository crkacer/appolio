import pyseto
from pyseto import Key
import os
from django.conf import settings


def encode_key(data):
    base_dir = settings.BASE_DIR
    private_file = "private_key.pem"

    with open(os.path.join(base_dir, private_file)) as key_file:
        private_key = Key.new(4, "public", key_file.read())
    token = pyseto.encode(
        private_key,
        payload=bin(data),
        footer=b"This is a footer",  # Optional
        implicit_assertion=b"xyz",  # Optional
    )

    return token


def decode_key(data):
    base_dir = settings.BASE_DIR
    public_file = "public_key.pem"

    with open(os.path.join(base_dir, public_file)) as key_file:
        public_key = Key.new(4, "public", key_file.read())
    decoded = pyseto.decode(public_key, data, implicit_assertion=b"xyz")

    return decoded
