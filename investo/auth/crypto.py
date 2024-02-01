from django.conf import settings
import pyseto
from pyseto import Key
import logging
import os

base_dir = settings.BASE_DIR
private_file = "private_key.pem"
public_file = "public_key.pem"


def encode(data, footer, implicit_assertion):
    logger = logging.getLogger("django")
    try:

        with open(os.path.join(base_dir, private_file)) as key_file:
            private_key = Key.new(4, "public", key_file.read())
        token = pyseto.encode(
            private_key,
            payload=str(data).encode("utf-8"),
            footer=str(data).encode("utf-8"),  # Optional
            implicit_assertion=str(implicit_assertion).encode("utf-8"),  # Optional
        )

        return token
    except Exception as e:
        logger.error("Failed to encode" + str(e))
        return ""


def decode(encoded_text, implicit_assertion):
    logger = logging.getLogger("django")
    try:

        with open(os.path.join(base_dir, public_file)) as key_file:
            public_key = Key.new(4, "public", key_file.read())
        decoded = pyseto.decode(
            public_key,
            encoded_text,
            implicit_assertion=str(implicit_assertion).encode("utf-8")
        )

        return decoded.payload
    except Exception as e:
        logger.error("Failed to encode" + str(e))
        return ""
