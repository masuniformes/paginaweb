import logging
from django.http import HttpResponsePermanentRedirect

logger = logging.getLogger('django')

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        scheme = request.scheme  # Detecta si es HTTP o HTTPS
        logger.debug(f"Host actual: {host}, Esquema: {scheme}")

        # Redirigir a HTTPS y añadir "www."
        if host == "masuniformes.com.uy":
            redirect_url = f"https://www.masuniformes.com.uy{request.path}"
            logger.debug(f"Redirigiendo a: {redirect_url}")
            return HttpResponsePermanentRedirect(redirect_url)

        if scheme == "http":
            redirect_url = f"https://{host}{request.path}"
            logger.debug(f"Forzando HTTPS: {redirect_url}")
            return HttpResponsePermanentRedirect(redirect_url)

        response = self.get_response(request)
        return response
