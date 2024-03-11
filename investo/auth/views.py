from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from pyseto import Key
from django.conf import settings
from .crypto import encode, decode
from datetime import date, datetime
from uuid import uuid4

@api_view(['POST'])
def login(request):

    logger = logging.getLogger("django")
    try:
        data = request.data
        email = data.get('email')
        password = data.get('password')
        token = encode(email, "random_footer", str(uuid4()))
        token_decode = token.decode("utf-8")
        resp = Response()
        resp.set_cookie(key="token", value=token_decode, httponly=False)
        resp.data = {
            "token": token_decode
        }

        return resp

    except Exception as e:
        logger.error(str(e))
        return Response({"token": None, "error": str(e)})


@api_view(['POST'])
def test_token(request):
    logger = logging.getLogger("django")
    try:
        data = request.data
        token = data.get('token')
        decoded_token = decode(token, "imp")
        return Response({
            "decode": decoded_token
        })

    except Exception as e:
        logger.error(str(e))
        return Response({"error": str(e)})
