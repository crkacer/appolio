# middleware.py

import logging
import time
from django.shortcuts import redirect
from django.urls import reverse

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture the start time of the request
        start_time = time.time()

        # Process the request and get the response
        response = self.get_response(request)

        # Calculate the total processing time
        total_time = time.time() - start_time

        # Log the request details
        logger.info(
            f"Path: {request.path}, Method: {request.method}, Status Code: {response.status_code}, "
            f"Total Time: {total_time:.2f} seconds"
        )

        return response


class AuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to the login page or any other desired URL
            return redirect(reverse('login'))  # Adjust the URL name as needed

        # Continue processing the request
        response = self.get_response(request)

        return response
