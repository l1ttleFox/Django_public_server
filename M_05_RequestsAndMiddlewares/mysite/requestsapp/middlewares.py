from django.http import HttpRequest
from django.core.exceptions import PermissionDenied
import time


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.all_request = dict()
        self.exceptions_count = 0
        
    def __call__(self, request: HttpRequest):
        last_call = self.all_request.get(request.META.get('REMOTE_ADDR'))
        if last_call is None or time.time() - last_call > 1:
            response = self.get_response(request)
        else:
            raise PermissionDenied
        self.all_request[request.META.get('REMOTE_ADDR')] = time.time()
        return response