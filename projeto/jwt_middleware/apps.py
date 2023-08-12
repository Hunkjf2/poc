from django.apps import AppConfig


class JwtMiddlewareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jwt_middleware'
