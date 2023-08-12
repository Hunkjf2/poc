from django.http import JsonResponse
from jwt.exceptions import ExpiredSignatureError
import jwt
from django.conf import settings

NOT_AUTH_PATH = ['/users/login']
class JwtMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        if request.path in NOT_AUTH_PATH:
            return self.get_response(request)

        try:
            token = request.headers.get('Authorization')
            jwt.decode(jwt=token,
                        key=settings.SECRET_KEY,
                        algorithms=["HS256"])

            return self.get_response(request)
        except Exception as error:
            return JsonResponse({'error': 'Token not valid'}, status=403)