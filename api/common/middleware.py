import json

from django.conf import settings
from django.http import HttpResponse


class NonHtmlDebugToolbarMiddleware:
    """
    Django Debug Toolbar usually only works for views that return HTML.
    This middleware wraps any non-HTML response in HTML if the request
    has a 'debug' query parameter (e.g. http://localhost/foo?debug).
    Special handling for json (pretty printing) and binary data (only
    show data length).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if settings.DEBUG and request.GET.get('debug') == '':
            if response['Content-Type'] == 'application/octet-stream':
                new_content = (
                    f'<html><body>Binary Data, '
                    f'Length: {len(response.content)}</body></html>'
                )
                response = HttpResponse(new_content)

            elif response['Content-Type'] != 'text/html':
                content = response.content
                try:
                    json_ = json.loads(content)
                    content = json.dumps(json_, sort_keys=True, indent=4)
                except ValueError:
                    pass

                response = HttpResponse(
                    f'<html><body><pre>{content}</pre></body></html>')

        return response
