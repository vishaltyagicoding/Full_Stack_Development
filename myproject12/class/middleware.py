from django.utils.deprecation import MiddlewareMixin
import datetime
class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"This is my middleware {request.path}")
        print(datetime.datetime.now())

    def process_response(self, request, response):
        print(f"This is my response middleware {response.path}")
        print(datetime.datetime.now())
        