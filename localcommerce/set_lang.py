import pdb
import logging
from django.utils import translation

LANGUAGES = ['en', 'es', 'fr']

def SetLangMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # pdb.set_trace()
        host = request.get_host().split('.')
        if host and host[0] in LANGUAGES:
            lang = host[0]
            logging.debug("Choosing language: {0}".format(lang))
            translation.activate(lang)
            request.LANGUAGE_CODE = lang

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
